from django.urls import path
from .views import create_transaction

urlpatterns = [
    path("create_transaction", create_transaction, name="create-transaction")
]
