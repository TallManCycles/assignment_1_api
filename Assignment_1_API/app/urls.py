from django.urls import path
from app.views import get_current_server_time

urlpatterns = [
  path('server_time/', get_current_server_time)
]

app_name = 'app'