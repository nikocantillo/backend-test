from rest_framework_simplejwt.serializers import  TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)
        data['access'] = token_backend.encode(decoded_payload)
        return data