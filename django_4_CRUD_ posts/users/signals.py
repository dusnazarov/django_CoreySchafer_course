
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("profile created!")

@receiver(post_save,sender=User)
def update_profile(sender, instance,**kwargs):  
    instance.profile.save()
    print("profile updated!")
    print(instance.profile)



""" 
in the app.py, we added  this 

( 
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
)



"""