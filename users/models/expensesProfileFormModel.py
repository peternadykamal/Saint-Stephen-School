from django.db import models

import uuid

from utils.get_env_value import get_env_value

from .profileModel import Profile


class ExpensesProfileForm(models.Model):
  year = models.CharField(max_length=4)
  amount_of_money_payed = models.IntegerField()
  created_for = models.ForeignKey(
      Profile, on_delete=models.SET_NULL, null=True, blank=False)

  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.year + " " + str(str(self.created_for) + " دفع " + str(self.amount_of_money_payed) + " جنيهات")

  # total number of Expenses (not as a proprty in the table but an constant stored in a spearte table or as .env file in backend)
  def getExpenses() -> int:
    return int(get_env_value("EXPENSES_PROFILE_FORM"))

  # -------------------------------- validation -------------------------------- #
  def validateAmountPayed(amount):
    expenses = ExpensesProfileForm.getExpenses()
    if amount == '':
      return False

    if amount.isdigit():
      amount = int(amount)
    else:
      return False

    if amount < 1 or amount > expenses:
      return False

    return True
