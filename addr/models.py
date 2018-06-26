from django.db import models
from django.utils import timezone


class Address(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    call_1 = models.CharField(max_length=20)
    call_2 = models.CharField(max_length=20, blank=True, null=True)
    e_mail = models.EmailField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

