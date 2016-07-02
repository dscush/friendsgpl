from collections import OrderedDict
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext

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

    mem_dues = Member.objects.dues_counts()
    fam_dues = Family.objects.dues_counts()
    mem_dues_data = [mem_dues[k] for k in sorted(mem_dues)]
    fam_dues_data = [fam_dues[k] for k in sorted(fam_dues)]
    dues_counts_col_headers = ['$' + str(x) for x in sorted(mem_dues)]

    return render_to_response(
        'membership/admin/datasheet.html',
        {
            'title': 'Datasheet',
            'datasets': [
                Dataset(
                    name='General Membership Info',
                    data=[
                        [Member.objects.active_members().count()],
                        ['$' + str(Family.objects.total_dues_fiscal_year())],
                        ['$' + str(Family.objects.total_dues_prev_12mo())],
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
                    col_headers=dues_counts_col_headers
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
						('Total dues fiscal year', ('$' + str(Family.objects.total_dues_fiscal_year()),)),
						('Total dues prev 12mo', ('$' + str(Family.objects.total_dues_prev_12mo()),)),
					]),
				},
				{
					'name': 'Dues Counts',
					'data':	OrderedDict([
						# TODO: organize after creating dataset class
						('Member dues counts', (Member.objects.dues_counts(),'foo')),
						('Family dues counts', (Family.objects.dues_counts(),'bar')),
					]),
				},
			],
        },
        RequestContext(request, {})
    )'''
admin.site.register_view('datasheet', view=datasheet_view, name='Datasheet')

