from rest_framework.throttling import UserRateThrottle

class ManagerThrottle(UserRateThrottle):
    scope = 'manager'