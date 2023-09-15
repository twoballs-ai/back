from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from test_main import views

urlpatterns = [
    path('menu/', views.MenuList.as_view()),
    path('blocks/', views.BlockList.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)