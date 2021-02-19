from django.urls import path

from .views import contact

app_name = "contact"
# View is called contact
urlpatterns = [
    path("", contact, name='contact')
]