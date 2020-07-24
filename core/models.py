from django.db import models

# Create your models here.
class Breed(models.Model):
    breed_name = models.CharField(max_length=255)

class Dog(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='dogs', blank=True, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    def __str__(self):
        return self.name