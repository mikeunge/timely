from datetime import datetime, date
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Timer


# get_total_time :: calculate and return the total time
def get_total_time(response=None, user=-1, json=True):
    try:
        timer = Timer.objects.get(user_id=user, is_running=True)
    except:
        if json:
            return JsonResponse({'message': 'No running timer'})
        return None

# TODO: this breaks the counter function ...
    # check if the stop time differs from the start time
    # if not, we take now from time, else, we take the timers stop time
    if timer.stop_time == timer.start_time:
        timer_end = datetime.now().time()
    else:
        timer_end = timer.stop_time
    today = date.today()
    # Calculate the difference between start and end.
    start = datetime.combine(today, timer.start_time).replace(microsecond=0)
    end = datetime.combine(today, timer_end).replace(microsecond=0)
    diff = end - start

    # if the timer runs till the next day, the diff prefixes with "-1 day"
    # to overcome this, we simply split the string and take the second array item.
    dSplit = str(diff).split(', ')
    if len(dSplit) > 1:
        diff = str(diff).split(', ')[1]

    # format the hours to be two digits
    hours = str(diff).split(':')[0]
    if len(str(hours)) < 2:
        hours = f'0{str(hours)}'
    minutes = str(diff).split(':')[1]
    time = f'{hours}:{minutes}'
    if json:
        return JsonResponse({'message': f'{time}'})
    return time


# get_username :: get the username according to the users id
def get_username(user_id):
    return User.objects.get(pk=user_id)
