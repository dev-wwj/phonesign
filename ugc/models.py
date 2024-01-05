from django.db import models
from user.models import CustomUser
from ckeditor.fields import RichTextField
# Create your models here.


class Coordinates(models.Model):
    latitude = models.FloatField()  #纬度
    longitude = models.FloatField()  #经度

    def __str__(self):
        return "(" + str(self.latitude) + "," + str(self.longitude) + ")"


class Location(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} : {self.name}{self.coordinates}"


class UGCPost(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(UGCPost, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def can_delete(self, user):
        return user == self.author
