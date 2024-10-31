from django.contrib import admin
from .models import Building, Room ,RoomApplication, MaintenanceRequest, Event, Communication


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'capacity',
        'facilities',
        'date',
        'updated',
    )
    list_display_links = ('name', 'address')
    search_fields = ('name', 'capacity')
    readonly_fields = ("date", "updated")
    ordering = ('-id',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'room_number',
        'floor_number',
        'capacity',
        'building',
        'status',
        'room_type',
        'date',
        'updated',
    )
    list_display_links = ('room_number', 'floor_number')
    search_fields = ('room_number', 'floor_number')
    readonly_fields = ("date", "updated")
    ordering = ('-id',)

@admin.register(RoomApplication)
class RoomApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'room',
        'application_date',
        'status',
    )
    list_display_links = ('student', 'room', 'status')
    search_fields = ('student', 'room')
    readonly_fields = ("application_date",)
    ordering = ('-id',)

@admin.register(MaintenanceRequest)
class MaintenanceRequestnAdmin(admin.ModelAdmin):
    list_display = (
        'room',
        'status',
        'resolved_on',
        'date',
    )
    list_display_links = ('room', 'status')
    search_fields = ('room',)
    readonly_fields = ("date",)
    ordering = ('-id',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'building',
        'name',
        'event_date',
        'date',
    )
    list_display_links = ('building', 'name')
    search_fields = ('name',)
    readonly_fields = ("date", "updated")
    ordering = ('-id',)

@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'message',
        'date',
    )
    list_display_links = ('title',)
    search_fields = ('title',)
    readonly_fields = ("date", "updated")
    ordering = ('-id',)