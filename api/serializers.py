from rest_framework import serializers
from .models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    company = serializers.RelatedField(source='company', read_only=True)

    class Meta:
        model = Vacancy
        fields = ['id', 'name', 'salary', 'company']
