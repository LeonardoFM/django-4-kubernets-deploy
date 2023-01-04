from rest_framework import serializers


class VehicleSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200, default='')
    date = serializers.DateField()
    price = serializers.IntegerField(default=0)
    cost = serializers.IntegerField(default=0)
