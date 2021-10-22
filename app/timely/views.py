from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db import models
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.contrib import messages
from datetime import datetime, date
from .forms import LoginForm
from .decorators import logged_in
from .models import Timer
from .services import get_total_time


@logged_in
def index(request):
    try:
        timer = Timer.objects.get(user_id=request.user.id, is_running=True)
        timer_state = True
    except:
        timer_state = False
    variables = {
        'page_title': 'Timely - Home',
        'timer_state': timer_state,
    }
    return render(request, 'timely/index.html', variables)


@logged_in
def timer_start(request, method=''):
    try:
        if Timer.objects.get(user_id=request.user.id, is_running=True):
            raise MultipleObjectsReturned
    except MultipleObjectsReturned:
        messages.error(
            request, "Sorry, but we cannot create a new timer when you have one already running")
        return redirect('/')
    except ObjectDoesNotExist:
        if method != 'work' and method != 'break':
            return redirect('/')

    timer = Timer(
        user_id=request.user.id,
        type=method,
        time_total=0
    )
    timer.save()
    return redirect('/')


@logged_in
def timer_stop(request):
    try:
        timer = Timer.objects.get(user_id=request.user.id, is_running=True)
    except:
        return redirect('/')
    # Calculate the difference between start and end.
    timer_end = datetime.now().time()
    total_time = get_total_time(user=request.user.id, json=False)
    # Update the timer object.
    Timer.objects.filter(
        user_id=request.user.id,
        is_running=True
    ).update(
        is_running=False,
        time_total=total_time,
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
            messages.success(
                request, 'Your password was successfully updated!')
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
                messages.error(
                    request, "Sorry, we cound't find a user with that username and password. Try it again, or maybe you forgot your password?")
        else:
            messages.error(
                request, 'Hmm... Something went wrong with your form. Please try again, we are trying to get it this time.')

    variables = {
        'page_title': 'Timely - Login',
        'form': form
    }
    return render(request, 'timely/accounts/login.html', variables)
