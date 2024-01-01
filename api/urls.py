from django.urls import path
from api import views



urlpatterns=[
    path('mobile/',views.MobileListCreateView.as_view()),
    path('mobile/<int:pk>/',views.MobileUpdateDetailDestroyView.as_view()),
]