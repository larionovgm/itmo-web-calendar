from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user or request.user.is_staff
