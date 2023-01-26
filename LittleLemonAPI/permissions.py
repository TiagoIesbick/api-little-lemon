from rest_framework import permissions


def is_manager_or_superuser(user):    
    return (user.groups.filter(name='Manager').exists() | user.is_superuser)

def is_delivery_crew(user):
    return user.groups.filter(name='Delivery crew').exists()


class IsManagerOrSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user        
        return is_manager_or_superuser(user)          
        