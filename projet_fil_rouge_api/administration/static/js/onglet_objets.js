"use strict";

//Fonction pour faire apparaître les champs et le bouton de validation
export function champsAjouterObjet() {
  document.getElementById("ajouter_objet_value").innerHTML = `
    <p>Saisir les données du nouveau objet :</p>
    <label>Nom de l'objet</label>
    <input type="text" id="designation_objet" required minlength="1" size="10" onblur="getValueDesignation_objet()">
    <label>Poids de l'objet</label>
    <input type="number" step=".0001" id="poids_objet" required minlength="1" size="10" onblur="getValuePoids_objet()">
    <label>Ordre IMP de l'objet</label>
    <input type="number" id="imp_objet" required minlength="1" size="10" onblur="getValueIMP_objet()">
    <label>Publicitaire de l'objet</label>
    <input type="number" step=".0001" id="publicitaire_objet" required minlength="1" size="10" onblur="getValuePublicitaire_objet()">
    <label>Conditionnement de l'objet</label>
    <input type="number" id="conditionnement_objet" required minlength="1" size="10" onblur="getValueConditionnement_objet()">
    <label>Points de l'objet</label>
    <input type="number" id="points_objet" required minlength="1" size="10" onblur="getValuePoints_objet()">
    <div id="ajouter_objet_insertion" onclick="insertionObjet()">Valider l'ajout de l'objet</div>
    <div id="annuler_objet_insertion" onclick="annulerInsertionObjet()">Annuler l'ajout de l'objet</div> 
  `;
}

//Déclaration des variables hors des fonctions
let designation_objet_value = "";
let poids_objet_value = "";
let imp_objet_value = "";
let publicitaire_objet_value = "";
let conditionnement_objet_value = "";
let points_objet_value = "";

//Affectation de la valeur de la désignation de l'objet
export function getValueDesignation_objet() {
  designation_objet_value = document.getElementById("designation_objet").value;
}
//Affection de la valeur du poids de l'objet
export function getValuePoids_objet() {
  poids_objet_value = document.getElementById("poids_objet").value;
}
//Affectation de la valeur de l'importance IMP de l'objet
export function getValueIMP_objet() {
  imp_objet_value = document.getElementById("imp_objet").value;
}
//Affectation de la valeur du publicitaire de l'objet
export function getValuePublicitaire_objet() {
  publicitaire_objet_value =
    document.getElementById("publicitaire_objet").value;
}
//Affectation de la valeur du conditionnement de l'objet
export function getValueConditionnement_objet() {
  conditionnement_objet_value = document.getElementById(
    "conditionnement_objet"
  ).value;
}
//Affectation de la valeur des points de l'objet
export function getValuePoints_objet() {
  points_objet_value = document.getElementById("points_objet").value;
}

//Fonction pour insérer le objet dans la base de données
export function insertionObjet() {
  document.location.href =
    "/home/ajoutObjet/" +
    designation_objet_value +
    "_" +
    poids_objet_value +
    "_" +
    imp_objet_value +
    "_" +
    publicitaire_objet_value +
    "_" +
    conditionnement_objet_value +
    "_" +
    points_objet_value;
}

//Fonction pour insérer le objet dans la base de données
export function annulerInsertionObjet() {
  document.getElementById("ajouter_objet_value").innerHTML = "";
}

//Déclaration des variables hors des fonctions
let designation_objet_modifier_value = "";
let poids_objet_modifier_value = "";
let imp_objet_modifier_value = "";
let publicitaire_objet_modifier_value = "";
let conditionnement_objet_modifier_value = "";
let points_objet_modifier_value = "";

let ancienne_id_objet = "Null";

