from django.db import models

class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        '''
        method that saves location
        '''
        self.save() 

    def delete_location(self):
        '''
        method that deletes location
        '''
        Location.objects.filter(id=self.id).delete()

    @classmethod
    def update_location(cls,id,name):
        '''
        method that updates location 
        '''

        return cls.objects.filter(id=id).update(name=name)


    

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        '''
        method that saves category
        '''
        self.save()  

    def delete_category(self):
        '''
        method that deletes category
        '''
        Category.objects.filter(id=self.id).delete()
    @classmethod
    def update_category(cls,id,new):
        '''
        method that updates category
        '''
        return cls.objects.filter(id=id).update(new=new)



class Image(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to ='images/',null=True)
    

    def __str__(self):
        return self.name

    def save_images(self):
        '''
        method that saves images
        '''
        self.save()

    def delete_image(self):
        '''
        method that deletes images
        '''
        Image.objects.filter(id=self.id).delete()

    @classmethod
    def found_images(cls):
        '''
        method that queries and return all image Properties
        '''
        images_list=cls.objects.all()
        return images_list  

    @classmethod
    def search_by_category(cls,search_term):
        '''
        method that  searches and return image by category
        '''
        searched_category=cls.objects.filter(category__name__icontains=search_term)
        return searched_category   

    @classmethod
    def search_by_location(cls,search_term):
        '''
        method that  searches and return image by location
        '''
        searched_location=cls.objects.filter(location__name__icontains=search_term)
        return  searched_location
         


       





    


