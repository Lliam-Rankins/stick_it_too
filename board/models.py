from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Board")

class Note(models.Model):
    is_image = models.BooleanField(default=False)

    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Note")

    # image = models.ImageField()