from audioop import avg
import math
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from commitee.decorators import allowed_users
from .form import Loan_Application, Loan_installment, Loan_installments, ExpenditureForm
from .models import Loan, Expenditure
from django.contrib import messages
# Create your views here.


@allowed_users(allowed_roles=['Member'])
def loan(request):
    fm = Loan_Application
    loan = Loan.objects.all().order_by("-id")
    member = request.GET.get("member_name")
    loan1 = Loan.objects.all().order_by("-id")

    secretary = request.user.groups.filter(name='Secretary')
    president = request.user.groups.filter(name='Precedent')
    accountant = request.user.groups.filter(name='Accountant')

    if secretary:
        loan = Loan.objects.filter(status_secretary='Pending').order_by("-id")

    if president:
        loan = Loan.objects.filter(
            status_secretary='Approved', status_president='Pending').order_by("-id")

    if accountant:
        loan = Loan.objects.filter(
            status_president='Approved', status_accountant='Pending').order_by("-id")

    if member != "" and member is not None:
        loan = Loan.objects.filter(member=member)

    context = {
        'form': fm,
        'loans': loan,
        'secretary': secretary,
        'president': president,
        'accountant': accountant,
        'loan1': loan1,
    }

    if request.method == 'POST':
        loan_amount = request.POST['loan_amount']
#        loan_limit =
        fm = Loan_Application(request.POST)
    #    if loan_amount>
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Loan application Sucessfully')
            return HttpResponseRedirect('/loan',)
    return render(request, 'account/loan.html', context)


@allowed_users(allowed_roles=['Member'])
def approve(request, id, Authority):
    loan = Loan.objects.filter(pk=id)
    loan_re = Loan_installment.objects.filter(pk=id)
    authority = str(Authority)
    if authority == 'secretary':
        loan.update(status_secretary="Approved")
    if authority == 'president':
        loan.update(status_president="Approved")
    if authority == 'accountant':
        loan.update(status_accountant="Approved")
        loan.update(approve="Active")
    if authority == 'Accountant':
        loan_re.update(status_accountant="Approved")
    messages.success(request, 'Loan is Approved')
    return redirect('loan')


@allowed_users(allowed_roles=['Member'])
def decline(request, id, Authority):
    loan = Loan.objects.filter(pk=id)
    loan_re = Loan_installment.objects.filter(pk=id)
    authority = str(Authority)
    if authority == 'secretary':
        loan.update(status_secretary="Declined")
    if authority == 'president':
        loan.update(status_president="Declined")
    if authority == 'accountant':
        loan.update(status_accountant="Declined")
    if authority == 'accountant':
        loan_re.update(status_accountant="Declined")
        messages.success(request, 'Loan is Declined')
    return redirect('loan')


@allowed_users(allowed_roles=['Member'])
def loan_details(request, id):
    loan = Loan.objects.get(pk=id)
    loan_installment = Loan_installment.objects.all()
    accountant = request.user.groups.filter(name='Accountant')
    fm = None

    if loan.approve == "Applied":
        messages.warning(request, 'Your Loan is not approved')
        return redirect('dashbord')

    if loan.approve == "Active":
        fm = Loan_installments()

#    if accountant and loan.approve == "Active":
#        fm = Aut_Loan_installments()

    context = {
        'loan': loan,
        'loan_installment': loan_installment,
        'form': fm,
        'Accountant': accountant,
    }

    if request.method == 'POST':
        fm = Loan_installments(request.POST)
        if fm.is_valid():
            fm.loan_id = id
            fm.save()
            messages.success(request, 'Request submitted successfully')
            return redirect('dashbord')
    return render(request, 'member/loan_details.html', context)

@allowed_users(allowed_roles=['Member'])
def overview(request):
    fm = ExpenditureForm()
    accountant = request.user.groups.filter(name='Accountant')
    expenditure = Expenditure.objects.all()
    loans = Loan.objects.filter(approve="Active")
    Total = Loan.objects.filter(approve="Active").aggregate(Sum('loan_amount')).get('loan_amount__sum')
    Total2 = Expenditure.objects.aggregate(Sum('amount')).get('amount__sum')
    context = {
        'form1': fm,
        'accountant': accountant,
        'expenditure': expenditure,
        'loan' : loans,
        'Total' : Total,
        'Total2': Total2,
    }
    return render(request, 'account/overview.html', context)

@allowed_users(allowed_roles=['Member','Accountant'])
def expenditures(request):
    if request.method == 'POST':
        fm1 = ExpenditureForm(request.POST)
        if fm1.is_valid():
            fm1.save()
            messages.success(request, 'Data Saved successfully')
    return HttpResponseRedirect('/overview')

@allowed_users(allowed_roles=['Member','Accountant'])
def delete_exp(request, id):
    d = Expenditure.objects.get(pk=id)
    d.delete()
    messages.success(request,'Expenditure deleted')
    return HttpResponseRedirect('/overview')
