
from django.shortcuts import render,redirect
import datetime
import math
from .models import *
from .forms import *

def add(request):

    return render(request,"index.html")
# Create your views here.


def fight(request):
    d=""
    if request.method == 'POST':
        a = request.POST.get('first')
        b = request.POST.get('second')
        c = int(a)+int(b)
        d= "SUM ="+str(c)
    return render(request, "hai.html", {'sum': d})

def factt(request):
    c=""
    if request.method =="POST":
        a= request.POST.get('num')
        b= math.factorial(int(a))
        c="FACT ="+str(b)
    return render(request, "factorial.html", {'fact': c})


def ins(request):
    msg = ""
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('addr')
        c = request.POST.get('age')
        d = request.POST.get('course')
        abc = Student(name=a,  address=b, age=c, course=d)
        abc.save()
        msg = "Data inserted successfully"
    return render(request, "insert.html", {'msg': msg})

def list(request):
    obj = Student.objects.all()
    return render(request, "list.html", {'obj': obj})

def delete(request, id):
    obj = Student.objects.get(id=id)
    obj.delete()
    return redirect(list)


def test_form(request):
    abc = Test_form(request.POST)
    if request.method == "POST":
        if abc.is_valid():
            abc.save()
            return redirect(list)
    return render(request, "form.html", {'form': abc})


def edit(request, id):
    xyz = Student.objects.get(id=id)
    abc = Test_form(request.POST or None, instance=xyz)
    if request.method == "POST":
        if abc.is_valid():
            abc.save()
            return redirect(list)
    return render(request, "form.html", {'form': abc})