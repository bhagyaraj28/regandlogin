from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Reg
from .forms import LoginForm
from .forms import RegForm


def home(request):
    return render(request, 'home.html')


def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return HttpResponse("reg sucess")
        else:
            print(form.error)
            return HttpResponse("error")
    else:
        form = RegForm()
        return render(request, 'reg.html', {'form': form})


def login(request):
    if request.method == 'POST':
        myloginform = LoginForm(request.POST)
        if myloginform.is_valid():
            un = myloginform.cleaned_data['user']
            pw = myloginform.cleaned_data['pwd']
            dbuser = Reg.objects.filter(user=un, pwd=pw)
            if not dbuser:
                return HttpResponse('login failed')
            else:
                return HttpResponse('login sucess')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
