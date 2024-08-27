from django.shortcuts import render
from .import forms
# from .forms import Form
# Create your views here.
def home(request):
    name = request.POST.get('UserName')
    roll_number = request.POST.get('roll')
    birth_date = request.POST.get('birthday')
    comment = request.POST.get('comment')
    email  = request.POST.get('email')
    agree = request.POST.get('agree')
    height = request.POST.get('height')
    return render(request,'home.html',{'name' : name, 'roll' : roll_number, 'bithday' : birth_date, 'comment' : comment, 'email' : email ,'agree' : agree, 'height' : height})
