from django.conf.urls import url
from . import views 

urlpatterns=[
    url('^$',views.gallery, name='galleryUrl'),
    
]