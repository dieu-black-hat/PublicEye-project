from django.db import models
class CrimeReport(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('resolved', 'Resolved'),
        ('in_progress', 'In Progress'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    victims = models.CharField(max_length=255, blank=True)
    crime_type = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='crime_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open', null=True)  # Default to 'open'

    def __str__(self):
        return f"{self.crime_type} reported by {self.name}"
from django.utils import timezone

class Officer(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Unique username
    password = models.CharField(max_length=150)  # Password (should be hashed)
    name = models.CharField(max_length=150)  # Officer's full name
    email = models.EmailField(max_length=150, unique=True)  # Officer's email
    phone = models.CharField(max_length=20, blank=True, null=True)  # Optional phone number
    specialization = models.CharField(max_length=100, blank=True, null=True)  # Officer specialization
    created_at = models.DateTimeField(default=timezone.now)  # Account creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Last update timestamp

    def __str__(self):
        return self.username
from django.db import models
class MostWanted(models.Model):
    STATUS_CHOICES = [
        ('seen', 'Seen'),
        ('not_seen', 'Not Seen'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    crime_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='most_wanted_images/', blank=True)
    reward = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='not_seen')

    def __str__(self):
        return f"{self.name} - Wanted for {self.crime_type}"

    class Meta:
        verbose_name = 'Most Wanted'
        verbose_name_plural = 'Most Wanted'
        ordering = ['-created_at']
        # models.py
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"

class Comment(models.Model):
    REPORT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('resolved', 'Resolved'),
    ]

    report = models.ForeignKey(CrimeReport, related_name='comments', on_delete=models.CASCADE)
    officer_email = models.EmailField()  # Email of the intelligence officer
    comment_text = models.TextField()  # The content of the comment
    status = models.CharField(max_length=20, choices=REPORT_STATUS_CHOICES, default='pending')  # Status of the comment
    attachments = models.FileField(upload_to='comment_attachments/', blank=True, null=True)  # Attachments related to the comment
    evidence_collected = models.TextField(blank=True, null=True)  # Description of any evidence collected
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the comment was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the comment was last updated

    def __str__(self):
        return f"Comment by {self.officer_email} on {self.created_at}"

class Feedback(models.Model):
    report = models.ForeignKey(CrimeReport, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    latitude = models.FloatField(null=True, blank=True)  # Add this line
    longitude = models.FloatField(null=True, blank=True)  # Add this line

    def __str__(self):
        return f'Feedback for Report {self.report.id} - {self.subject}'