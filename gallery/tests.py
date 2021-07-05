from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.bondo = Location(name = 'bondo')

    def test_instance(self):
        self.assertTrue(isinstance(self.bondo, Location))

    def test_save_location(self):
        self.bondo.save_location()
        searched_locations = Location.objects.all()
        self.assertTrue(len(searched_locations ) >0) 

    def test_delete_location(self):
        self.bondo.save_location()
        self.bondo.delete_location()
        found_location=Location.objects.all()
        self.assertTrue(len(found_location)==0) 

    def test_update_location(self):
        self.bondo.save_location()
        self.bondo.update_location(self.bondo.id,'Nairobi')
        location_list=Location.objects.all()
        self.assertTrue(len(location_list)==1)
        updated_object=Location.objects.all().first()
        self.assertTrue(updated_object.name=='Nairobi')



class CategoryTestClass(TestCase):
    def setUp(self):
        self.large = Category(name = 'large')

    def test_instance(self):
        self.assertTrue(isinstance(self.large, Category))  

    def test_save_category(self):
        self.large.save_category()
        searched_category = Category.objects.all()
        self.assertTrue(len(searched_category  ) >0) 

    def test_delete_category(self):
        self.large.save_category()
        self.large.delete_category()
        found_category=Category.objects.all()
        self.assertTrue(len(found_category)==0)

    def test_update_category(self):
        self.large.save_category()
        self.large.update_category(self.large.id,'small')
        returned_category_list=Category.objects.all()
        self.assertTrue(len(returned_category_list)==1)
        updated_category_object=Category.objects.all().first()
        self.assertTrue(updated_category_object.name=='small')

class ImageTestClass(TestCase):
    def setUp(self):
        self.tech= Image (name='tech',description='network topology')
         
    def test_instance(self):
        self.assertTrue(isinstance(self.tech, Image))

    def test_save_image(self):
        self.tech.save_images()
        searched_image = Image.objects.all()
        self.assertTrue(len(searched_image) >0) 

    def test_delete_image(self):
        self.tech.save_images()
        self.tech.delete_image()
        found_after_delete=Image.objects.all()
        self.assertTrue(len(found_after_delete)==0)   