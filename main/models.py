from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    COMPACT = 'compact'
    SEDAN = 'sedan'
    SUV = 'suv'
    CONVERTIBLE = 'convertible'
    COUPE = 'coupe'

    CAR_TYPE_CHOICES = (
        (COMPACT, 'Compact'),
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (CONVERTIBLE, 'Convertible'),
        (COUPE, 'Coupe'),
    )
    title = models.CharField(_('title'), max_length=255)
    model = models.CharField(_('model'), max_length=255, blank=True, null=True)
    condition = models.CharField(_('condition'), max_length=255, blank=True, null=True)
    color = models.CharField(_('color'), max_length=255, blank=True, null=True)
    drive_type = models.CharField(_('drive_type'), max_length=255, blank=True, null=True)
    transmission = models.CharField(_('transmission'), max_length=255, blank=True, null=True)
    year = models.CharField(_('year'), max_length=255, blank=True, null=True)
    mileage = models.CharField(_('mileage'), max_length=255, blank=True, null=True)
    fuel_type = models.CharField(_('fuel_type'), max_length=255, blank=True, null=True)
    engine_size = models.CharField(_('engine_size'), max_length=255, blank=True, null=True)
    doors = models.CharField(_('doors'), max_length=255, blank=True, null=True)
    cylinders = models.CharField(_('cylinders'), max_length=255, blank=True, null=True)
    vin = models.CharField(_('vin'), max_length=255, blank=True, null=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)
    image1 = models.ImageField(_('image1'), upload_to='cars/')
    image2 = models.ImageField(_('image2'), upload_to='cars/', blank=True)
    image3 = models.ImageField(_('image3'), upload_to='cars/', blank=True)
    image4 = models.ImageField(_('image4'), upload_to='cars/', blank=True)
    image5 = models.ImageField(_('image5'), upload_to='cars/', blank=True)
    image6 = models.ImageField(_('image6'), upload_to='cars/', blank=True)
    description = models.TextField(_('description'), blank=True)
    is_new = models.BooleanField(blank=False)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)

    class Meta:
        verbose_name = _('car')
        verbose_name_plural = _('cars')
        ordering = ('title',)

    def __str__(self):
        return self.title


class OldCarInformation(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    history = models.TextField(_('color'), blank=True, null=True)
    number_owners = models.CharField(max_length=20)

    def __str__(self):
        return self.car.title


class Order(models.Model):
    name = models.CharField(_('name'), max_length=255)
    phone = models.CharField(_('phone'), max_length=255)
    email = models.CharField(_('email'), max_length=255)
    comment = models.CharField(_('comment'), max_length=255)

    def __str__(self):
        return self.name