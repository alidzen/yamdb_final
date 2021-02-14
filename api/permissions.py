from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)


class IsAdminRole(IsAuthenticated):
    def has_permission(self, request, view):
        return (
            super().has_permission(request, view)
            and request.user.is_admin
        )


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class RetrieveOnlyOrHasCUDPermissions(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True

        request_user = request.user
        return (
            request_user.is_admin
            or request_user.is_moderator
            or request_user == obj.author
        )
