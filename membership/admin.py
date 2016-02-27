from django.contrib import admin

from .models import Family, Member

class MemberAdmin(admin.ModelAdmin):
    def is_grafton_resident(self, m):
        return m.family.is_grafton_resident()
    is_grafton_resident.boolean = True
    list_display = (
        'full_name',
        'family',
        'is_grafton_resident',
        'volunteer',
        'board',
        'trustee',
        'staff',
    )
    search_fields = ['first_name','last_name', 'family__family_name']

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
        '__str__',
        'members',
        'last_paid',
        'is_active',
        'paid_this_fiscal_year',
        'is_grafton_resident',
    )
    inlines = [MemberInline]
    #list_filter = ['last_paid',]
    search_fields = ['family_name','family_name_2']

admin.site.register(Family, FamilyAdmin)
admin.site.register(Member, MemberAdmin)

