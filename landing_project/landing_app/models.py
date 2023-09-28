from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=200,verbose_name='User ismi')
    email=models.EmailField(max_length=100)
    number=models.CharField(max_length=50)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Foydalanuvchi"
