from rest_framework import viewsets, permissions
from .models import ExpenseIncome
from .serializers import ExpenseIncomeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return ExpenseIncome.objects.all()
        return ExpenseIncome.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User created successfully', 'user': serializer.data}, status=201)
    return Response(serializer.errors, status=400)