from rest_framework import permissions


class IsRegistrarOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif bool(request.user and request.user.is_authenticated):
            if request.user.user_type == True:
                return True
        return bool(request.user and request.user.is_staff)
