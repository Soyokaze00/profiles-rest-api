from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile == request.user
    
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    
    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update thier own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
    