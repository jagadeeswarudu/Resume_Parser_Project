from django.urls import path
from . import views 

app_name = 'calc'
urlpatterns=[
    path('',views.upload,name='upload'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('upload/',views.upload,name='upload'),
    path('upload_text/',views.upload_text,name='upload_text'),
]
