/* -------------------------------------------------------------------------- */
function getApiUrl(path) {
  const protocol = window.location.protocol;
  const hostname = window.location.hostname;
  const port = window.location.port;

  let apiUrl;
  if (!isNaN(port) && port !== "") {
    apiUrl = `${protocol}//${hostname}:${port}${path}`;
  } else {
    apiUrl = `${protocol}//${hostname}${path}`;
  }

  return apiUrl;
}
function getCSRFToken() {
  const cookieValue = document.cookie
    .split("; ")
    .find((cookie) => cookie.startsWith("csrftoken="))
    .split("=")[1];

  return cookieValue;
}

// --------------------------------------------------------------

function previewImage() {
  const imageInput = document.getElementById("profile_image");
  const imagePreview = document.getElementById("imagePreview");

  imageInput.addEventListener("change", function () {
    readURL(this);
  });

  function readURL(input) {
    if (input.files && input.files[0]) {
      const reader = new FileReader();

      reader.onload = function (e) {
        imagePreview.setAttribute("src", e.target.result);
        imagePreview.style.display = "block";
      };

      reader.readAsDataURL(input.files[0]);
    }
  }
}
document.addEventListener("DOMContentLoaded", previewImage);

// --------------------------------------------------------------

const fullNameInputs = document.querySelectorAll("#fullnameInput input");
const hiddenNameInput = document.getElementById("hiddenNameInput");

// Function to update the hidden input with the concatenated full name
function updateNameInput() {
  const fullName = Array.from(fullNameInputs)
    .map((input) => input.value.trim())
    .join(" ");
  hiddenNameInput.value = fullName;
}

// Function to handle keydown event and move the cursor to the next input on space press
function handleKeyDown(event, currentIndex) {
  const condition =
    (event.key === "Spacebar" || event.key === " " || event.key === "Space") &&
    event.target.value.trim() !== "";

  if (condition) {
    event.preventDefault();
    const nextIndex = currentIndex + 1;
    if (nextIndex < fullNameInputs.length) {
      fullNameInputs[nextIndex].focus();
    }
  }
}

function splittingNameIfPasted(event, index) {
  event.preventDefault();
  const names = event.target.value.trim().split(" ");
  if (names.length > fullNameInputs.length - index) {
    fullNameInputs[index].value = "";
    return;
  }
  for (let i = 0; i < names.length; i++) {
    fullNameInputs[index + i].value = names[i];
  }
}

// Add event listeners to each input
fullNameInputs.forEach((input, index) => {
  input.addEventListener("input", updateNameInput);
  input.addEventListener("keydown", (event) => handleKeyDown(event, index));
  input.addEventListener("input", (event) =>
    splittingNameIfPasted(event, index)
  );
});
// --------------------------------------------------------------
const schoolLevelDropdown = document.getElementById("school_level");

function populateDropdown(data, querySelectorValue) {
  const dropdown = document.querySelector(querySelectorValue);
  dropdown.innerHTML = "";

  data.forEach((year) => {
    const option = document.createElement("option");
    option.value = year;
    option.textContent = year;
    dropdown.appendChild(option);
  });
}
// this function assume that the select element have an attribute called selected that contain
// the value that should be selected
function setSelectedLevel(querySelectorValue) {
  const element = document.querySelector(querySelectorValue);
  const selectedValue = element.getAttribute("selected");
  console.log(selectedValue);
  const optionToSelect = document.querySelector(
    `${querySelectorValue} option[value="${selectedValue}"]`
  );
  if (optionToSelect) {
    optionToSelect.selected = true;
  }
  console.log();
}
function elementVisibility(isVisible, querySelectorValue) {
  element = document.querySelector(querySelectorValue);
  if (!isVisible) {
    element.classList.add("d-none");
  } else {
    element.classList.remove("d-none");
  }
}
async function handleSchoolLevelChange() {
  const selectedSchoolLevel = schoolLevelDropdown.value;
  const url = getApiUrl("/u/get_school_level_years/");

  try {
    const response = await fetch(url, {
      method: "POST", // or 'GET' depending on your server-side implementation
      body: JSON.stringify({ school_level_id: selectedSchoolLevel }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(),
      },
    });

    const data = await response.json();
    switch (data.show) {
      case "textField":
        elementVisibility(false, "#school_level_year_container");
        elementVisibility(true, "#job_container");
        break;
      case "dropBox":
        elementVisibility(true, "#school_level_year_container");
        elementVisibility(false, "#job_container");
        break;
      default:
        elementVisibility(false, "#school_level_year_container");
        elementVisibility(false, "#job_container");
        break;
    }

    populateDropdown(data.getSchoolLevelYears, "#current_school_level_year");
    setSelectedLevel("#current_school_level_year");
  } catch (error) {
    console.error("Error:", error);
  }
}

