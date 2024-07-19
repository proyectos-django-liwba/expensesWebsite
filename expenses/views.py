from django.shortcuts import render

def index(request):
    return render(request, 'expenses/index.html', {'title': 'Home'})

def add_expenses(request):
    return render(request, 'expenses/add-expenses.html', {'title': 'Add Expenses'})
