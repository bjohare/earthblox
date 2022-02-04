from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel
from django.contrib.postgres.fields import ArrayField
from django_countries.fields import CountryField
from enum import Enum
from apps.users.models import User


class Supplier(TimeStampedModel):

    # defines permissible choices for datatypes field
    class DATATYPES(Enum):
        geotagged_photos = ('GP', 'Geotagged Photos')
        drone_photo = ('DP', 'Drone Photography')
        ground_point = ('GC', 'Ground Control Points')
        drone_video = ('DV', 'Drone Video')
        drone_lidar = ('DL', 'Drone Lidar')
        drone_radar = ('DR', 'Drone Radar')
        aerial_video = ('AV', 'Aerial Video')
        aerial_radar = ('AR', 'Aerial Radar')
        aerial_lidar = ('AL', 'Aerial Lidar')
        aerial_photo = ('AP', 'Aerial Photo')
        stereo_photo = ('SP', 'Stereo Photo')
        other = ('OT', 'Other')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    class Meta:
        indexes = [
            models.Index(fields=['company_name'], name="company_name_idx"),
            models.Index(fields=['email'], name="email_idx"),
        ]

    company_name = models.CharField(
        max_length=150, verbose_name=_('Company Name'))
    contact_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name=_('Email'))
    datatypes = ArrayField(
        base_field=models.CharField(
            max_length=2, blank=False,
            choices=[x.value for x in DATATYPES],
        ),
        default=list,
        verbose_name=_('Datatypes collected')
    )
    countries = CountryField(
        multiple=True, verbose_name=_('Operating Countries'), default="GB")
    consent = models.BooleanField(verbose_name=_('Consent'))
    certified = models.BooleanField(verbose_name=_('Certified'))

    def __str__(self):
        return (f"""Supplier: {self.company_name}, email: {self.email}.""")
