from rest_framework_json_api import serializers
from census_api.models import Citizen

class CitizenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citizen
        fields = ('first_name','sur_name','age','gender' ,'mobile','email','address','tribe','state')

