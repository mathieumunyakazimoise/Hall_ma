from django.urls import path
from . import views

urlpatterns = [
    path("buildings/", views.BuildingListCreateAPIView.as_view(), name="buildings"),
    path("buildings/<int:pk>/", views.BuildingRetrieveUpdateDestroyAPIView.as_view(), name="buildings-view-update-delete"),

    path("rooms/", views.RoomListCreateAPIView.as_view(), name="rooms"),
    path("rooms/<int:pk>/", views.RoomRetrieveUpdateDestroyAPIView.as_view(), name="rooms-view-update-delete"),

    path("room_applications/", views.RoomApplicationListCreateAPIView.as_view(), name="room_applications"),
    path("room_applications/<int:pk>/", views.RoomApplicationRetrieveUpdateDestroyAPIView.as_view(), name="room_applications-view-update-delete"),

    path("maintenance_requests/", views.MaintenanceRequestListCreateAPIView.as_view(), name="maintenance_requests"),
    path("maintenance_requests/<int:pk>/", views.MaintenanceRequestDetailAPIView.as_view(), name="maintenance_requests-view-update-delete"),
    
    path("event/", views.EventListCreateAPIView.as_view(), name="event"),
    path("event/<int:pk>/", views.EventDetailAPIView.as_view(), name="event-view-update-delete"),
    
    path("communication/", views.CommunicationListCreateAPIView.as_view(), name="communication"),
    path("communication/<int:pk>/", views.CommunicationDetailAPIView.as_view(), name="communication-view-update-delete"),
]
