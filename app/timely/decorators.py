from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


# logged_in :: make sure a user is logged in.
# 
# Add this decorator over pages that do need a logged in user.
# This does not have anything to do with superuser settings or group rules.
def logged_in(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view(request, *args, **kwargs)
        # TODO: the messages.error() creates 2 messages instead of one... does the wrapper get called twice?
        messages.error(request, 'You need to be logged in before visiting this page.')
        return redirect('/accounts/login/')
    return wrapper


def is_moderator(user):
    return user.groups.filter(name='Member').exists()

