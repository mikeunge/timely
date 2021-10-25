from django.shortcuts import render, redirect

def stats_base(request):
    return render(request, 'statistic/index.html')
