from django.db import models
from django.contrib.auth.models import User

from categories.models import CategoryModel
# Create your models here.
class CarModel(models.Model):
    image = models.ImageField(upload_to='car/media/uploads/', blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    brand = models.ForeignKey(User, on_delete = models.CASCADE)
    detail = models.CharField(max_length=1000)
    category = models.ManyToManyField(CategoryModel)
    def __str__(self) -> str:
        return self.name
    

class CommentModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateField(auto_now_add = True)