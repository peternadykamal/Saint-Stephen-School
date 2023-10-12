/* -------------------------------------------------------------------------- */
/* -- following code is related to the input fields in the attendance page -- */
/* -------------------------------------------------------------------------- */

import * as utils from "./utils.js";
// Load the mapping data from the data-container element
const dataContainer = document.getElementById("data-container");
const mappingData = JSON.parse(dataContainer.getAttribute("data-mapping"));

// Access form element IDs from the mapping data
const usernameFieldId = mappingData["username"];
const attendanceDateFieldId = mappingData["attendance_date"];
const attendanceTypeFieldId = mappingData["attendance_type"];
const statusFieldId = mappingData["status"];

// Get the corresponding form elements
const usernameField = document.getElementById(usernameFieldId);
const attendanceDateField = document.getElementById(attendanceDateFieldId);
const attendanceTypeField = document.getElementById(attendanceTypeFieldId);
const statusField = document.getElementById(statusFieldId);

// Add event listeners and perform actions on form elements
function toggleVisibilityOfStatusField(e) {
  if (e.target.value === "liturgy") {
    utils.elementVisibility(false, `#${statusFieldId}_field`);
  } else {
    utils.elementVisibility(true, `#${statusFieldId}_field`);
  }
}

attendanceTypeField.addEventListener("change", toggleVisibilityOfStatusField);

// Function to save the selected option to local storage
function saveSelectedOption() {
  // Save attendance type to local storage
  const selectedAttendanceType = attendanceTypeField.value;
  localStorage.setItem("selectedAttendanceType", selectedAttendanceType);

  // Save status to local storage
  const selectedStatus = statusField.value;
  localStorage.setItem("selectedStatus", selectedStatus);
}

function loadSelectedOptions() {
  // Load the selected option from local storage for attendance type
  const selectedAttendanceType = localStorage.getItem("selectedAttendanceType");
  if (selectedAttendanceType) {
    attendanceTypeField.value = selectedAttendanceType;
  }

  // Load the selected option from local storage for status
  const selectedStatus = localStorage.getItem("selectedStatus");
  if (selectedStatus) {
    statusField.value = selectedStatus;
  }
}

document
  .getElementById("submitButton")
  .addEventListener("click", saveSelectedOption);

// When the page loads
document.addEventListener("DOMContentLoaded", function () {
  // Load selected options from local storage
  loadSelectedOptions();

  // Check if the attendance type is liturgy, if so, hide the status field
  if (attendanceTypeField.value === "liturgy") {
    utils.elementVisibility(false, `#${statusFieldId}_field`);
    console.log("Hide status field");
  } else {
    console.log("Show status field");
    utils.elementVisibility(true, `#${statusFieldId}_field`);
  }

  // Focus on the username field
  usernameField.focus();
});

/* -------------------------------------------------------------------------- */
/* ------- the following code is for the clock in the attendance page ------- */
/* -------------------------------------------------------------------------- */
let isClockEditable = false;
let clockInterval;

function toggleClockEditability() {
  const editableDivs = document.querySelectorAll(".editable-span");
  const playPauseButton = document.getElementById("playPauseButton");
  isClockEditable = !isClockEditable;

  if (isClockEditable) {
    editableDivs.forEach((div) => {
      div.contentEditable = "true";
    });
    clearInterval(clockInterval);
    // change icon class (icon element is the only child of the button)
    playPauseButton.firstElementChild.classList.remove("bi-pause-btn");
    playPauseButton.firstElementChild.classList.add("bi-play-btn");
  } else {
    editableDivs.forEach((div) => {
      div.contentEditable = "false";
    });
    updateClockValues();
    clockInterval = setInterval(updateClockValues, 1000);
    // change icon class (icon element is the only child of the button)
    playPauseButton.firstElementChild.classList.remove("bi-play-btn");
    playPauseButton.firstElementChild.classList.add("bi-pause-btn");
  }
}

function updateClockValues() {
  const now = new Date();
  var hours = now.getHours();
  const minutes = now.getMinutes();
  const seconds = now.getSeconds();
  const ampm = hours < 12 ? "AM" : "PM";

  if (hours > 12) {
    hours -= 12;
  } else if (hours === 0) {
    hours = 12;
  }

  document.getElementById("hours").textContent = String(hours).padStart(2, "0");
  document.getElementById("minutes").textContent = String(minutes).padStart(
    2,
    "0"
  );
  document.getElementById("seconds").textContent = String(seconds).padStart(
    2,
    "0"
  );
  document.getElementById("ampm").textContent = ampm;
}
function handleTimeInput(event, elementId) {
  const otherKeys =
    event.key !== "Backspace" &&
    event.key !== "ArrowLeft" &&
    event.key !== "ArrowRight";
  if (!/^[0-9]$/.test(event.key) && otherKeys) {
    event.preventDefault();
  }

  const element = document.getElementById(elementId);
  if (element.textContent.trim().length >= 2 && otherKeys) {
    event.preventDefault();
  }
}

