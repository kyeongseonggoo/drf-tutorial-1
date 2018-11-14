from . import views
from django.urls import path

urlpatterns = [
    path('snippets/', views.snippet_list),
]