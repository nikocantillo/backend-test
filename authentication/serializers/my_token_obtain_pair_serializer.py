from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from datetime import datetime

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  """
  Serializer para la customizar los parámetros encriptados en el JWT. 
  """
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    if user.last_login:
        token['last_login'] = user.last_login.strftime("%Y/%m/%d - %H:%M:%S")
    user.last_login = datetime.now()
    user.save()
    return token
