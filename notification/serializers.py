from rest_framework import serializers
from notification.models import DeviceToken

class TokenSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = DeviceToken
        fields = ['id', 'token', 'Type', 'device', 'creator', 'created']