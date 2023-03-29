from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from backend.models import User 
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json
import random

@csrf_exempt 
def check(request):
    if request.method == 'GET':
        return HttpResponse("Hello World")  
    if request.method == 'POST':
        return HttpResponse("Hello World") 

@csrf_exempt 
def signup(request):
    if request.method == 'GET':
        return HttpResponse("Hello World")  
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            
            username = body["username"]
            checkUsername = User.objects.filter(username=username).values()

            if(len(checkUsername) == 0):
                newUser = User()
                newUser.username = username
                newUser.first_name = body["first_name"]
                newUser.last_name = body["last_name"]
                newUser.email = body["email"]
                newUser.isTeacher = body["isTeacher"]
                newUser.password = hashlib.sha256(body["password"].encode()).hexdigest()

                newUser.save()

                response = HttpResponse("Successfully signed up")
                response.status_code = 200
                return response
            
            else:
                response = HttpResponse("Username already exists")
                response.status_code = 500
                return response
            
        except Exception as e:
            response = HttpResponse(e)
            response.status_code = 500
            return response
        
@csrf_exempt 
def login(request):
    if(request.method == 'GET'):
        return HttpResponse("Login exists here")
    
    elif(request.method == 'POST'):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        username = body["username"]
        password = body["password"]

        passwordHash = hashlib.sha256(password.encode()).hexdigest()

        response = HttpResponse("Logged in")
        response.status_code = 200

        user = User.objects.filter(username=username).values()
        password = user[0]["password"]

        if(password == passwordHash):
            logCode = random.randint(100, 10000000)
            loggedUser = User.objects.get(username=username)
            loggedUser.logCode = logCode
            loggedUser.logStatus = True
            loggedUser.save()

            response = HttpResponse(json.dumps({"logCode": logCode}))
            response.status_code = 200
            return response 

        else:
            response = HttpResponse("Password doesn't match")
            response.status_code = 500
            return response
        
@csrf_exempt 
def logout(request):
    if(request.method == 'GET'):
        return HttpResponse("Log out exists here")
    
    elif(request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username = body["username"]
        logCode = body["logCode"]

        user = User.objects.filter(username=username).values()
        
        existingLogCode = user[0]["logCode"]

        if(logCode == existingLogCode):
            user = User.objects.get(username=username)
            user.logCode = -1
            user.logStatus = False
            user.save()

            response = HttpResponse("Logged Out")
            response.status_code = 200
            return response
        
        else:
            response = HttpResponse("Invalid Request")
            response.status_code = 500
            return response


@csrf_exempt 
def display(request):
    if(request.method == 'GET'):
        return HttpResponse("Delete exists here")
    
    elif(request.method == 'POST'):
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usernames = body["usernames"]

        userDetails = []

        for username in usernames:
            user = User.objects.filter(username=username).values()
            userDetails.append(user[0])
            print(user[0])

        response = HttpResponse(userDetails)
        response.status_code = 200
        return response

@csrf_exempt 
def delete(request):
    if(request.method == 'GET'):
        return HttpResponse("Delete exists here")
    
    elif(request.method == 'POST'):
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usernames = body["usernames"]

        for username in usernames:
            user = User.objects.get(username=username)
            user.delete()
        response = HttpResponse("Deleted")
        response.status_code = 200
        return response
