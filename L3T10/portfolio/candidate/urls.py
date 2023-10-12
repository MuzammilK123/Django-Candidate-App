from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='candidate/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]