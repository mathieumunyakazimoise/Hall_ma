from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    """
    Custom permission to allow only students to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'

class IsAdministrator(permissions.BasePermission):
    """
    Custom permission to allow only administrators to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'administrator'

class IsAdministratorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow administrators full access, and others read-only access.
    """
    def has_permission(self, request, view):
        # Allow read-only for non-administrators
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow administrators to write (POST, PUT, DELETE, etc.)
        return request.user.is_authenticated and request.user.role == 'administrator'



