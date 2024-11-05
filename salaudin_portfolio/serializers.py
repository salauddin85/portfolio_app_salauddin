from rest_framework import serializers
from .models import SalauddinPortfolio

class SalauddinPortfolioSerializer(serializers.ModelSerializer):
    message = serializers.CharField(max_length=5000)  # Set your desired max length here

    class Meta:
        model = SalauddinPortfolio
        fields = ['name', 'email', 'subject', 'message']
