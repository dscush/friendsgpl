from django.contrib import admin

from .models import Family, Member

class MemberInline(admin.TabularInline):
    model = Member
    extra = 0

class FamilyAdmin(admin.ModelAdmin):
    '''fieldsets = [
        (None, {'fields': ['family_name']}),
        ('Contact information', {'fields': [
            'street_address_1',
            'street_address_2',
            'zip_code',
            'home_phone',
        ]}),
        ('Dues', {'fields': ['dues_amount', 'last_paid']}),
    ]'''
    def members(self, f):
        return ', '.join([str(m) for m in f.member_set.all()])
    list_display = (
        'family_name',
        'members',
        'last_paid',
        'is_active',
        'is_grafton_resident',
    )
    inlines = [MemberInline]
    #list_filter = ['last_paid',]
    search_fields = ['family_name',]

admin.site.register(Family, FamilyAdmin)
admin.site.register(Member)

