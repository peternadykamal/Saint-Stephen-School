const form = document.querySelector("form");
const inputs = form.querySelectorAll("input");

// Attach event listeners to each input
inputs.forEach((input, index) => {
  input.addEventListener("keydown", (event) => {
    const { key } = event;

    // Prevent input of space character
    if (key === " ") {
      event.preventDefault();
      return;
    }

    // If the user presses the space key, move to the next input element
    if (key === "Spacebar" || key === " " || key === "Space") {
      event.preventDefault();
      const nextIndex = index + 1;
      if (nextIndex < inputs.length) {
        inputs[nextIndex].focus();
      }
    }
  });
});

// document.addEventListener("DOMContentLoaded", function () {
//   const imageInput = document.getElementById("imageInput");
//   const imagePreview = document.getElementById("imagePreview");

//   imageInput.addEventListener("change", function () {
//     readURL(this);
//   });

//   function readURL(input) {
//     if (input.files && input.files[0]) {
//       const reader = new FileReader();

//       reader.onload = function (e) {
//         imagePreview.setAttribute("src", e.target.result);
//         imagePreview.style.display = "block";
//       };

//       reader.readAsDataURL(input.files[0]);
//     }
//   }
// });
