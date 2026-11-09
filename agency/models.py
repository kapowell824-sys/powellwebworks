from django.db import models

class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    client_type = models.CharField(max_length=100) 
    description = models.TextField()
    tech_stack = models.CharField(max_length=255) 
    image_url = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Lead(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New Inbound Lead'),
        ('CALLED', 'Cold Called - Left Message'),
        ('PITCHED', 'Pitched - Awaiting Answer'),
        ('WON', 'Closed - Deposit Paid'),
        ('LOST', 'Closed - Not Interested'),
    ]
    
    business_name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    current_website = models.URLField(blank=True)
    pain_points = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business_name} - {self.status}"