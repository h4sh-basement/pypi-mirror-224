from django.core.exceptions import PermissionDenied
from functools import wraps

OBJECT_ARRAY = [
    "change_task",
    "customer",
    "kanban",
    "kanban_board",
    "kanban_card",
    "requirement",
    "requirement_item",
    "request_for_change",
    "organisation",
    "project",
    "task",
]


def check_destination():
    """
    Does a quick check to make sure the destination variable is inside the OBJECT_ARRAY
    If not - it will return a Permission Denied. i.e. object does not exist do nothing.
    """
    def decorator(func):
        @wraps(func)
        def inner(request, destination, *args, **kwargs):
            # See if the destination is correct (permission denied if not).
            if destination not in OBJECT_ARRAY:
                raise PermissionDenied

            # It passed - return the function
            return func(request, destination, *args, **kwargs)

        return inner

    return decorator
