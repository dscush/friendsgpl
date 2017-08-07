from collections import OrderedDict
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import DuesPayment, Member, Committee, Role

class MemberInline(admin.TabularInline):
    model = Member.dues_payments.through
    extra = 2

class MemberAdmin(admin.ModelAdmin):
    def is_grafton_resident(self, m):
        return m.dues_payment.is_grafton_resident()
    is_grafton_resident.boolean = True
    list_display = (
        'full_name',
        'is_grafton_resident',
        'volunteer',
        'trustee',
        'staff',
    )
    inlines = [MemberInline]
    search_fields = ['first_name','last_name', 'dues_payment__family_name']

class DuesPaymentAdmin(admin.ModelAdmin):
    '''fieldsets = [
        (None, {'fields': ['family_name']}),
        ('Contact information', {'fields': [
            'street_address_1',
            'street_address_2',
            'zip_code',
            'home_phone',
        ]}),
        ('Dues', {'fields': ['amount', 'date_paid']}),
    ]'''
    def members(self, f):
        return ', '.join([str(m) for m in f.member_set.all()])
    list_display = (
        '__str__',
        'members',
        'date_paid',
        'is_active',
        'paid_this_fiscal_year',
        'is_grafton_resident',
    )
    inlines = [MemberInline]
    #list_filter = ['date_paid',]
    search_fields = ['family_name','family_name_2']

class RoleInline(admin.TabularInline):
    model = Role
    extra = 2

class CommitteeAdmin(admin.ModelAdmin):
    def committee_members(self, c):
        return '; '.join([str(m) for m in c.role_set.all()])
    list_display = (
        'name',
        'committee_members',
    )
    inlines=[RoleInline]

admin.site.register(DuesPayment, DuesPaymentAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Committee, CommitteeAdmin)

def datasheet_view(request):
    class Dataset():
        def __init__(self, name, data, row_headers=None, col_headers=None):
            self.name = name
            self.data = data
            self.row_headers = row_headers
            self.col_headers = col_headers
            self.has_row_headers = False
            if self.row_headers:
                self.has_row_headers = True
                for i, data_row in enumerate(data):
                    data_row.insert(0,row_headers[i])

    mem_dues = Member.objects.level_counts()
    fam_dues = DuesPayment.objects.level_counts()
    mem_dues_data = [mem_dues[k] for k in sorted(mem_dues)]
    fam_dues_data = [fam_dues[k] for k in sorted(fam_dues)]
    level_counts_col_headers = ['$' + str(x) for x in sorted(mem_dues)]

    return render_to_response(
        'membership/admin/datasheet.html',
        {
            'title': 'Datasheet',
            'datasets': [
                Dataset(
                    name='General Membership Info',
                    data=[
                        [Member.objects.active_members().count()],
                        ['$' + str(DuesPayment.objects.total_fiscal_year())],
                        ['$' + str(DuesPayment.objects.total_prev_12mo())],
                    ],
                    row_headers=(
                        'Number of active members',
                        'Total dues fiscal year',
                        'Total dues prev 12mo',
                    )
                ),
                Dataset(
                    name='Dues Counts',
                    data=[
                        mem_dues_data,
                        fam_dues_data,
                    ],
                    row_headers=(
                        'Member dues counts',
                        'Family dues counts',
                    ),
                    col_headers=level_counts_col_headers
                ),
            ]
        },
        RequestContext(request, {})
    )
'''    return render_to_response(
        'membership/admin/datasheet.html',
        {
            'title': 'Datasheet',
			# TODO: Make this more pythonic and less JSONic (make dataset class)
			'datasets': [
				{
					'name': 'General Membership Info',
					'data':	OrderedDict([
						('Number of active members', (Member.objects.active_members().count(),)),
						('Total dues fiscal year', ('$' + str(DuesPayment.objects.total_fiscal_year()),)),
						('Total dues prev 12mo', ('$' + str(DuesPayment.objects.total_prev_12mo()),)),
					]),
				},
				{
					'name': 'Dues Counts',
					'data':	OrderedDict([
						# TODO: organize after creating dataset class
						('Member dues counts', (Member.objects.level_counts(),'foo')),
						('Family dues counts', (DuesPayment.objects.level_counts(),'bar')),
					]),
				},
			],
        },
        RequestContext(request, {})
    )'''
admin.site.register_view('datasheet', view=datasheet_view, name='Datasheet')

