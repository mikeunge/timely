from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import LoginForm
from .decorators import logged_in
from .models import Timer


@logged_in
def index(request):
	variables = {
		'page_title': 'Timely - Home'
	}
	return render(request, 'timely/index.html', variables)


@logged_in
def timer_start(request):
    # start a new timer
    return redirect('/')


@logged_in
def timer_stop(request):
    # stop curent timer
    return redirect('/')


@logged_in
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('/')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	
	variables = {
		'page_title': 'Timely - Logout',
		'form': form
	}
	return render(request, 'timely/accounts/change_password.html', variables)


@logged_in
def signout(request):
    logout(request)
    return redirect('/accounts/login/')


def signin(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.error(request, "Sorry, we cound't find a user with that username and password. Try it again, or maybe you forgot your password?")
		else:
			messages.error(request, 'Hmm... Something went wrong with your form. Please try again, we are trying to get it this time.')

	variables = {
		'page_title': 'Timely - Login',
		'form':form
	}
	return render(request, 'timely/accounts/login.html', variables)
