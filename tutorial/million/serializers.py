from rest_framework import serializers
from million.models import *
class Sex_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Sex
		fields=('sex_name',)
