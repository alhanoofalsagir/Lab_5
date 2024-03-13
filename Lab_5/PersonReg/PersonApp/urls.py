from django.urls import path
from .views import add_view, list_view

urlpatterns = [
    path('add/', add_view, name='add_view'),  # Updated the view name
    path('', list_view, name='list_view'),    # Updated the view name
]