//Fonction pour faire apparaître les champs pour modifier un objet
export function champsModifierLigneObjet(id_objet) {
  if (ancienne_id_objet != "Null") {
    document.getElementById("boutton_modifier_" + ancienne_id_objet).innerHTML =
      "Modifier cette ligne";
  }
  document.getElementById("boutton_modifier_" + id_objet).innerHTML =
    "En cours de modification";
  designation_objet_modifier_value = "";
  poids_objet_modifier_value = "";
  imp_objet_modifier_value = "";
  publicitaire_objet_modifier_value = "";
  conditionnement_objet_modifier_value = "";
  points_objet_modifier_value = "";
  document.getElementById("modifier_objet_value").innerHTML = "";
  document.getElementById("modifier_objet_value").innerHTML +=
    `
    <p>Saisir les nouvelles données de l'objet ` +
    id_objet +
    ` :</p>
    <label>Nom de l'objet</label>
    <input type="text" id="designation_objet_modifier" required minlength="1" size="10" onblur="getValueModifierDesignation_objet()">
    <label>Poids de l'objet</label>
    <input type="number" step=".0001" id="poids_objet_modifier" required minlength="1" size="10" onblur="getValueModifierPoids_objet()">
    <label>Ordre IMP de l'objet</label>
    <input type="number" id="imp_objet_modifier" required minlength="1" size="10" onblur="getValueModifierIMP_objet()">
    <label>Publicitaire de l'objet</label>
    <input type="number" step=".0001" id="publicitaire_objet_modifier" required minlength="1" size="10" onblur="getValueModifierPublicitaire_objet()">
    <label>Conditionnement de l'objet</label>
    <input type="number" id="conditionnement_objet_modifier" required minlength="1" size="10" onblur="getValueModifierConditionnement_objet()">
    <label>Points de l'objet</label>
    <input type="number" id="points_objet_modifier" required minlength="1" size="10" onblur="getValueModifierPoints_objet()">
    <div id="modifier_objet_insertion" onclick="modifierLigneObjet(` +
    id_objet +
    `)">Valider la modification de l'objet</div>
    <div onclick="supprimerChampsModifierLigneObjet(` +
    id_objet +
    `)">Annuler la modification de l'objet</div>
  `;
  ancienne_id_objet = id_objet;
}

export function supprimerChampsModifierLigneObjet(id_objet) {
  document.getElementById("boutton_modifier_" + id_objet).innerHTML =
    "Modifier cette ligne";
  document.getElementById("modifier_objet_value").innerHTML = "";
}

//Affectation de la valeur de la désignation de l'objet
export function getValueModifierDesignation_objet() {
  designation_objet_modifier_value = document.getElementById(
    "designation_objet_modifier"
  ).value;
}
//Affection de la valeur du poids de l'objet
export function getValueModifierPoids_objet() {
  poids_objet_modifier_value = document.getElementById(
    "poids_objet_modifier"
  ).value;
}
//Affectation de la valeur de l'importance IMP de l'objet
export function getValueModifierIMP_objet() {
  imp_objet_modifier_value =
    document.getElementById("imp_objet_modifier").value;
}
//Affectation de la valeur du publicitaire de l'objet
export function getValueModifierPublicitaire_objet() {
  publicitaire_objet_modifier_value = document.getElementById(
    "publicitaire_objet_modifier"
  ).value;
}
//Affectation de la valeur du conditionnement de l'objet
export function getValueModifierConditionnement_objet() {
  conditionnement_objet_modifier_value = document.getElementById(
    "conditionnement_objet_modifier"
  ).value;
}
//Affectation de la valeur des points de l'objet
export function getValueModifierPoints_objet() {
  points_objet_modifier_value = document.getElementById(
    "points_objet_modifier"
  ).value;
}

//Fonction pour modifier la ligne d'un objet
export function modifierLigneObjet(id_objet) {
  document.location.href =
    "/home/modificationObjet/" +
    id_objet +
    "_" +
    designation_objet_modifier_value +
    "_" +
    poids_objet_modifier_value +
    "_" +
    imp_objet_modifier_value +
    "_" +
    publicitaire_objet_modifier_value +
    "_" +
    conditionnement_objet_modifier_value +
    "_" +
    points_objet_modifier_value;
}

//Fonction pour vérifier le status de l'objet
export function verifierStatus(id_objet, statusValue) {
  if (statusValue == 1) {
    document.getElementById("action_active_" + id_objet).innerHTML = `
      <div id="boutton_desactiver_${id_objet}" onclick="DesactiverObjet(${id_objet})">Désactiver</div>
    `;
  } else if (statusValue == 0) {
    document.getElementById("action_active_" + id_objet).innerHTML = `
      <div id="boutton_activer_${id_objet}" onclick="ActiverObjet(${id_objet})">Activer</div>
    `;
  }
}

//Fonction pour activer un objet
export function ActiverObjet(id_objet) {
  document.location.href = "/home/statusObjet/" + id_objet + "_" + "1";
}

//Fonction pour désactiver un objet
export function DesactiverObjet(id_objet) {
  document.location.href = "/home/statusObjet/" + id_objet + "_" + "0";
}
