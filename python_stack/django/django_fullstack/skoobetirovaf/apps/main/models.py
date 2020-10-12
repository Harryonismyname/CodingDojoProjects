from django.db import models
from ..login.models import User
# Create your models here.
class Book_Validator(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title'])==0:
            errors['title'] = "You must enter a title"
        if len(postData['description'])<5:
            errors['desc']='The description must be at least 5 characters long'
        return errors

class Book(models.Model):
    objects = Book_Validator()
    title = models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    uploaded_by=models.ForeignKey(User, related_name="books_uploaded",on_delete=models.CASCADE)
    users_who_like=models.ManyToManyField(User, related_name='liked_books')
