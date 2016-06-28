#!/usr/bin/env python3

from django.core.management.base import BaseCommand, CommandError
import csv
from datetime import date
#from friends import settings
#from django.core.management import setup_environ
#setup_environ(settings)
#import django
#django.setup()
from membership.models import Member, Family

class Command(BaseCommand):
    help = "Save all membership data to a csv file"

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            default='./friends_member_list_' + date.today().isoformat() + '.csv',
            help='Location of the resulting csv file',
            nargs='?',
        )

    def handle(self, *args, **options):
        fams = Family.objects.all()
        famlist = [[
            'Family Name',
            'Other Family Name',
            'Primary Member',
            'Email',
            'Phone',
            'Street Address 1',
            'Street Address 2',
            'City',
            'Zip Code',
            'Date Last Paid',
            'Dues Amount',
            'Volunteer',
            'Other Family Members',
            'Comment',
        ]]
        for f in fams:
            mems = f.member_set.all()
            mems_with_emails = mems.exclude(email__isnull=True).exclude(email__exact='')
            primary_member = mems_with_emails and mems_with_emails[0] or mems[0]
            other_members = mems.exclude(first_name=primary_member.first_name) | mems.exclude(last_name=primary_member.last_name)
            if other_members:
                other_members = [m.first_name + ' ' +  m.last_name for m in other_members]
                other_members = ', '.join(other_members)
            else:
                other_members = ''
            if f.zip_code in ('01519', '01536', '01560'):
                city = {'01519':'Grafton', '01536':'North Grafton', '01560':'South Grafton'}[f.zip_code]
                state = 'MA'
            else:
                city = state = ''
            if f.home_phone:
                phone = str(f.home_phone)
                phone = '%s-%s-%s' % (phone[:3],phone[3:6],phone[6:])
            else:
                phone = ''
            if f.last_paid == date(1,1,1):
                last_paid = ''
            else:
                last_paid = f.last_paid
            comments = [f.comment] + [m.comment for m in mems if m.comment]
            comment = ' | '.join(filter(lambda c:c, comments))
            #if comment == ' | ':
            #    comment = ''
            famlist.append([
                f.family_name,
                f.family_name_2,
                primary_member.first_name + ' ' + primary_member.last_name,
                primary_member.email,
                phone,
                f.street_address_1,
                f.street_address_2,
                city,
                f.zip_code,
                last_paid,
                f.dues_amount,
                primary_member.volunteer and 'x' or '',
                other_members,
                comment,
            ])

        with open(options['filename'], 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, dialect='excel')
            csvwriter.writerows(famlist)

