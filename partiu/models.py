from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.utils import timezone

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Model for user
    """

    email = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField('Is Staff?', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return "User {}".format(self.email)


class Transaction(models.Model):
    """ Model for transactions
    """

    TYPES = [
        ('entrance', 'Entrance'),
        ('exit', 'Exit')
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='transactions',
        null=True
    )
    type = models.CharField(max_length=8, choices=TYPES)
    value = models.IntegerField()
    created_on = models.DateTimeField('created on', default=timezone.now)
    updated_on = models.DateTimeField('updated on', default=timezone.now)

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

    def __str__(self):
        return "Transaction {}".format(self.id)
