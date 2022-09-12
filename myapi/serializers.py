from rest_framework import serializers
from myapi.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=('company_id', 'Company_name', 'location', 'about','type','added_date','active')
