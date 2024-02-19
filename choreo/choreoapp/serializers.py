from choreoapp.models import Dancer
from rest_framework import serializers

class DancerSerializer(serializers.ModelSerializer):
    class Meta:
        #сериализуемая модель
        model = Dancer
        #сериализуемые поля
        fields = ['dancer_id', 'name', 'position', 'number']


