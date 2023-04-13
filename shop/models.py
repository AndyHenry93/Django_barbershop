from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# TODO: create profile class
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="img/avatar/%Y/%m/%d", default="avatar.jpg")
    follows = models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    shop_address = models.CharField(max_length=100, blank= True, null=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    client_photo = models.ImageField(upload_to="img/client/%Y/%m/%d", null=True)
    is_barber = models.BooleanField(default=False, blank=True)


    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("shop:profile", args=[self.profile.id])

# signal function which creates a new profile object when users are created
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])