from rest_framework import serializers
from .models import AudioGear

class AudioGearSerializer(serializers.ModelSerializer):
# With Meta Class/ Model Serializer
    class Meta:
        model = AudioGear
        # fields = ['id', 'name', 'quantity', 'price']
        fields = '__all__'



# Without Meta Class    
    # name = serializers.CharField(max_length=30)
    # quantity = serializers.IntegerField()
    # price = serializers.FloatField()

    # def create(self, validated_data):
    #     return AudioGear.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.quantity = validated_data.get('quantity', instance.quantity)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.save()
    #     return instance