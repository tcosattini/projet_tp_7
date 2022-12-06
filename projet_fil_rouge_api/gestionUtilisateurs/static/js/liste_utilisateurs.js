"use strict";

const currentForm = null;
export const addFormState = false;

export const showAddForm = (e, utilisateur) => {
  e.preventDefault();
  console.log({ utilisateur });
  currentForm = document.getElementById("add-form");
  currentForm.hidden = false;
};

export const showChangeForm = (e) => {
  e.preventDefault();
  currentForm = document.getElementById("change-form");
  currentForm.hidden = false;
};

export const cancelForm = (e) => {
  e.preventDefault();
  e.target.hidden = true;
  currentForm = null;
};
