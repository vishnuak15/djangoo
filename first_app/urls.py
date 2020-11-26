from .views import EntityDetailView,ProgramDetailView,EntityCreateView,EntityUpdateView,EntityDeleteView,ProgramUpdateView#,ProgramDeleteView
from django.urls import path
from first_app import views
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    
    path('front/', views.front, name='front'),
    path('upload/<int:pk>', views.Upload, name='upload'),
    path('entitys/', views.entitys, name='entitys'),
    path('prog/<int:pk>', views.prog, name='prog'),
    path('users/<int:pk>', views.users, name='users'),
    path('addorg/', views.EntityCreateView.as_view(), name='addorg'),
    #path('addprog/',views.ProgramCreateView.as_view(), name='addprog'),
    path('adduser/<int:pk>/', views.add_User, name='adduser'),
    path('addprog/<int:pk>/', views.add_Program, name='addprog'),
    path('entity/edit/<int:pk>/',EntityUpdateView.as_view(), name='updatentity'),
    path('prog/edit/<int:pk>/',ProgramUpdateView.as_view(), name='updateprog'),
    path('entity/<int:pk>/delete/',EntityDeleteView.as_view(), name='deletentity'),
    path('program/delete/<int:pk>/',views.Program_remove, name='deleteprogram'),
    path('user/delete/<int:pk>/',views.User_remove, name='deleteuser'),
    url(r'^detail/(?P<pk>\d+)$', views.EntityDetailView.as_view(), name='detail'),
    url(r'^programs/(?P<pk>\d+)$', views.ProgramDetailView.as_view(), name='program')
]


