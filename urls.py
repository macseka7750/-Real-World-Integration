from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.py),
    
    # Auth Endpoints
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Modular App Endpoints
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/blog/', include('apps.blog.urls')),
    path('api/v1/payments/', include('apps.payments.urls')),
]
