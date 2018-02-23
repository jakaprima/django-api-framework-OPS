from rest_framework import serializers
from .models import SettingWeb

class SettingWebSerializer(serializers.ModelSerializer):
	class Meta:
		model = SettingWeb
		fields = ('id', 'nama_web', 'deskripsi_web')