from django.db import models

# Create your models here.
<<<<<<< HEAD


=======
>>>>>>> a68599ac6d5c74b2bd06751bea7c7c1e459d42f8
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
<<<<<<< HEAD
        return self.name
=======
        return self.name
>>>>>>> a68599ac6d5c74b2bd06751bea7c7c1e459d42f8
