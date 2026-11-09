# agency/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PortfolioProject
from .forms import LeadCaptureForm

def home(request):
    projects = PortfolioProject.objects.all()
    
    if request.method == 'POST':
        form = LeadCaptureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! I've received your information and will be in touch shortly.")
            return redirect('home')
    else:
        form = LeadCaptureForm()
        
    context = {
        'projects': projects,
        'form': form
    }
    return render(request, 'index.html', context)