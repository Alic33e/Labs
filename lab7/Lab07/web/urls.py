from django.urls import path
from .views import *

app_name = 'web'

urlpatterns = [
    path('', PrincipalView.as_view(), name='index_principal'),
    path('eliminar/<int:id>/', EliminarView.as_view(), name='eliminar'),
]

