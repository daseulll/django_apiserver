from rest_framework import permissions

class IsAuthorUpdateOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
        # True가 리턴되면 permission이 허용       
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True    
        if (request.method == 'DELETE'):
            return request.user.is_superuser
        return obj.author == request.user