from django.urls import path
from ssul import views

urlpatterns = [
    path('register/', views.register_ssul),

]
