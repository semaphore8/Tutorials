from rest_framework import permissions

class IsAssigned(permissions.BasePermission):
    """
    Only person who assigned has permission
    """

    def has_object_permission(self, request, view, obj):
        if obj.assigned_to == request.user:
            return True
        else:
            return False