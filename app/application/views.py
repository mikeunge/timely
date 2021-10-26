from django.shortcuts import render, redirect
from timely.decorators import logged_in


# Create your views here.
@logged_in
def application(request):
    return render(request, 'application/index.html')


@logged_in
def view_all(request):
    return redirect('/application/') 
