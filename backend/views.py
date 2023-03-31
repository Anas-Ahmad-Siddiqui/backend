from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from backend.models import UserStudents, UserTeachers, Class
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
def signup_student(request):
    if request.method == 'GET':
        return HttpResponse("Hello World")
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            username = body["username"]
            checkUsername = UserStudents.objects.filter(
                username=username).values()

            if (len(checkUsername) == 0):
                newUser = UserStudents()
                newUser.username = username
                newUser.first_name = body["first_name"]
                newUser.last_name = body["last_name"]
                newUser.email = body["email"]
                newUser.classes = []
                newUser.password = hashlib.sha256(
                    body["password"].encode()).hexdigest()

                newUser.save()

                response = HttpResponse(json.dumps({"id": newUser.id}))
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
def loginStudent(request):
    if (request.method == 'GET'):
        return HttpResponse("Login exists here")

    elif (request.method == 'POST'):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username = body["username"]
        password = body["password"]

        passwordHash = hashlib.sha256(password.encode()).hexdigest()

        response = HttpResponse("Logged in")
        response.status_code = 200

        user = UserStudents.objects.filter(username=username).values()
        password = user[0]["password"]

        if (password == passwordHash):
            logCode = random.randint(100, 10000000)
            loggedUser = UserStudents.objects.get(username=username)
            loggedUser.logCode = logCode
            loggedUser.logStatus = True
            loggedUser.save()

            response = HttpResponse(json.dumps({"id":loggedUser.id, "logCode": logCode}))
            response.status_code = 200
            return response

        else:
            response = HttpResponse("Password doesn't match")
            response.status_code = 500
            return response


@csrf_exempt
def logoutStudent(request):
    if (request.method == 'GET'):
        return HttpResponse("Log out exists here")

    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username = body["username"]
        logCode = body["logCode"]

        user = UserStudents.objects.filter(username=username).values()

        existingLogCode = user[0]["logCode"]

        if (logCode == existingLogCode):
            user = UserStudents.objects.get(username=username)
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
def displayStudent(request):
    if (request.method == 'GET'):
        return HttpResponse("Delete exists here")

    elif (request.method == 'POST'):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usernames = body["usernames"]

        userDetails = []

        for username in usernames:
            user = UserStudents.objects.filter(username=username).values()
            userDetails.append(user[0])
            print(user[0])

        response = HttpResponse(userDetails)
        response.status_code = 200
        return response


@csrf_exempt
def deleteStudent(request):
    if (request.method == 'GET'):
        return HttpResponse("Delete exists here")

    elif (request.method == 'POST'):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usernames = body["usernames"]

        for username in usernames:
            user = UserStudents.objects.get(username=username)
            user.delete()
        response = HttpResponse("Deleted")
        response.status_code = 200
        return response


#######################################################################

@csrf_exempt
def signup_teacher(request):
    if request.method == 'GET':
        return HttpResponse("Hello World")
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            username = body["username"]
            checkUsername = UserTeachers.objects.filter(
                username=username).values()

            if (len(checkUsername) == 0):
                newUser = UserTeachers()
                newUser.username = username
                newUser.first_name = body["first_name"]
                newUser.last_name = body["last_name"]
                newUser.email = body["email"]
                newUser.classes = []
                newUser.password = hashlib.sha256(
                    body["password"].encode()).hexdigest()

                newUser.save()

                response = HttpResponse(json.dumps({"id": newUser.id}))
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
def loginTeacher(request):
    if (request.method == 'GET'):
        return HttpResponse("Login exists here")

    elif (request.method == 'POST'):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username = body["username"]
        password = body["password"]

        passwordHash = hashlib.sha256(password.encode()).hexdigest()

        response = HttpResponse("Logged in")
        response.status_code = 200

        user = UserTeachers.objects.filter(username=username).values()
        password = user[0]["password"]

        if (password == passwordHash):
            logCode = random.randint(100, 10000000)
            loggedUser = UserTeachers.objects.get(username=username)
            loggedUser.logCode = logCode
            loggedUser.logStatus = True
            loggedUser.save()

            response = HttpResponse(json.dumps({"id": loggedUser.id, "logCode": logCode}))
            response.status_code = 200
            return response

        else:
            response = HttpResponse("Password doesn't match")
            response.status_code = 500
            return response


@csrf_exempt
def logoutTeacher(request):
    if (request.method == 'GET'):
        return HttpResponse("Log out exists here")

    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username = body["username"]
        logCode = body["logCode"]

        user = UserTeachers.objects.filter(username=username).values()

        existingLogCode = user[0]["logCode"]

        if (logCode == existingLogCode):
            user = UserTeachers.objects.get(username=username)
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
def displayTeacher(request):
    if (request.method == 'GET'):
        return HttpResponse("Delete exists here")

    elif (request.method == 'POST'):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usernames = body["usernames"]

        userDetails = []

        for username in usernames:
            user = UserTeachers.objects.filter(username=username).values()
            userDetails.append(user[0])
            print(user[0])

        response = HttpResponse(userDetails)
        # response.header("Access-Control-Allow-Origin", "true");
        response.status_code = 200
        return response


@csrf_exempt
def deleteTeacher(request):
    if (request.method == 'GET'):
        return HttpResponse("Delete exists here")

    elif (request.method == 'POST'):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        usernames = body["usernames"]

        for username in usernames:
            user = UserTeachers.objects.get(username=username)
            user.delete()
        response = HttpResponse("Deleted")
        response.status_code = 200
        return response
    
@csrf_exempt
def insertClassStudent(request):
    if (request.method == 'GET'):
        return HttpResponse("Classes can be inserted into student here")
    
    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username = body["username"]
        classes = body["classes"]

        user = UserStudents.objects.get(username = username)
        
        # lst = user.classes
        user.classes.extend(classes)

        user.save()

        response = HttpResponse("Added into class")
        response.status_code = 200

        return response


@csrf_exempt
def insertStudentsIntoClass(request):
    if (request.method == 'GET'):
        return HttpResponse("Students can be inserted into class from here")
    
    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        classID = body["id"]
        usernames = body["usernames"]
        clas = Class.objects.get(classId = classID)

        for username in usernames:
            user = UserStudents.objects.get(username = username)
            user.classes.extend([classID])
            user.save()

            clas.students.extend([user.id])


        clas.save()

        response = HttpResponse("Students added into class and Class added into students")
        response.status_code = 200

        return response



@csrf_exempt
def addClassToTeacher(request):
    if (request.method == 'GET'):
        return HttpResponse("teacher can add class to themselves")
    
    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8'  )
        body = json.loads(body_unicode)

        username = body["username"]
        classes = body["classes"]
        
        user = UserTeachers.objects.get(username = username)
        
        # lst = user.classes
        user.classes.extend(classes)

        user.save()

        response = HttpResponse("Added class to teacher")
        response.status_code = 200

        return response

@csrf_exempt
def createClass(request):
    if (request.method == 'GET'):
        return HttpResponse("Class created here")
    
    elif (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8'  )
        body = json.loads(body_unicode)

        className = body["className"]

        clas = Class()
        clas.className = className
        clas.students = []
        clas.save()

        # clas = Class.objects.all().last()
        print(clas.classId)
        response = HttpResponse(json.dumps({"classId":clas.classId}))
        response.status_code = 200

        return response
