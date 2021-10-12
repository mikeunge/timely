from django.http import HttpResponse
from django.shortcuts import redirect


# logged_in :: make sure a user is logged in.
# 
# Add this decorator over pages that do need a logged in user.
# This does not have anything to do with superuser settings or group rules.
def logged_in(view):
	def wrapper(request, *args, **kwargs):
		if request.user.is_authenticated:
			return view(request, *args, **kwargs)
		return redirect('/accounts/login/')
	return wrapper