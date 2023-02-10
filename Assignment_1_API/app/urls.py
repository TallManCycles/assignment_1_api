from django.urls import path
from app.views import get_current_server_time, load_locations

urlpatterns = [
  path('server_time/', get_current_server_time),
  path('load_locations/', load_locations)
]

app_name = 'app'