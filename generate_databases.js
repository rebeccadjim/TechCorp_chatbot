const fs = require('fs');
const path = require('path');

// Données des employés (extraites du code React)
const employees = [
  { id: 1, nom: "Dupont", prenom: "Marie", poste: "Directrice Générale", anciennete: 12, dateEntree: "2013-01-15", salaireBrut: 85000, bonus: 15000, departement: "Direction" },
  { id: 2, nom: "Martin", prenom: "Pierre", poste: "Directeur Technique", anciennete: 8, dateEntree: "2017-03-20", salaireBrut: 72000, bonus: 10000, departement: "IT" },
  { id: 3, nom: "Bernard", prenom: "Sophie", poste: "Chef de Projet Senior", anciennete: 6, dateEntree: "2019-06-10", salaireBrut: 58000, bonus: 5000, departement: "Projets" },
  { id: 4, nom: "Dubois", prenom: "Lucas", poste: "Développeur Senior", anciennete: 5, dateEntree: "2020-02-01", salaireBrut: 52000, bonus: 4000, departement: "IT" },
  { id: 5, nom: "Thomas", prenom: "Emma", poste: "Responsable RH", anciennete: 7, dateEntree: "2018-09-15", salaireBrut: 48000, bonus: 3500, departement: "RH" },
  { id: 6, nom: "Petit", prenom: "Alexandre", poste: "Chef de Projet", anciennete: 4, dateEntree: "2021-04-12", salaireBrut: 45000, bonus: 3000, departement: "Projets" },
  { id: 7, nom: "Robert", prenom: "Camille", poste: "Développeur", anciennete: 3, dateEntree: "2022-01-08", salaireBrut: 42000, bonus: 2500, departement: "IT" },
  { id: 8, nom: "Richard", prenom: "Thomas", poste: "Comptable Senior", anciennete: 9, dateEntree: "2016-07-01", salaireBrut: 46000, bonus: 3000, departement: "Finance" },
  { id: 9, nom: "Durand", prenom: "Julie", poste: "Chargée de Communication", anciennete: 2, dateEntree: "2023-03-15", salaireBrut: 38000, bonus: 2000, departement: "Marketing" },
  { id: 10, nom: "Moreau", prenom: "Antoine", poste: "Assistant RH", anciennete: 1, dateEntree: "2024-01-10", salaireBrut: 32000, bonus: 1500, departement: "RH" },
  { id: 11, nom: "Simon", prenom: "Laura", poste: "Designer UX/UI", anciennete: 3, dateEntree: "2022-05-20", salaireBrut: 44000, bonus: 2500, departement: "Design" },
  { id: 12, nom: "Laurent", prenom: "Maxime", poste: "Commercial Senior", anciennete: 6, dateEntree: "2019-10-01", salaireBrut: 50000, bonus: 8000, departement: "Commercial" },
  { id: 13, nom: "Lefebvre", prenom: "Chloé", poste: "Analyste Données", anciennete: 2, dateEntree: "2023-02-14", salaireBrut: 40000, bonus: 2000, departement: "IT" },
  { id: 14, nom: "Michel", prenom: "David", poste: "Développeur Junior", anciennete: 1, dateEntree: "2024-06-01", salaireBrut: 35000, bonus: 1500, departement: "IT" },
  { id: 15, nom: "Garcia", prenom: "Léa", poste: "Assistante Direction", anciennete: 4, dateEntree: "2021-08-15", salaireBrut: 36000, bonus: 2000, departement: "Direction" }
];

// Créer le dossier data s'il n'existe pas
const dataDir = './data/Documents';
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
  console.log('📁 Dossier ./data créé');
}

// Fonction pour générer le CSV
function generateCSV() {
  const separator = ';';

  const headers = [
    'ID',
    'Nom',
    'Prenom',
    'Poste',
    'Departement',
    'Date_Entree',
    'Anciennete_ans',
    'Salaire_Brut_euros',
    'Bonus_euros',
    'Remuneration_Totale_euros'
  ];

  const csvContent = [
    headers.join(separator),
    ...employees.map(emp => [
      emp.id,
      emp.nom,
      emp.prenom,
      `"${emp.poste}"`,
      emp.departement,
      emp.dateEntree,
      emp.anciennete,
      emp.salaireBrut,
      emp.bonus,
      emp.salaireBrut + emp.bonus
    ].join(separator))
  ].join('\n');

  const filePath = path.join(dataDir, 'salaires_techcorp.csv');
  fs.writeFileSync(filePath, '\ufeff' + csvContent, 'utf8');

  console.log(`✅ Fichier CSV créé : ${filePath}`);
}
// Fonction pour générer l'Excel (format XML)
function generateExcel() {
  const xmlHeader = '<?xml version="1.0"?><?mso-application progid="Excel.Sheet"?>';
  const workbookXML = '<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet" xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet">';
  const worksheetStart = '<Worksheet ss:Name="Salaires 2025"><Table>';
  
  // En-têtes
  let rows = '<Row>';
  const headers = ['ID', 'Nom', 'Prénom', 'Poste', 'Département', 'Date Entrée', 'Ancienneté (ans)', 'Salaire Brut (€)', 'Bonus (€)', 'Rémunération Totale (€)'];
  headers.forEach(header => {
    rows += `<Cell><Data ss:Type="String">${header}</Data></Cell>`;
  });
  rows += '</Row>';
  
  // Données
  employees.forEach(emp => {
    rows += '<Row>';
    rows += `<Cell><Data ss:Type="Number">${emp.id}</Data></Cell>`;
    rows += `<Cell><Data ss:Type="String">${emp.nom}</Data></Cell>`;
    rows += `<Cell><Data ss:Type="String">${emp.prenom}</Data></Cell>`;
    rows += `<Cell><Data ss:Type="String">${emp.poste}</Data></Cell>`;
    rows += `<Cell><Data ss:Type="String">${emp.departement}</Data></Cell>`;
    rows += `<Cell><Data ss:Type="String">${emp.dateEntree}</Data></Cell>`;
    rows += `<Cell><Data ss:Type="Number">${emp.anciennete}</Data></Cell>`;
    rows += `<Cell><Data ss:Type="Number">${emp.salaireBrut}</Data></Cell>`;
    rows += `<Cell><Data ss:Type="Number">${emp.bonus}</Data></Cell>`;
    rows += `<Cell><Data ss:Type="Number">${emp.salaireBrut + emp.bonus}</Data></Cell>`;
    rows += '</Row>';
  });
  
  const worksheetEnd = '</Table></Worksheet>';
  const workbookEnd = '</Workbook>';
  
  const fullXML = xmlHeader + workbookXML + worksheetStart + rows + worksheetEnd + workbookEnd;
  
  const filePath = path.join(dataDir, 'salaires_techcorp.xls');
  fs.writeFileSync(filePath, fullXML, 'utf8');
  console.log(`✅ Fichier Excel créé : ${filePath}`);
}

// Exécuter la génération
console.log('🚀 Génération des fichiers de données...\n');
generateCSV();
generateExcel();
console.log('\n✨ Génération terminée avec succès!');
console.log(`📊 ${employees.length} employés exportés`);