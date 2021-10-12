from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm


def index(request):
	variables = {
		'page_title': 'Timely - Home'
	}
	return render(request, 'timely/index.html', variables)


# TODO: get rid of the messages.info/messages.error
#		display the messages on the login page
def login_user(request):
	if request.user.is_authenticated:
		redirect('/')

	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f'You are now logged in as {username}.')
				return redirect('/')
			else:
				messages.error(request, 'Invalid username or password.')
		else:
			messages.error(request, 'Invalid username or password.')

	variables = {
		'page_title': 'Timely - Login',
		'form':form
	}
	return render(request, 'timely/login.html', variables)


def logout_user(request):
    logout(request)
    return redirect('/login')