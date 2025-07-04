from rest_framework import serializers
from .models import ExpenseIncome
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
        
class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    class Meta:
        model = ExpenseIncome
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at', 'total']
        
    def get_total(self, obj):
        return obj.total
    
    