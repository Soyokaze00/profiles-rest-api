from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView""" #something like a form which accepts imputs and stuff
    name = serializers.CharField(max_length=20)
