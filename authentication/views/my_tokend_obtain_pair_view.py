import django
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import (
	InvalidToken, 
	TokenError
)
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authentication.domain import User
from django.db import connection
from rest_framework import status


class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer

	def post(self, request, *args, **kwargs):
		django.setup()
		if not connection.in_atomic_block:
			connection.close()
		data = request.data
		serializer = self.get_serializer(data=data)
		try:
			serializer.is_valid(raise_exception=True)
		except TokenError as e:
			raise InvalidToken(e.args[0])
		data = serializer.validated_data
		return Response(data,  status=status.HTTP_200_OK)