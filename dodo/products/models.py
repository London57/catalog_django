from django.db import models
from django.core.validators import MinValueValidator



class Rubric(models.Model):
    name = models.CharField(
        max_length=20, 
        blank = False,
    )
    
class Product(models.Model):
    name = models.CharField(
        max_length=20, 
        blank = False,
    )
    description = models.CharField(
        max_length =50,
        blank=False,
    )
    price = models.FloatField(
        validators=[MinValueValidator(0)],
        blank=False
    )
    rubric = models.ForeignKey(
        'Rubric',
        on_delete=models.PROTECT,
        blank=False,
          
    )
    image = models.ImageField(
        upload_to='avatar/',
        blank=True
    )

