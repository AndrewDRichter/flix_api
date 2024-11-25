from rest_framework import serializers
from .models import Movie

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def get_rate(self, obj):
        return 5

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1900.')
        return value
    
    def validate_summary(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Summary não deve conter mais de 500 caracteres.')