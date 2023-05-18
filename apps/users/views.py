from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import BankUser

from apps.users.serializer import UserSerializer ,RegisterUserSerializer, UserDetailSerializer

# Create your views here.
class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin):
    queryset = BankUser.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ('create', ):
            return RegisterUserSerializer
        if self.action in ('retrieve', ):
            return UserDetailSerializer
        return UserSerializer

    