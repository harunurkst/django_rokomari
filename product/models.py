from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=150)
    # photo = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name