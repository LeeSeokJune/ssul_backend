from django.urls import path
import views

urlpatterns = [
    path('select-category/', views.select_category)
]
