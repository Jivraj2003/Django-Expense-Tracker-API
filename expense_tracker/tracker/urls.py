from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseIncomeViewSet, register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router and register the viewset with it
router = DefaultRouter()
router.register('expenses', ExpenseIncomeViewSet,basename='expenses')
urlpatterns = [
    # API endpoint for user registration
    path('auth/register/', register,),
    # JWT authentication endpoints
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Token refresh endpoint
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Include the router's URLs
    path('', include(router.urls)),
]