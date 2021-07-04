from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.bondo = Location(name = 'bpndo')

    def test_instance(self):
        self.assertTrue(isinstance(self.bondo, Location))

    