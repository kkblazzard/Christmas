from django.shortcuts import render, redirect
from django.contrib import messages
from .models import users
from datetime import datetime
from apps.shows_app.models import shows
# from app2.models import app2
import bcrypt
import re	# the regex module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX =re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

# Create your views here.
def home_page(request):
    request.session.clear()
    return redirect('/christmas')
def register(request):
    return render(request,'l_r_app/register.html')

def login(request): # see if the username provided exists in the database
    request.session['logged_in'] = False
    errors=users.objects.login(request.POST)
    request.session['logged_in']=errors
    if request.session['logged_in'] !=True:
        info=request.POST #used to repop the fields
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register',{'info':info})# redirect if errors.
    else:
        errors={}
        person=users.objects.get(email=request.POST['email'])
        request.session['fname']=person.fname
        request.session['lname']=person.lname
        request.session['email']=person.email
        request.session['id']=person.id
        request.session['logged_in']=True
        request.session['username']=person.username
        # never render on a POST, always redirect!
        errors['success']="You have sucessfully logged in"
        return redirect('dashboard/')
    return redirect("/register")            

def process(request):
    # To generate a hash, provide the password to be hashed as an argument
    # bcrypt.generate_password_hash(password_string)
    # To compare passwords, provide the hash as the first argument and the password to be checked as the second argument
    # bcrypt.check_password_hash(hashed_password, password_string)
    request.session['logged_in'] = False
    errors=users.objects.registration(request.POST)
    if errors:
        info=request.POST
        new_user=request.POST #saving info to repop the fields
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register',{'info':info})# redirect if errors.{'new_user':new_user},{'info':info}

    else:
        person=users.objects.get(email=request.POST['email'])
        request.session['fname']=person.fname
        request.session['lname']=person.fname
        request.session['email']=person.email
        request.session['id']=person.id
        request.session['logged_in']=True
        request.session['username']=person.username
        return redirect('/dashboard')
    

def dashboard(request): #pass variable from url page'name'
    errors={}
    if not 'logged_in' in request.session:
        request.session['logged_in']=False
        errors['not_logged_in'] ='Please login or register'
        context={'errors':errors}
        return redirect('/register',context)
    if request.session['logged_in'] !=True:
        errors['login_error']=(request, "You have not logged in")
        return redirect('/register',{'errors':errors})
    
    for key, value in errors.items():
            messages.error(request, value)
    today = datetime.now().date()
    user=users.objects.get(id=request.session['id'])
    watchlist=shows.objects.filter(users=user)#.order_by(air_date)
    # past_shows=shows.objects.filter(users=user)
    context={'user':user, 'watchlist':watchlist, }
    return render(request,'l_r_app/dashboard.html',context)

def edit(request,id):
    # is_valid = True
    # errors = {}
    # email = users.objects.filter(email=POSTdata['email'])
    # print(email)
    # username = users.objects.filter(username=POSTdata['username'])
    # if email: #if repeat has any value we know is_valid=False
    #     errors['email']='Email address already in use please login!' #alert user
    #     is_valid=False
    # if not EMAIL_REGEX.match(POSTdata['email']):    # test whether a field matches the pattern
    #     is_valid=False
    #     errors['invalid_email']='Invalid email address!'
    # if not PASSWORD_REGEX.match(POSTdata['password']):    # test whether a field matches the pattern
    #     is_valid=False
    #     errors['password']='Minimum eight characters, at least one uppercase letter, one lowercase letter and one number:!'
    # if len(POSTdata['fname']) < 2:
    #     is_valid = False
    #     errors['fname']='First name must contain at least 2 characters!'# display validation error
    # if len(POSTdata['lname']) < 2:
    #     is_valid = False
    #     errors['lname']='Last name must contain at least 2 characters!'# display validation error
    # if len(POSTdata['email']) < 7:
    #     is_valid = False
    #     errors ['email']='Email must contain at least 8 characters!'# display validation error
    # if POSTdata['password']!= POSTdata['confirmpw']:
    #     is_valid=False
    # if is_valid:  #if not '_flashes' in request.session.keys():	# there are no errors
    #     # add user to database 
    #     updated_user =users.objects.get(id=id)
    #     updated_user.fname = POSTdata['fname']
    #     updated_user.lname = POSTdata['lname']
    #     updated_user.email = POSTdata['email']
    # context ={'errors':errors}    #log user in
    return render(request,'l_r_app/edit.html')

def update(request,id):
    errors={}
    if request.session['logged_in'] !=True:
        errors['login_error']=(request, "You have not logged in")
        return redirect('/',{'errors':errors})
    user=users.objects.get(id=id)
    user.fname=request.POST['fname']
    user.lname=request.POST['lname']
    user.email=request.POST['email']
    user.save()
    request.session['fname']=user.fname
    request.session['lname']=user.lname
    request.session['email']=user.email
    errors['success']='Your information has been updated successfully'
    for key, value in errors.items():
            messages.error(request, value)
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    request.session['logged_in']=False
    return redirect('/christmas')

def delete_user_from_db(request,id):
    user=users.objects.get(id=id)
    user.delete()

    return redirect('/register')
