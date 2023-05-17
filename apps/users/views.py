from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.users.models import BankUser
from apps.users.serializer import BankUserSerializer, RegisterUserSerializer

# Create your views here.
class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin):
    queryset = BankUser.objects.all()
    serializer_class = BankUserSerializer

    def get_serializer_class(self):
        if self.action in ('create', ):
            return RegisterUserSerializer
        return BankUserSerializer