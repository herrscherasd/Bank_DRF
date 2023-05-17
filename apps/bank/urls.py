from django.urls import path

from .views import CreateTransferView

urlpatterns = [
    path('transfer/', CreateTransferView.as_view(), name = "transfer"),
]