from django.db import models

# Create your models here.
class CourseValidator(models.Manager):
    def new_course_validator(self, postData):
        errors = {}
        if len(postData['name'])<5:
            errors['name'] = 'Name must be at least 5 characters long'
        if len(postData['description'])<15:
            errors['description'] = 'Description must be at least 15 characters long'
        return errors

class Course(models.Model):
    name=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseValidator()

class Description(models.Model):
    desc = models.TextField(default='')
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)