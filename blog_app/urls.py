from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('show-blog/',views.show_blog,name="show_blog"),
    path('create-blog/',views.create_blog,name="create_blog"),
    
]




