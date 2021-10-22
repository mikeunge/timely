from datetime import datetime, date
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Timer, UserSettings


def settings_show_seconds(response=None, user=-1):
    try:
        settings = UserSettings.objects.get(user_id=user)
        return settings.timer_seconds
    except:
        return None

# get_total_time :: calculate and return the total time
def get_total_time(response=None, user=-1, json=True, db_call=False):
    try:
        timer = Timer.objects.get(user_id=user, is_running=True)
    except:
        if json:
            return JsonResponse({'message': 'No running timer'})
        return None

    if not db_call:
        seconds = settings_show_seconds(user=user)
    else:
        seconds = True

    # check if the stop time differs from the start time
    # if not, we take now from time, else, we take the timers stop time
    start_time = timer.start_time.replace(microsecond=0)
    stop_time = timer.stop_time.replace(microsecond=0)
    today = date.today()
    if  stop_time == start_time:
        timer_end = datetime.now().time()
    else:
        timer_end = timer.stop_time

    # Calculate the difference between start and end.
    start = datetime.combine(today, start_time)
    end = datetime.combine(today, timer_end).replace(microsecond=0)
    time = end - start

    # if the timer runs till the next day, the diff prefixes with "-1 day"
    # to overcome this, we simply split the string and take the second array item.
    timeSplit = str(time).split(', ')
    if len(timeSplit) > 1:
        time = timeSplit[1]

    # get rid of the seconds
    timeArr = str(time).split(':')
    hours = timeArr[0]
    if len(str(hours)) < 2:
        hours = f'0{str(hours)}'
    minutes = timeArr[1]
    time = f'{hours}:{minutes}:{timeArr[2]}' if seconds else f'{hours}:{minutes}'

    if json:
        return JsonResponse({'message': f'{time}'})
    return time

