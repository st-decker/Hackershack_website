"""stevend_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("stevend_website.apps.public.urls")),  # home page
    path("accounts/", include("stevend_website.apps.accounts.urls")),
    path("contact/", include("stevend_website.apps.contact.urls")),
    # path('about', views.about, name='about'),
    # path('contact', views.contact, name='contact'),
    # path('accounts/profile', views.ProfileView.as_view(), name='profile'),
    # path('', TemplateView.as_view(template_name="index.html"), name='index')
    # Django Auth
    # path('accounts/login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('accounts/logout', auth_views.LogoutView.as_view(), name='logout')
]

# register all below with command
# path('accounts/', include('django.contrib.auth.urls'))

# 8 different views login app views. Preconfigured templates
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change_done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset_done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done [name='password_reset_complete']

# manage.py createsuperuser
