from rest_framework.routers import SimpleRouter
from django.urls import path,include
from .views import (
	MyTokenObtainPairView
)

router = SimpleRouter()

urlpatterns = router.urls + [
	path('login/', MyTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
]