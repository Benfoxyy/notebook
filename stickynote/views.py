from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import NotesForm

def index_view(request):
    note=notes.objects.all()
    context={'note':note}
    return render(request,'sticky_them.html',context)

def form_view(request):
    if request.method=='POST':
        note=NotesForm(request.POST)
        if note.is_valid():
            note.save()
            return HttpResponseRedirect('/')
    form=NotesForm()
    return render(request,'save.html',{'form':form})
