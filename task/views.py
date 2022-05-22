from asyncio import tasks
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import * 
from .form import * 
# Create your views here.
def index(request):
    tasks = Schedule.objects.all()
    forms = Scheduleform()

    if request.method == "POST" :
        forms = Scheduleform(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect("/")


    context = {'tasks': tasks , 'forms':forms} 


    return render(request,'list.html',context)


def updateTask(request, pk):
    item = Schedule.objects.get(id=pk)

    forms = Scheduleform(instance=item)

    if request.method == 'POST':
        forms = Scheduleform(request.POST, instance=item)
        if forms.is_valid():
            forms.save()
            return redirect('/')


    context = {'forms': forms}

    return render(request , 'update_task.html',context)


def deleteTask(request ,pk):
    items = Schedule.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect("/")

    context = {'items' : items}
    return render(request, 'delete.html',context)
