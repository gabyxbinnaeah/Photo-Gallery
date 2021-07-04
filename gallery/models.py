from django.db import models

class Locations(models.Model):
    name=models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

# class Category(models.Model):
#     name=models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

# class Image(models.Model):
#     name=models.CharField(max_length=30)
#     description=models.TextField()
#     category=models.ForeignKey('Category',on_delete=CASCADE,blank=True)
#     location=models.ForeignKey('Location',on_delete=CASCADE,blank=True)
#     image=models.ImageField(upload_to='images/',blank=True)

