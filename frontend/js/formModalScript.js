document
  .getElementById("modalSubmitButton")
  .addEventListener("click", function () {
    const modalInput1Value = document.querySelector('[name="expenses"]').value;
    document.querySelector('[name="input1"]').value = modalInput1Value;
    document.getElementById("mainForm").submit();
  });

// to make the modal appear on page load (for testing)
// var myModal = new bootstrap.Modal(
//   document.getElementById("confirmationModal"),
//   {}
// );
// myModal.toggle();
