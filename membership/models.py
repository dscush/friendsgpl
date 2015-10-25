from django.db import models
from django.core.validators import (
    validate_email,
    RegexValidator,
    MinLengthValidator,
    MaxLengthValidator,
)
from django.utils import timezone

phone_validators = [
    RegexValidator(regex=r'^\d{10}$', message="Please enter a ten-digit phone number.")
]
zip_validators = [
    RegexValidator(regex=r'^\d{5}$', message="Please enter a five-digit ZIP code."),
]

class Family(models.Model):
    family_name = models.CharField(max_length=200)
    family_name_2 = models.CharField(max_length=200, blank=True, verbose_name='Alternative family name')
    street_address_1 = models.CharField(max_length=200, blank=False)
    street_address_2 = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=5, blank=False, validators=zip_validators)
    home_phone = models.IntegerField(
        validators=phone_validators,
        blank=True,
        null=True,
    )
    last_paid = models.DateField(verbose_name="date dues paid")
    dues_amount = models.PositiveSmallIntegerField()
    comment = models.CharField(max_length=200, blank=True)
    def is_active(self):
        year_ago = timezone.now().date().replace(year=timezone.now().year-1)
        return self.last_paid >= year_ago
    is_active.admin_order_field = last_paid
    is_active.boolean = True
    is_active.short_description = 'Dues paid?'
    def is_grafton_resident(self):
        return self.zip_code in ('01519', '01536', '01560')
    is_grafton_resident.admin_order_field = zip_code
    is_grafton_resident.boolean = True
    is_grafton_resident.short_description = 'Grafton resident(s)?'
    def __str__(self):
        return self.family_name

class Member(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    family = models.ForeignKey(Family)
    email = models.EmailField(blank=True, null=True, validators=[validate_email])
    personal_phone = models.IntegerField(
        validators=phone_validators,
        blank=True,
        null=True,
    )
    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    def __str__(self):
        return self.full_name

