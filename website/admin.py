from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CMSBlock, Page

class CMSBlockAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(CMSBlock, CMSBlockAdmin)

class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Page, PageAdmin)
