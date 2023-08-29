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
const sectionContent = document.querySelector(".editTagContent");
const updateProfile = async () => {
  try {
    // const res = await api.post("/update-profile", form);
    // return res;
    await utils.sleep(2000);
    return true;
  } catch (err) {
    throw new Error("error.unknown");
  }
};

listItems.forEach((item) => {
  item.addEventListener("click", async () => {
    const itemId = item.getAttribute("data-id");
    const itemText = item.textContent;
    sectionContent.textContent = `Clicked Item ID: ${itemId}, Text: ${itemText}`;

    utils.toggleVisibility("editTagSpinner", "addEditTag");
    const res = await updateProfile();
    console.log(res);
    utils.toggleVisibility("editTagContent", "addEditTag");
  });
});
/* -------------- the use case to change the order of the tags -------------- */
function dragIconVisibility(isVisible) {
  var elements = document.querySelectorAll(".bi-grip-vertical");

  elements = Array.from(elements);
  // remove the first and last elements
  elements.shift(); // Remove the first element
  elements.pop(); // Remove the last element

  elements.forEach((element) => {
    if (!isVisible) {
      element.classList.add("d-none");
    } else {
      element.classList.remove("d-none");
    }
  });
}
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
  window.location.reload();
});
// add event listener on saveHierarchy button
// get saveHierarchy button
const saveHierarchyButton = document.querySelector("#saveHierarchy");
saveHierarchyButton.addEventListener("click", async () => {
  const response = await utils.makeRequest("POST", "/tag/updateHierarchy/", {
    newHierarchy: sortable.toArray(),
  });
  window.location.reload();
});
/* -------------------------------------------------------------------------- */
const toastTrigger = document.getElementById("confirmationToastBtn");
const toastLiveExample = document.getElementById("confirmationToast");

if (toastTrigger) {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
  toastTrigger.addEventListener("click", () => {
    toastBootstrap.show();
  });
}
