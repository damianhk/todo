from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_id>', views.category, name='category')
]