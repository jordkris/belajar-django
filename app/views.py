from django.shortcuts import render
from django.http import HttpResponse
from app.models import Customer
from app.forms import customerForm

def index(request):
    return HttpResponse("<b>Hello, world. You're at the polls index.</b>")

def text(request):
    output = '<b>This is a bold text.</b>'
    output += '<i>This is a italic text.</i>'
    output += '<u>This is a underlined text.</u>'
    output += '<p>This is a paragraph.</p>'
    return HttpResponse(output)


def temp(request):
    my_dict = {'my_name': "Jordy", 'my_age': "23"}
    return render(request, 'index.html', context=my_dict)


def customer(request):
    data = Customer.objects.all()
    customerDataDict = {'customerData': data}
    return render(request, 'customer.html', context=customerDataDict)


def customerFormView(request):
    form = customerForm()
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid:
            print('this is valid')
    return render(request, 'customer.html', context={'form': form})
