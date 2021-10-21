from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from datetime import datetime, date
from .forms import LoginForm
from .decorators import logged_in
from .models import Timer


@logged_in
def index(request):
    try:
        ok = Timer.objects.get(user_id=request.user.id, is_running=True)
        timer_state = True
        timer_link = 'timer/stop'
    except:
        timer_state = False
        timer_link = 'timer/start'
    variables = {
        'page_title': 'Timely - Home',
        'timer_state': timer_state,
        'timer_link': timer_link
    }
    return render(request, 'timely/index.html', variables)


@logged_in
def timer_start(request):
    # start a new timer
    try:
        Timer.objects.get(user_id=request.user.id, is_running=True)
        redirect('/')
    except:
        pass
    timer = Timer(
        user_id=request.user.id,
        type='wo',
        time_total=0
    )
    timer.save()
    return redirect('/')


@logged_in
def timer_stop(request):
    # stop curent timer
    try:
        timer = Timer.objects.get(user_id=request.user.id, is_running=True)
    except:
        redirect('/')
    # Calculate the difference between start and end.
    today = date.today()
    timer_end = datetime.now().time()
    start = datetime.combine(today, timer.start_time).replace(microsecond=0)
    end = datetime.combine(today, timer_end).replace(microsecond=0)
    diff = end - start
    # Update the timer object.
    Timer.objects.filter(
        user_id=request.user.id,
        is_running=True
    ).update(
        is_running=False,
        time_total=diff,
        stop_time=timer_end
    )
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
