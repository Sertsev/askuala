from rest_framework import permissions


class IsRegistrarOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if self.request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and (request.user.user_type == 'registrar' or request.user.is_staff))
