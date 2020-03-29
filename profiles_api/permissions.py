from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            # safe method means request is not to make a modification (e.g, GET request)
            return True

        # only allow modification (update, delete) if user making request
        # is current user
        return obj.id == request.user.id    
