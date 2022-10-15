

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LoanIntrest(models.Model):
    intrest_rate = models.PositiveIntegerField(null=True, blank=True)
    Tag = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.Tag


class Loan_Limit(models.Model):
    loan_limit = models.PositiveIntegerField(null=True, blank=True)
    Tag = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.Tag


class financel_year(models.Model):
    financel_year = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.financel_year


Action = (
    ("Pending", "Pending"), ("Approved", "Approved"), ("Declined", "Declined"),
)

Status = (
    ("Applied", "Applied"), ("Active", "Active"), ("Closed", "Closed")
)


class Loan(models.Model):
    member = models.ForeignKey(User, on_delete=models.PROTECT)
    intrest_rate = models.ForeignKey(LoanIntrest, on_delete=models.PROTECT)
    loan_amount = models.PositiveIntegerField(null=True, blank=True)
    application_Date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status_secretary = models.CharField(
        max_length=10, choices=Action, default="Pending", null=True, blank=True)
    status_president = models.CharField(
        max_length=10, choices=Action, default="Pending", null=True, blank=True)
    status_accountant = models.CharField(
        max_length=10, choices=Action, default="Pending", null=True, blank=True)
    approve = models.CharField(
        max_length=10, choices=Status, default="Applied", null=True, blank=True)

    def __str__(self):
        return self.member.username


Years = (
    ("2021 ", "2021"), ("2022", "2022"), ("2023", "2023"), ("2024", "2024"), ("2025", "2025"), ("2026", "2026"), ("2027", "2027"), ("2028", "2028"), ("2029", "2029"), ("2030","2030"), ("2031", "2031"), ("2032", "2032"), ("2033", "2033"), ("2034", "2034"), ("2035", "2035"), ("2036", "2036"), ("2037", "2037"), ("2038", "2038"), ("2039", "2039"), ("2040", "2040")
)

Months = (
    ("January", "January"), ("February", "February"), ("March", "March"), ("April", "April"), ("May", "May"), ("June", "June"), ("July","July"), ("August", "August"), ("September", "September"), ("October", "October"), ("November", "November"), ("December", "December"),
)


class Loan_installment(models.Model):
    loan = models.OneToOneField(Loan, on_delete=models.PROTECT)
    year = models.CharField(
        max_length=10, choices=Years, null=True, blank=True)
    month = models.CharField(
        max_length=10, choices=Months, null=True, blank=True)
    installment_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    loan_amount = models.PositiveIntegerField(null=True, blank=True)
    intrest_on_loan = models.PositiveIntegerField(null=True, blank=True)
    late_fee = models.PositiveIntegerField(null=True, blank=True)
    status_accountant = models.CharField(
        max_length=10, choices=Action, default="Pending", null=True, blank=True)

    def __str__(self):
        return self.loan


class Bachat(models.Model):
    member = models.ForeignKey(User, on_delete=models.PROTECT)
    year = models.CharField(
        max_length=10, choices=Years, null=True, blank=True)
    month = models.CharField(
        max_length=10, choices=Months, null=True, blank=True)
    installment_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    bachat_amount = models.PositiveIntegerField(null=True, blank=True)
#    intrest_on_loan = models.PositiveIntegerField(null=True, blank=True)
    late_fee = models.PositiveIntegerField(null=True, blank=True)
    status_accountant = models.CharField(
        max_length=10, choices=Action, default="Pending", null=True, blank=True)

    def __str__(self):
        return self.member.username


class Expenditure(models.Model):
    type = models.CharField(max_length=25, null=False, blank=False)
    amount = models.PositiveIntegerField(
        max_length=25, null=False, blank=False)
