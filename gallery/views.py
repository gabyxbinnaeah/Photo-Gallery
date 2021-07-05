from django.shortcuts import render
from .models import Image

def gallery(request):
    photo_contents=Image.found_images()
    return render(request, 'gallery.html',{"photo_contents":photo_contents})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_by_category(search_term)
        message = f"{search_term}"

              

        return render(request, 'all-gallery/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})




def search_result(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_locations = Image.search_by_location(search_term)
        message = f"{search_term}"

              

        return render(request, 'all-gallery/location.html',{"message":message,"categories": searched_locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/location.html',{"message":message})
