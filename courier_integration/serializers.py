from rest_framework import serializers

from courier_integration.models import Couriers


class CourierSerializer(serializers.ModelSerializer):
    waybillID = serializers.CharField(max_length=200)
    label = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=50)

    class Meta:
        model = Couriers
        fields = '__all__'
