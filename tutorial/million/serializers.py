from rest_framework import serializers
from million.models import*#импорт звездочка импортируют все файлы
class Sex_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Sex
		fields=('sex_name',)
