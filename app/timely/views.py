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
        if Timer.objects.get(user_id=request.user.id, is_running=True):
            timer_state = True
    except MultipleObjectsReturned:
        messages.error(request, 'You have currently more than one timer running. Please inform your administrator about this incident!')
        timer_state = False
    except ObjectDoesNotExist:
        timer_state = False
    variables = {
        'page_title': 'Timely - Home',
        'timer_state': timer_state,
    }
    return render(request, 'timely/index.html', variables)

# --- TIMER ---

@logged_in
def timer_start(request, method=''):
    try:
        if Timer.objects.get(user_id=request.user.id, is_running=True):
            raise MultipleObjectsReturned
    except MultipleObjectsReturned:
        messages.info(request, 'You already have a running timer.')
        return redirect('/')
    except ObjectDoesNotExist:
        if method != 'work' and method != 'break':
            messages.error(request, f'Timer method ({method}) is not allowed!')
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
        Timer.objects.get(user_id=request.user.id, is_running=True)
    except ObjectDoesNotExist:
        messages.info(request, 'You need a timer before you can stop one.')
        return redirect('/')
    # Calculate the difference between start and end.
    timer_end = datetime.now().time()
    total_time = get_total_time(user=request.user.id, json=False, db_call=True)
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


# --- ACCOUNTS ---

@logged_in
def settings(request):
    variables = {
        'page_title': 'Timely - Setting'
    }
    return render(request, 'timely/accounts/settings.html', variables)


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
