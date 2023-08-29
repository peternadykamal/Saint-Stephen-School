import * as utils from "./utils.js";
/* -------------------------------------------------------------------------- */
var tagsIDs = [];

// List with handle
var sortable = Sortable.create(tagsList, {
  handle: ".bi-grip-vertical",
  animation: 150,
  dataIdAttr: "data-id",
  delay: 150,
  delayOnTouchOnly: true,
  filter: ".undraggable",
  onMove: function (evt) {
    if (evt.related && evt.related.classList.contains("undraggable")) {
      return false;
    }
  },
});

sortable.option("onUpdate", function (evt) {
  tagsIDs = sortable.toArray();
  console.log(tagsIDs);
});

/* ------------------------------- edit a tag ------------------------------- */
const listItems = sortable.el.querySelectorAll(".list-group-item");
const editTagSection = document.querySelector(".editTagContent");

listItems.forEach((item) => {
  item.addEventListener("click", async () => {
    utils.toggleVisibility("editTagSpinner", "addEditTag");
    const itemFetchUrl = item.getAttribute("get-tag");
    const response = await utils.makeRequest("GET", itemFetchUrl);
    utils.toggleVisibility("editTagContent", "addEditTag");
    editTagSection.innerHTML = response["form_html"];
    settingUpTagUpdateFormButtons();
  });
});

/* --------------------- the use case of updating a tag --------------------- */
function settingUpTagUpdateFormButtons() {
  // make sure the form doesn't get sumitted when pressing enter
  const form = editTagSection.querySelector(".editTagForm");
  form.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
    }
  });
  // setting up save button
  const saveTagButton = editTagSection.querySelector(".saveTagChanges");
  saveTagButton.addEventListener("click", async () => {
    utils.toggleVisibility("editTagSpinner", "addEditTag");
    const formSubmitUrl = form.getAttribute("action");
    const options = {
      method: "POST",
      headers: {
        "X-CSRFToken": form.querySelector("input[name=csrfmiddlewaretoken]")
          .value,
      },
      body: new FormData(form),
    };
    const fullUrl = utils.getApiUrl(formSubmitUrl);
    const response = await fetch(fullUrl, options);
    const json = await response.json();
    utils.toggleVisibility("editTagContent", "addEditTag");
    console.log(json["status"]);
    if (json["status"] === "fail") {
      editTagSection.innerHTML = json["form_html"];
      settingUpTagUpdateFormButtons();
    } else window.location = window.location;
  });
  // setting up cancel button
  const cancelTagButton = editTagSection.querySelector(".cancelButton");
  cancelTagButton.addEventListener("click", () => {
    utils.toggleVisibility("editTagMessage", "addEditTag");
  });

  const toastTrigger = editTagSection.querySelector("#confirmationToastBtn");
  const toastLiveExample = editTagSection.querySelector("#confirmationToast");

  if (toastTrigger) {
    const toastBootstrap =
      bootstrap.Toast.getOrCreateInstance(toastLiveExample);
    toastTrigger.addEventListener("click", () => {
      console.log("object");
      toastBootstrap.show();
    });
  }

  // setting up delete button
  const deleteTagButton = editTagSection.querySelector("#deleteTag");
  deleteTagButton.addEventListener("click", async () => {
    await utils.makeRequest("DELETE", deleteTagButton.getAttribute("url"));
    window.location = window.location;
  });
}
/* ---------------------- the use case to add a new tag --------------------- */
const addTagSection = document.querySelector(".addTagContent");
// add event listener on add button to show the add tag form
const addTagButton = document.querySelector("#addNewTag");
addTagButton.addEventListener("click", async () => {
  utils.toggleVisibility("editTagSpinner", "addEditTag");
  const itemFetchUrl = addTagButton.getAttribute("url");
  console.log(itemFetchUrl);
  const response = await utils.makeRequest("GET", itemFetchUrl);
  utils.toggleVisibility("addTagContent", "addEditTag");
  addTagSection.innerHTML = response["form_html"];
  settingUpTagAddFormButtons();
});

function settingUpTagAddFormButtons() {
  // make sure the form doesn't get sumitted when pressing enter
  const form = addTagSection.querySelector(".addTagForm");
  form.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
    }
  });

  // add event listener on cancel button
  const cancelAddButton = addTagSection.querySelector(".cancelButton");
  cancelAddButton.addEventListener("click", () => {
    utils.toggleVisibility("editTagMessage", "addEditTag");
  });

  // add event listener on save button
  const saveTagButton = addTagSection.querySelector(".saveTagChanges");
  saveTagButton.addEventListener("click", async () => {
    utils.toggleVisibility("editTagSpinner", "addEditTag");
    const formSubmitUrl = form.getAttribute("action");
    const options = {
      method: "POST",
      headers: {
        "X-CSRFToken": form.querySelector("input[name=csrfmiddlewaretoken]")
          .value,
      },
      body: new FormData(form),
    };
    const fullUrl = utils.getApiUrl(formSubmitUrl);
    const response = await fetch(fullUrl, options);
    const json = await response.json();
    utils.toggleVisibility("addTagContent", "addEditTag");
    console.log(json["status"]);
    if (json["status"] === "fail") {
      addTagSection.innerHTML = json["form_html"];
      settingUpTagAddFormButtons();
    } else window.location = window.location;
  });
}
/* ------------------ the use case to change tags hierarchy ----------------- */
const mainButtons = document.querySelector("#addTag-updateHierarchy-buttons");
const hierarchyControlButtons = document.querySelector(
  "#update-hierarchy-buttons"
);
// add event listener on updateHierarchy button
// get updateHierarchy button
const updateHierarchyButton = document.querySelector("#updateHierarchy");
updateHierarchyButton.addEventListener("click", () => {
  mainButtons.classList.add("d-none");
  hierarchyControlButtons.classList.remove("d-none");
  utils.elementVisibility(true, ".bi-grip-vertical");
});
// add event listener on cancelUpdateHierarchy button
// get cancelUpdateHierarchy button
const cancelUpdateHierarchyButton = document.querySelector(
  "#cancelUpdateHierarchy"
);
cancelUpdateHierarchyButton.addEventListener("click", () => {
  // refresh the page
  window.location = window.location;
});
// add event listener on saveHierarchy button
// get saveHierarchy button
const saveHierarchyButton = document.querySelector("#saveHierarchy");
saveHierarchyButton.addEventListener("click", async () => {
  const response = await utils.makeRequest("POST", "/tag/updateHierarchy/", {
    newHierarchy: sortable.toArray(),
  });
  window.location = window.location;
});
