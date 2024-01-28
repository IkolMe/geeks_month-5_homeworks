from rest_framework import serializers


class DirectorSerializer(serializers.Serializer):
    class Meta:
        fields = 'name'.split()


class MovieSerializer(serializers.Serializer):
    class Meta:
        fields = 'title description duration director'.split()


class ReviewSerializer(serializers.Serializer):
    class Meta:
        fields = 'text movie'
