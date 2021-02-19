from django.urls import path

from . import views

# all urls identifies prefixed with "public"
app_name = "public"
urlpatterns = [
    path("", views.index, name="index"),  # home page
    path("about", views.about, name="about"),
    # path("contact", views.contact, name="contact"),
    # path('', TemplateView.as_view(template_name="index.html"), name='index')
]
