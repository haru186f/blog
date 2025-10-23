from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='Login'),
    path('accounts/logout', views.LogoutView.as_view(next_page='/', name='logout')),
    path('', include('apps.blog.urls')),
]
