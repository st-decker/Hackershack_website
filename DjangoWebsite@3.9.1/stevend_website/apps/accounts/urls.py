from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "accounts"
urlpatterns = [
    # path('about', views.about, name='about'),
    # path('contact', views.contact, name='contact'),
    path("profile", views.ProfileView.as_view(), name="profile"),
    # path('', TemplateView.as_view(template_name="index.html"), name='index')
    # Django Auth
    path(
        "login",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
