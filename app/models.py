from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=500)
	address = models.CharField(max_length=500)
	description = models.TextField()
	date = models.DateTimeField(default=datetime.now())
	created_at = models.DateTimeField(default=datetime.now())