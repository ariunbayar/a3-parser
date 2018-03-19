from django.core.management.base import BaseCommand
# from endpoint.models import Department, Employee
from main.models import Certificate
import json


class Command(BaseCommand):
    help = 'Parse and save certificate data from json'

    def handle(self, *args, **options):


        with open('/dev/stdin') as f:
            data = json.load(f)

        cert_data = data.get('certificateList')
        if not cert_data:
            self.stdout.write(self.style.ERROR('No data recieved at'))
        else:
            self.stdout.write(self.style.SUCCESS('%s certificates found' % len(cert_data)))

        for c in cert_data:

            cert = Certificate()
            cert.person_id = c.get('personId')
            cert.firstname = c.get('firstName')
            cert.lastname = c.get('lastName')
            cert.register = c.get('register')
            cert.email = c.get('email')
            cert.certificate_number = c.get('certificateNumber')
            cert.certificate_type_name = c.get('certificateTypeName')
            cert.city_segment_value_name = c.get('citySegmentValueName')
            cert.district_segment_value_name = c.get('districtSegmentValueName')
            cert.industry_names = c.get('industryNames')
            cert.start_date = c.get('startDate')
            cert.start_date_string = c.get('startDateString')
            cert.end_date = c.get('endDate')
            cert.end_date_string = c.get('endDateString')
            cert.save()
