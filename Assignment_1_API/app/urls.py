from django.urls import path
from app.views import get_current_server_time, load_locations, export_itinerary

urlpatterns = [
  path('server_time/', get_current_server_time),
  path('load_locations/', load_locations),
  path('export_itinerary/', export_itinerary)
]

app_name = 'app'