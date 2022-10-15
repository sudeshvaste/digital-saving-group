from django.contrib import admin
from .models import LoanIntrest, financel_year, Loan, Loan_Limit, financel_year
# Register your models here.
admin.site.register(LoanIntrest)
admin.site.register(financel_year)
admin.site.register(Loan)
admin.site.register(Loan_Limit)

