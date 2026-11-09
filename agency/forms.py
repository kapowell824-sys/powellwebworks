# agency/forms.py
from django import forms
from .models import Lead

class LeadCaptureForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['business_name', 'contact_name', 'phone', 'email', 'current_website', 'pain_points']