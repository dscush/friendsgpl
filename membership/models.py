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

class MemberManager(models.Manager):
    def active_members(self):
        member_ids = [member.id for member in self.all() if member.family.is_active()]
        return self.filter(pk__in=member_ids)
    def dues_counts(self):
        dues = [member.family.dues_amount for member in self.all() if member.family.is_active()]
        return {i:len([d for d in dues if d == i]) for i in set(dues)}

class FamilyManager(models.Manager):
    def total_dues_fiscal_year(self):
        return sum(family.dues_amount for family in self.all() if family.paid_this_fiscal_year())
    def total_dues_prev_12mo(self):
        return sum(family.dues_amount for family in self.all() if family.is_active())
    def dues_counts(self):
        dues = [family.dues_amount for family in self.all() if family.is_active()]
        return {i:len([d for d in dues if d == i]) for i in set(dues)}

class Family(models.Model):
    objects = FamilyManager()
    family_name = models.CharField(max_length=200)
    family_name_2 = models.CharField(max_length=200, blank=True, verbose_name='Alternative family name')
    street_address_1 = models.CharField(max_length=200, blank=True)
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
    def paid_this_fiscal_year(self):
        start_fiscal_year = timezone.now().date().replace(month=7)
        if start_fiscal_year > timezone.now().date():
            start_fiscal_year = start_fiscal_year.replace(year=timezone.now().year-1)
        return self.last_paid >= start_fiscal_year
    paid_this_fiscal_year.admin_order_field = last_paid
    paid_this_fiscal_year.boolean = True
    paid_this_fiscal_year.short_description = 'Dues paid this fiscal year?'
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
        if self.family_name_2:
            return self.family_name + '/' + self.family_name_2
        return self.family_name

class Member(models.Model):
    objects = MemberManager()
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    family = models.ForeignKey(Family)
    email = models.EmailField(blank=True, null=True, validators=[validate_email])
    personal_phone = models.IntegerField(
        validators=phone_validators,
        blank=True,
        null=True,
    )
    comment = models.CharField(max_length=200, blank=True)
    volunteer = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    trustee = models.BooleanField(default=False)
    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    def __str__(self):
        return self.full_name

class Committee(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    members = models.ManyToManyField(Member, through='Role')

class Role(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    def __str__(self):
        return "%s, %s" % (self.member.__str__(), self.title)
    def __key__(self):
        role_order = {
            'president': 0,
            'secretary': 1,
            'treasurer': 2,
            'director': 1000,
            'chair': 2000,
            'member': 3000,
        }
        key = role_order.get(self.title.lower())
        if key is None:
            for ro in role_order:
                if ro in self.title.lower():
                    key = role_order.get(ro) + 0.0001
        if key is None:
            key = 1000000
        return key
    def __lt__(self, other):
        return self.__key__() < other.__key__()

