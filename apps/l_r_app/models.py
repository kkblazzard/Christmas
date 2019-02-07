from django.db import models
import bcrypt
import re	# the regex module
from apps.shows_app.models import shows
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX =re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
class validation_Manager(models.Manager):
    def registration(self,postdata):
        is_valid = True
        errors = {}
        email = users.objects.filter(email=postdata['email'])
        print(email)
        username = users.objects.filter(username=postdata['username'])
        if email: #if repeat has any value we know is_valid=False
            errors['email']='Email address already in use please login!' #alert user
            is_valid=False
        if email: #if repeat has any value we know is_valid=False
            errors['username']='Username address already in use please login!' #alert user
            is_valid=False
        if not EMAIL_REGEX.match(postdata['email']):    # test whether a field matches the pattern
            is_valid=False
            errors['invalid_email']='Invalid email address!'
        if not PASSWORD_REGEX.match(postdata['password']):    # test whether a field matches the pattern
            is_valid=False
            errors['password']='Minimum eight characters, at least one uppercase letter, one lowercase letter and one number:!'
        if len(postdata['fname']) < 2:
            is_valid = False
            errors['fname']='First name must contain at least 2 characters!'# display validation error
        if len(postdata['lname']) < 2:
            is_valid = False
            errors['lname']='Last name must contain at least 2 characters!'# display validation error
        if len(postdata['email']) < 7:
            is_valid = False
            errors ['email']='Email must contain at least 8 characters!'# display validation error
        if postdata['password']!= postdata['confirmpw']:
            is_valid=False
            errors['password_miss_match']='Passwords did not match!'
        if is_valid:  #if not '_flashes' in request.session.keys():	# there are no errors
            # add user to database 
            hash1= bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt())
            new_user = users.objects.create(
                username= postdata['username'],
                password = hash1, 
                fname = postdata['fname'],
                lname = postdata['lname'],
                email = postdata['email'])
            #log user in
            return 
            
        return errors
            # never render on a post, always redirect!
    
    def login(self,postdata):
            errors = {}
            try: 
                existing = users.objects.get(email=postdata['email'])
            # if we get True after checking the password, we may put the user id in request.session
                if bcrypt.checkpw(postdata['password'].encode(), existing.password.encode()):
                    return True
                else:
                    errors['login fail']='Incorrect Email or Password'
                    return errors
            except:
                print("login failed ")
                    # if we didn't find anything in the database by searching by username or if the passwords don't match,
                    # throw an error message and redirect back to a safe route
                errors['login_error']='You could not be logged in'
                return errors

class update_Manager(models.Manager):
    def user_update(self,postdata):
        is_valid = True
        errors = {}
        email = users.objects.filter(email=postdata['email'])
        print(email)
        username = users.objects.filter(username=postdata['username'])
        if email: #if repeat has any value we know is_valid=False
            errors['email']='Email address already in use please login!' #alert user
            is_valid=False
        if not EMAIL_REGEX.match(postdata['email']):    # test whether a field matches the pattern
            is_valid=False
            errors['invalid_email']='Invalid email address!'
        if len(postdata['fname']) < 2:
            is_valid = False
            errors['fname']='First name must contain at least 2 characters!'# display validation error
        if len(postdata['lname']) < 2:
            is_valid = False
            errors['lname']='Last name must contain at least 2 characters!'# display validation error
        if len(postdata['email']) < 7:
            is_valid = False
            errors ['email']='Email must contain at least 8 characters!'# display validation error
        if is_valid:  #if not '_flashes' in request.session.keys():	# there are no errors
            # add user to database 
            updated =users.objects.get(id=id)
            updated.fname = postdata['fname']
            updated.lname = postdata['lname']
            updated.email = postdata['email']
            #log user in
        return errors

class users(models.Model):
    username= models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    fname = models.CharField(max_length=45)
    lname=models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    watchlist=[]
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=validation_Manager()
    show = models.ManyToManyField(shows, related_name="users")

class ratings(models.Model):
    userid=models.ForeignKey(users, related_name="rating")
    showid=models.ForeignKey(shows, related_name="rating")
    rating=models.FloatField(default=0)