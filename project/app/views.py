from django.shortcuts import render, redirect
from .models import Credit
from .forms import Credit_Form
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView


# Create your views here.

def signup(request):
    regi_form = UserCreationForm()
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect ('home')

    return render(request, 'signup.html', {'regi_form':regi_form})

class MyLoginView(LoginView):
    template_name = 'login.html'


def home(request):
    credits = Credit.objects.all()
    return render(request, 'home.html', {'credit':credits,})

def create(request):
    credit_form = Credit_Form
    if request.method == "POST":
        filled_form = credit_form(request.POST)
        if filled_form.is_valid():
            temp_from = filled_form.save(commit=False)
            temp_from.author = request.user
            temp_from.save()
            return redirect('home')
    return render(request, 'create.html', {'credit_form':credit_form})

def detail(request, credit_id):
    try:
        my_credit = Credit.objects.get(pk=credit_id)
    except:
        raise Http404
    
    return render(request, 'detail.html', {'my_credit':my_credit})

def delete(request, credit_id):
    my_credit = Credit.objects.get(pk=credit_id)
    if request.user == my_credit.author:
        my_credit.delete()
        return redirect('home')

    raise PermissionDenied

def update(request, credit_id):
    my_credit = Credit.objects.get(pk=credit_id)
    credit_form = Credit_Form(instance=my_credit)
    if request.method == "POST":
        updated_form = Credit_Form(request.POST, instance=my_credit)
        if updated_form.is_valid():
            updated_form.save()
            return redirect ('home')
    return render(request, 'create.html', {'credit_form':credit_form})