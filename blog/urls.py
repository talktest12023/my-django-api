from django.urls import path
from . import views
from .views import post_detail

urlpatterns = [
    path('', views.post_list, name='home'),  # Homepage shows all posts
    path('about/', views.about, name='about'),  # New route for the about page
    path('post/<int:post_id>/', post_detail,
         name='post-detail'),  # URL with parameter
]
