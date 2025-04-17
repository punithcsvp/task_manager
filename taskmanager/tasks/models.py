from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)  # New field for Due Date

    def __str__(self):
        return self.title

    def is_due_soon(self):
        """Checks if the task is due in the next 24 hours."""
        if self.due_date:
            return self.due_date - timedelta(hours=24) <= timezone.now() <= self.due_date
        return False

    def is_overdue(self):
        """Checks if the task's due date has passed."""
        if self.due_date:
            return timezone.now() > self.due_date
        return False

    def clean(self):
        """Ensure that the due date is not in the past."""
        if self.due_date and self.due_date < timezone.now():
            raise ValidationError('Due date cannot be in the past.')

# Add the Notification model here
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"
