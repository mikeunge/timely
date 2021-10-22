from datetime import datetime, date
from django.http import JsonResponse
from .models import Timer


def get_total_time(response, user=-1, json=True):
    try:
        timer = Timer.objects.get(user_id=user, is_running=True)
    except:
        if json:
            return JsonResponse({'message': 'No running timer'})
        return Null
    # Calculate the difference between start and end.
    today = date.today()
    timer_end = datetime.now().time()
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


def update_total_time(user_id):
    pass
