# agency/admin.py
from django.contrib import admin
from .models import PortfolioProject, Lead

admin.site.register(PortfolioProject)
admin.site.register(Lead)