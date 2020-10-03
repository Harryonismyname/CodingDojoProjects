from __future__ import unicode_literals
from django.db import models
from datetime import date

class ShowManager(models.Manager):
    def basic_validator(self, postData, workingObject=None):
        errors = {}
        current_date = str(date.today())
        all_shows= Show.objects.all()
        if workingObject is not None:
            for shows in all_shows:
                if postData['Title'] == shows.title and postData['Title'] != workingObject.title:
                    errors['unique_title'] = "Title must be unique"
        if len(postData['Title']) < 2:
            errors['title'] = "Title must be greater than 2 characters long"
        if len(postData['Network']) < 3:
            errors['network'] = "Network must be greater than 3 characters long"
        if len(postData['Description'])< 10 and len(postData['Description']) > 0:
            errors['description'] = "Description must be at least 10 characters long or empty"
        if postData['Release Date'] > current_date or len(postData['Release Date']) == 0:
            errors['release_date'] = "Release date must be before today"
        return errors

# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    description=models.TextField(default="Some Text")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= ShowManager()