from django.db import models
from django.contrib.auth import get_user_model
from .constants import RoomConstants


class Building(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    description = models.TextField(null=True, blank=True)
    capacity = models.IntegerField()
    facilities = models.TextField(null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Building"
        verbose_name_plural = "Buildings"
        ordering = ["id"]


class Room(models.Model):
    room_number = models.CharField(max_length=255, unique=True)
    floor_number = models.CharField(max_length=50)
    capacity = models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="room_building", null=False)
    status = models.CharField(max_length=50, choices=RoomConstants.STATUS_CHOICES)
    room_type = models.CharField(max_length=50, choices=RoomConstants.ROOM_TYPES, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_number

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["id"]


class RoomApplication(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="student_room_applications")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_applications")
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"{self.student} applied for {self.room}"

    class Meta:
        verbose_name = "Room Application"
        verbose_name_plural = "Room Applications"
        ordering = ["-id"]


class MaintenanceRequest(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="maintenance_requests")
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending')
    resolved_on = models.DateTimeField(auto_now=True)

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request for {self.room} on {self.date}"

    class Meta:
        verbose_name = "Maintenance Request"
        verbose_name_plural = "Maintenance Requests"
        ordering = ["-id"]


class Event(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    event_date = models.DateField()

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["-id"]


class Communication(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    students = models.ManyToManyField(get_user_model(), related_name="communications")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Communication"
        verbose_name_plural = "Communications"
        ordering = ["-id"]
