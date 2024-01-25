from  rest_framework import serializers

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direction = serializers.charField()
    pais = serializers.CharField()
    descripcion = serializers.charField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()