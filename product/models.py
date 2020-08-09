from django.db import models
from django.urls import reverse


class Writer(models.Model):
    name = models.CharField(max_length=150)
    # photo = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('writer_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name