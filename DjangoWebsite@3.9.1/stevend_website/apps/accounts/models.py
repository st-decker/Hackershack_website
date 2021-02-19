from django.db import models
from django.contrib.auth.models import User

# blank means optional


class UserInterest(models.Model):
    # name of interest
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)

    # string function to print the name
    def __str__(self):
        return self.name


class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class UserProfile(models.Model):
    # Owner. Foreign key. Whenever we fetch user, we should fetch the user profile
    # related_name = we can access profile through user object aka request.user.profile
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # settings
    is_full_name_displayed = models.BooleanField(default=True)

    # details
    bio = models.CharField(max_length=500, default=True, null=True)
    website = models.URLField(max_length=500, default=True, null=True)
    persona = models.ForeignKey(
        UserPersona, on_delete=models.SET_NULL, blank=True, null=True
    )
    interests = models.ManyToManyField(
        UserInterest, blank=True
    )  # field that references user profile
