from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import (
    Building, Room,
    RoomApplication, MaintenanceRequest,
    Event, Communication
)


# Building Serializer
class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = [
            "id",
            'name',
            'address',
            'capacity',
            'facilities',
            'description',
        ]


# Room Serializer
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            'room_number',
            'floor_number',
            'capacity',
            'building',
            'status',
            'room_type',
        ]


# Room Application Serializer
class RoomApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomApplication
        fields = [
            "id",
            'student',
            'room',
            'application_date',
            'status'
        ]


# Maintenance Request Serializer
class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = [
            "id",
            'room',
            'description',
            'status',
        ]


# Event Serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            'building',
            'name',
            'description',
            'event_date',
        ]


# Communication Serializer
class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = [
            "id",
            'title',
            'message',
            'students',
        ]

