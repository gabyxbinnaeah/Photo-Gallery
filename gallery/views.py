from django.shortcuts import render
from .models import Image

def gallery(request):
    photo_contents=Image.found_images()
    return render(request, 'gallery.html',{"photo_contents":photo_contents})
