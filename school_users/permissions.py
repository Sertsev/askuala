from rest_framework.permissions import BasePermission, IsAuthenticated


class IsGuest(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            if request.user.user_type == 'guest':
                return super().has_permission(request, view)


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            if request.user.user_type == 'student':
                return super().has_permission(request, view)


class IsLecturer(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            if request.user.user_type == 'lecturer':
                return super().has_permission(request, view)


class IsRegistrar(BasePermission):
    def has_permission(self, request, view):
        if bool(request.user and request.user.is_authenticated):
            if request.user.user_type == 'registrar':
                return super().has_permission(request, view)
