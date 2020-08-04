from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse



class Colors(models.Model):
    title = models.CharField(max_length=50)
    color_image = models.ImageField( default="red.jpg",upload_to='colors')

    def __str__(self):
        return f"{self.title}"
    


class Note(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    background_color = models.ForeignKey(Colors,default="null",on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("note-detail", kwargs={"pk": self.pk})
    



# Create your models here.
