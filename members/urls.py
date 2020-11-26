from django.urls import path
from members import views

urlpatterns = [
    #path('register/',UserRegisterView.as_view(),name='register'),   
    path('register/', views.register, name='register'),
]