from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_migrate
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Permission
from django.conf import settings
from django.dispatch import receiver


class UpperCaseCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCaseCharField, self).pre_save(model_instance, add)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    meting_ids = UpperCaseCharField(max_length=240, null=True)

    def __str__(self):
        return self.user.username


@receiver(pre_migrate, sender=auth_models)
def add_user_permissions(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(settings.AUTH_USER_MODEL)
    Permission.objects.get_or_create(codename='view_user', name='View user', content_type=content_type)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()