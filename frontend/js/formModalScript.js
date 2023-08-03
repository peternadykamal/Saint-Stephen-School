// document
//   .getElementById("modalSubmitButton")
//   .addEventListener("click", function () {
//     const modalInputExpenses =
//       document.querySelector('[name="expenses"]').value;
//     document.querySelector("#amount_of_money_payed").value = modalInputExpenses;
//     document.getElementById("mainForm").submit();
//   });

// to make the modal appear on page load (for testing)
var myModal = new bootstrap.Modal(
  document.getElementById("confirmationModal"),
  {}
);
myModal.toggle();
