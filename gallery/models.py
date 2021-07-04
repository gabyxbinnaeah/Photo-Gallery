from django.db import models

class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save() 

    def delete_location(self):
        Location.objects.filter(id=self.id).delete()

    def update_location(self):
        self.objects.filter(id = self.id).update()  


    

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()  

    def delete_category(self):
        Category.objects.filter(id=self.id).delete()


class Image(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to = 'album/',blank=True,null=True)
    

    def __str__(self):
        return self.name

    def save_images(self):
        self.save()

    def delete_image(self):
        Image.objects.filter(id=self.id).delete()

    @classmethod
    def found_images(cls):
        images_list=cls.objects.all()
        return images_list  

    @classmethod
    def search_by_category(cls,search_term):
        searched_image=cls.objects.filter(category=search_term)
        return searched_image     








    


