from django.db import models

class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save() 

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()  

class Image(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,null=True)
    

    def __str__(self):
        return self.name

