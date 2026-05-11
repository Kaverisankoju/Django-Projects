from django.db import models
from accounts.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20, default='Applied')

    def __str__(self):
        return self.user.username
# Create your models here.
