from django.shortcuts import render, redirect
from .forms import LawsuitForm
from .models import Accident


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = LawsuitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results')
    else:
        form = LawsuitForm()
    return render(request, 'testapp/index.html', {'form': form})

def results(request):
    accidents = Accident.objects.all()
    return render(request, 'testapp/results.html', {'accidents': accidents})