function handleAmPmInput(event) {
  const element = document.getElementById("ampm");
  if (
    event.key === "ArrowLeft" ||
    event.key === "ArrowRight" ||
    event.key === "ArrowUp" ||
    event.key === "ArrowDown"
  ) {
    var textContent = element.textContent.trim();
    if (textContent === "AM") {
      element.textContent = "PM";
    } else {
      element.textContent = "AM";
    }
  } else {
    event.preventDefault();
  }
}

function parseAndSetDateTime(event) {
  class InvalidTimeFormatError extends Error {
    constructor() {
      super();
      this.name = "InvalidTimeFormatError";
      this.message = "الرجاء إدخال الوقت بالصيغة الصحيحة";
    }
  }

  try {
    const hours = parseInt(document.getElementById("hours").textContent);
    const minutes = parseInt(document.getElementById("minutes").textContent);
    const seconds = parseInt(document.getElementById("seconds").textContent);
    const ampm = document.getElementById("ampm").textContent;

    if (!isNaN(hours) && !isNaN(minutes) && !isNaN(seconds)) {
      const now = new Date();
      const year = now.getFullYear();
      const month = now.getMonth() + 1; // Months are 0-based
      const day = now.getDate();

      let formattedHours = hours;

      if (ampm === "PM" && hours !== 12) {
        formattedHours += 12; // Add 12 hours for PM, except when it's 12 PM
      } else if (ampm === "AM" && hours === 12) {
        formattedHours = 0; // Convert 12 AM to 0 hours
      }

      const timeString = `${year}-${month.toString().padStart(2, "0")}-${day
        .toString()
        .padStart(2, "0")}T${formattedHours
        .toString()
        .padStart(2, "0")}:${minutes.toString().padStart(2, "0")}:${seconds
        .toString()
        .padStart(2, "0")}`;

      const parsedDate = new Date(timeString); // Throws an error if the time is invalid
      if (isNaN(parsedDate.getTime())) {
        throw new InvalidTimeFormatError();
      }
      // set the value of the element which is an input element with type datetime-local
      document.querySelector('input[type="datetime-local"]').value = timeString;
    } else {
      throw new InvalidTimeFormatError();
    }
  } catch (error) {
    // select div with id="attendance_date_error"
    const errorDiv = document.getElementById("attendance_date_error");
    errorDiv.textContent = error.message;
    event.preventDefault();
  }
}

// Function to save the clock state (editable or not) and value to local storage
function saveClockState() {
  localStorage.setItem("isClockEditable", isClockEditable);
  localStorage.setItem(
    "clockHours",
    document.getElementById("hours").textContent
  );
  localStorage.setItem(
    "clockMinutes",
    document.getElementById("minutes").textContent
  );
  localStorage.setItem(
    "clockSeconds",
    document.getElementById("seconds").textContent
  );
  localStorage.setItem(
    "clockAmPm",
    document.getElementById("ampm").textContent
  );
}

// Function to load the clock state (editable or not) and value from local storage
function loadClockState() {
  const savedEditable = localStorage.getItem("isClockEditable") || "false";
  if (savedEditable === "true") {
    // the clock state is false by default, so we need to toggle it
    toggleClockEditability();
    // Load the clock values from local storage
    document.getElementById("hours").textContent =
      localStorage.getItem("clockHours") || "12";
    document.getElementById("minutes").textContent =
      localStorage.getItem("clockMinutes") || "00";
    document.getElementById("seconds").textContent =
      localStorage.getItem("clockSeconds") || "00";
    document.getElementById("ampm").textContent =
      localStorage.getItem("clockAmPm") || "AM";
  }
}

// when the page is loaded
document.addEventListener("DOMContentLoaded", function () {
  // Event listener for the "Toggle Editable" button
  document
    .getElementById("playPauseButton")
    .addEventListener("click", toggleClockEditability);

  // Event listeners for the editable-span elements
  const editableDivs = document.querySelectorAll(".editable-span");
  editableDivs.forEach((div) => {
    div.addEventListener("keydown", (event) => handleTimeInput(event, div.id));
  });

  // Event listener for the "AM/PM" span
  document.getElementById("ampm").addEventListener("keydown", handleAmPmInput);

  // Event listener for the "Set Date and Time" button
  document
    .getElementById("submitButton")
    .addEventListener("click", function () {
      parseAndSetDateTime();
      saveClockState();
    });

  // Initialize the clock and start updating
  updateClockValues();
  clockInterval = setInterval(updateClockValues, 1000);
  loadClockState();
});
