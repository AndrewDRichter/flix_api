from rest_framework.permissions import BasePermission


class GenrePermissionClass(BasePermission):
    def has_permission(self, request, view):
        return True