schoolLevelDropdown.addEventListener("change", handleSchoolLevelChange);
// --------------------------------------------------------------
const talmzaLevelDropdown = document.getElementById("talmza_level");

async function handleTalmzaLevelChange() {
  const selectedTalmzaLevel = talmzaLevelDropdown.value;
  const url = getApiUrl("/u/get_talmza_level_years/");

  try {
    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify({ talmza_level_id: selectedTalmzaLevel }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(),
      },
    });

    const data = await response.json();
    populateDropdown(data, "#current_talmza_level_year");
    setSelectedLevel("#current_talmza_level_year");
  } catch (error) {
    console.error("Error:", error);
  }
}

talmzaLevelDropdown.addEventListener("change", handleTalmzaLevelChange);
// --------------------------------------------------------------
// modal script
const mainForm = document.getElementById("mainForm");

document
  .getElementById("modalSubmitButton")
  .addEventListener("click", function () {
    const modalInputExpenses =
      document.querySelector('[name="expenses"]').value;
    document.querySelector("#amount_of_money_payed").value = modalInputExpenses;
    mainForm.submit();
  });
/* -------------------------------------------------------------------------- */
// search bar
const searchButton = document.getElementById("searchButton");
const registrationInput = document.getElementById("registration_number");

function openLinkWithGETParameter(path, parameterName, parameterValue) {
  if (path[path.length - 1] === "/") path = path.substr(0, path.length - 1);
  const link =
    getApiUrl(path) +
    "?" +
    parameterName +
    "=" +
    encodeURIComponent(parameterValue);
  window.location.href = link;
}
function searchByUserId(id) {
  openLinkWithGETParameter(window.location.pathname, "id", id);
}
function handleSearch() {
  const inputValue = registrationInput.value.trim();
  if (inputValue !== "") {
    searchByUserId(inputValue);
  }
}

registrationInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    handleSearch();
  }
});
searchButton.addEventListener("click", handleSearch);
/* -------------------------------------------------------------------------- */
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("mainForm");
  const formElements = form.elements;

  // Get the search input element
  const searchInput = document.getElementById("registration_number");

  // Store the initial values of all form elements when the page loads
  const initialValues = {};
  for (let i = 0; i < formElements.length; i++) {
    const element = formElements[i];
    if (element.type !== "submit") {
      if (element.type === "radio" && !element.checked) {
        // For radio buttons, store the initial value of the checked option
        initialValues[element.name] = form.querySelector(
          `input[name="${element.name}"]:checked`
        ).value;
      } else if (element.type === "select-one") {
        // For select options, store the initial value of the selected option
        initialValues[element.name] = element.value;
      } else {
        initialValues[element.id] = element.value;
      }
    }
  }

  // Add change event listeners to all form elements
  form.addEventListener("change", function (event) {
    const element = event.target;

    // Check if the value of any form element has changed from its initial value
    let hasValueChanged = false;
    for (let i = 0; i < formElements.length; i++) {
      const currentElement = formElements[i];
      if (currentElement.type !== "submit") {
        if (currentElement.type === "radio") {
          // For radio buttons, check if the checked option value has changed
          if (
            currentElement.name === element.name &&
            currentElement.value !== initialValues[element.name] &&
            currentElement.checked
          ) {
            hasValueChanged = true;
            break;
          }
        } else if (currentElement.type === "select-one") {
          // For select options, check if the selected option value has changed
          if (
            currentElement.name === element.name &&
            currentElement.value !== initialValues[element.name]
          ) {
            hasValueChanged = true;
            break;
          }
        } else if (currentElement.value !== initialValues[currentElement.id]) {
          hasValueChanged = true;
          break;
        }
      }
    }

    // Disable the search input if any other form element value has changed
    searchInput.disabled = hasValueChanged;
  });
});

/* -------------------------------------------------------------------------- */
function main() {
  handleSchoolLevelChange();
  handleTalmzaLevelChange();
}
main();
