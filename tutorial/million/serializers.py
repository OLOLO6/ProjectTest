from rest_framework import serializers
from million.models import *
class Singers_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Singers
		fields=('id','names','ages','phoneNumber')

class Groups_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Groups
		fields=('name','style','singers')

class  Concert_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Concert
		fields=('time','who','place')

