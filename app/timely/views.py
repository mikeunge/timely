from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def index(request):
	return render(request=request, template_name='timely/index.html', context={'page_title': 'Timely - Home'})


# TODO: get rid of the messages.info/messages.error
#		display the messages on the login page
def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		print(form)
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
	form = AuthenticationForm()
	return render(request=request, template_name='timely/login.html', context={'page_title': 'Timely - Login', 'login_form':form})