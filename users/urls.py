from django.urls import path
from . import views

# from .views import SignUpView

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('panel/', views.panel, name='panel')
]
