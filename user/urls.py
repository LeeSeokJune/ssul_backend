from django.urls import path
import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('select-category/', views.select_category),

]
