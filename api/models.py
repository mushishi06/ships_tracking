from django.db import models

# Create your models here.

class Ship(models.Model):
    name = models.CharField(max_length=30)
    imo = models.PositiveIntegerField(unique=True)

    @classmethod
    def get_by_imo(cls, imo):
        return cls.objects.get(imo=imo)

    @classmethod
    def get_by_name(cls, name):
        return cls.objects.get(name=name)

    def __str__(self):
        return '{} - {}'.format(self.name, self.imo)


class Position(models.Model):
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    timestamp = models.DateTimeField()
    ship = models.ForeignKey(
        'Ship',
        on_delete=models.CASCADE,
    )
