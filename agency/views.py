# agency/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import PortfolioProject
from .forms import LeadCaptureForm

def home(request):
    projects = PortfolioProject.objects.all()
    
    if request.method == 'POST':
        form = LeadCaptureForm(request.POST)
        if form.is_valid():
            # 1. Save the lead to the database
            form.save()
            
            # 2. Extract the submitted data
            name = form.cleaned_data.get('name', 'Unknown')
            email = form.cleaned_data.get('email', 'No Email')
            message = form.cleaned_data.get('message', '')
            
            # 3. Construct and send the email
            subject = f"New Lead from Powell Web Works: {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,         # Sends FROM your authenticated business email
                [settings.EMAIL_HOST_USER],       # Sends TO your business email
                fail_silently=False,              # Forces an error if it fails so we can see it in the logs
            )
            
            messages.success(request, "Thanks! I've received your information and will be in touch shortly.")
            return redirect('home')
    else:
        form = LeadCaptureForm()
        
    context = {
        'projects': projects,
        'form': form
    }
    return render(request, 'index.html', context)