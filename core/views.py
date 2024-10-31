from django.shortcuts import render
from .models import Building, Room, RoomApplication, MaintenanceRequest, Event, Communication
from .serializers import BuildingSerializer, RoomSerializer, RoomApplicationSerializer, MaintenanceRequestSerializer, EventSerializer, CommunicationSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .custom_pagination import CustomPageNumberPagination


class BuildingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Building.objects.all().order_by("id")
    serializer_class = BuildingSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        if not hasattr(self, "_queryset"):
            buildings = Building.objects.all().order_by("id")
            serialized_data = BuildingSerializer(buildings, many=True).data

            self._queryset = serialized_data
        return self._queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            return self.get_paginated_response(page)
        return Response(queryset)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BuildingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)


class RoomListCreateAPIView(generics.ListCreateAPIView):
    queryset = Room.objects.all().order_by("id")
    serializer_class = RoomSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        if not hasattr(self, "_queryset"):
            rooms = Room.objects.all().order_by("id")
            serialized_data = RoomSerializer(rooms, many=True).data

            self._queryset = serialized_data
        return self._queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            return self.get_paginated_response(page)
        return Response(queryset)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoomRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)


class RoomApplicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = RoomApplication.objects.all().order_by("id")
    serializer_class = RoomApplicationSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        if not hasattr(self, "_queryset"):
            room_applications = RoomApplication.objects.all().order_by("id")
            serialized_data = RoomApplicationSerializer(room_applications, many=True).data

            self._queryset = serialized_data
        return self._queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            return self.get_paginated_response(page)
        return Response(queryset)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoomApplicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomApplication.objects.all()
    serializer_class = RoomApplicationSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)


class MaintenanceRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    
class MaintenanceRequestDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class CommunicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer  
    
class CommunicationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer      
    