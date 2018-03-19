from django.db import models


class Certificate(models.Model):
    person_id = models.IntegerField(null=True)
    firstname = models.CharField(max_length=250, null=True)
    lastname = models.CharField(max_length=250, null=True)
    register = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    certificate_number = models.CharField(max_length=250, null=True)
    certificate_type_name = models.CharField(max_length=250, null=True)
    city_segment_value_name = models.CharField(max_length=250, null=True)
    district_segment_value_name = models.CharField(max_length=250, null=True)
    industry_names = models.CharField(max_length=250, null=True)
    start_date = models.CharField(max_length=250, null=True)
    start_date_string = models.CharField(max_length=250, null=True)
    end_date = models.CharField(max_length=250, null=True)
    end_date_string = models.CharField(max_length=250, null=True)
