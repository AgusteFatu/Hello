from cProfile import label
from statistics import StatisticsError, mean, median, mode, stdev, variance, pstdev
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from matplotlib.pyplot import title
from numpy import number


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

class twoNumberForm(forms.Form):
    number1 = forms.FloatField(label="Enter Number 1")
    number2 = forms.FloatField(label="Enter Number 2",)

class Stats(forms.Form):
    numbers = forms.CharField(
        label='',
        widget = forms.widgets.Textarea(attrs={'cols': '80', 'rows': '3'}))

# Create your views here.

alper = ['alper']

def index(request):
    return render(request, "lecture3/index.html")

def tasks(request):
    if "tasks5" not in request.session:
        request.session["tasks5"] = []
    return render(request, "lecture3/tasks.html" ,{
        "task1": request.session["tasks5"],
        "name" : alper
    }) # "tasks" is the variable html can access

def add(request):
    if request.method == "POST": # Check if the request method is POST
        form = NewTaskForm(request.POST) # Figure it out all the data they submitted save inside form variable
        if form.is_valid(): # Check if the data is right format
            task = form.cleaned_data["task"] # "task" which is inside the class task
            request.session["tasks5"] += [task]
            return HttpResponseRedirect(reverse("lecture3:tasks"))
            
        else: # If not render the same html page with same form data
            return render(request,"lecture3/add.html", {
                "form": form
        })

    return render(request,"lecture3/add.html", { # if the method is not POST return empty form
        "form": NewTaskForm() 
    })

def greet(request,name):
     return render(request, "lecture3/greet.html", {
         "name": name.capitalize()
     }) # giving this template additional information 'name' so I can use name inside the greet.html 

def newyear(request):
    now = datetime.now()
    return render(request,"lecture3/newyear.html", {
        "newyear" : now.month == 1 and now.day == 1
    })

def base(request):
    return render(request,"lecture3/base.html")

# ---

def stats_(request):
    if request.method == "POST":
        form = Stats(request.POST)
        if form.is_valid():
            numbers = form.cleaned_data["numbers"]
            numbersClean = list(map(float,numbers.split()))
            try:
                var = f"{variance(numbersClean):.3f}"
            except StatisticsError as e:
                var = e
            try:
                sd =  f"{stdev(numbersClean):.3f}"
            except StatisticsError as e:
                sd = e

            return render(request,"lecture3/statistics.html",{
                "form" : form,
                "numbers" : numbersClean,
                "n" : len(numbersClean),
                "sum"  : f"{sum(numbersClean):.3f}",
                "mean" : f"{mean(numbersClean):.3f}",
                "median" : f"{ median(numbersClean)}",
                "mode" : f"{mode(numbersClean)}",
                "var" : var,
                "sd" :  sd
            })
        else:
            return render(request,"lecture3/statistics.html",{
                "form" : form
            })
            
    return render(request,"lecture3/statistics.html",{
        "form" : Stats()
    })

def sumO(request):
    if request.method == "POST":
        form = twoNumberForm(request.POST)
        if form.is_valid():
            number1  = form.cleaned_data["number1"]
            number2  = form.cleaned_data["number2"]
            try:
                div = number1 / number2
            except ZeroDivisionError:
                div = "Zero Division!"
            return render(request,"lecture3/sum.html",{
                'form' : form,
                'sum' : number1 + number2,
                'sub' : number1 - number2,
                'mul' : number1 * number2,
                'div' : div
            })
        else:
            return render(request,"lecture3/add.html", {
                "form": form
            })
    return render(request,"lecture3/sum.html",{
        "form": twoNumberForm()
    })
# -----------------------------------

# def alper(request):
#     return HttpResponse('Hello, Brian!333')

# def david(request):
#     return HttpResponse("Hello, David!")

# def greet(request,name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")