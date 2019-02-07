from django.shortcuts import render, redirect, HttpResponse
import datetime
from .models import shows
from apps.l_r_app.models import users, ratings
from django.contrib import messages


def index(request):
    christmas_shows=shows.objects.all().order_by('air_date')
    context={'christmas_shows':christmas_shows}
    
    return render(request, 'shows_app/index.html',context)

def all_shows(request):
    return render(request,'shows_app/all.html')

def network(request,network):
    christmas_shows=shows.objects.filter(network=network)
    print(network)
    context={'christmas_shows':christmas_shows,'network':network}
    return render(request,'shows_app/network.html',context)
def city(request):
    christmas_shows=shows.objects.filter(theme='city')
    context={'christmas_shows':christmas_shows,}
    return render(request,'shows_app/themes/city.html',context)

def country(request):
    christmas_shows=shows.objects.filter(theme='country')
    context={'christmas_shows':christmas_shows,}
    return render(request,'shows_app/themes/country.html',context)

def syfy(request):
    christmas_shows=shows.objects.filter(theme='syfy/horror')
    context={'christmas_shows':christmas_shows,}
    return render(request,'shows_app/themes/syfy.html',context)

def add(request,id):
    errors={}
    if 'logged_in' not in request.session:
        errors['logged_in']='Please login or register to add to your watchlist'
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/christmas',{'errors':errors})
    user=users.objects.get(id=request.session['id'])
    show=shows.objects.get(id=id)
    user.show.add(show)
    return redirect(request.META.get('HTTP_REFERER', '/christmas'))

def remove(request,id):
    user=users.objects.get(id=request.session['id'])
    show=shows.objects.get(id=id)
    user.show.remove(show)
    return redirect(request.META.get('HTTP_REFERER', '/dashboard'))

def rate(request,id):
    errors={}
    if 'logged_in' not in request.session:
        errors['logged_in']='Please login or register to add to your watchlist'
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(request.META.get('HTTP_REFERER', '/christmas'),{'errors':errors})
    user=users.objects.get(id=request.session['id'])
    show=shows.objects.get(id=id)
    x=float(request.POST['rating'])
    ratings.objects.create(
        userid=user,
        showid=show,
        rating=x,
    )
    rate=ratings.objects.filter(showid=id)
    count=0
    sum=0
    print(rate.all())
    for i in rate:
        sum+=i.rating
        count+=1
    show.rate=(sum/count)
    show.save()
    rating=ratings.objects.filter(userid=request.session['id'])
    context={'rating':rating}
    return redirect(request.META.get('HTTP_REFERER', '/christmas'))