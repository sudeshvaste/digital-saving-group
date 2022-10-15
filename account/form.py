from cProfile import label
from dataclasses import field
from django.forms import ModelForm
from .models import Loan, Loan_installment, Bachat, Expenditure


class Loan_Application(ModelForm):
    class Meta:
        model = Loan
        fields = ['member', 'intrest_rate', 'loan_amount']


class Loan_installments(ModelForm):
    class Meta:
        model = Loan_installment
        fields = '__all__'


class BachatForm(ModelForm):
    class Meta:
        model = Bachat
        fields = ['member', 'year', 'month', 'bachat_amount', 'late_fee']


class Aut_Loan_installments(ModelForm):
    class Meta:
        model = Loan_installment
        fields = ['loan', 'year', 'month',
                  'loan_amount', 'intrest_on_loan', 'late_fee']


class ExpenditureForm(ModelForm):
    class Meta:
        model = Expenditure
        fields = '__all__'
