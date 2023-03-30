"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.check),
    path('signupStudent/', views.signup_student),
    path('loginStudent/', views.loginStudent),
    path('logoutStudent/', views.logoutStudent),
    path('deleteStudent/', views.deleteStudent),
    path('displaystudent/', views.displayStudent),
    path('signupTeacher/', views.signup_teacher),
    path('loginTeacher/', views.loginTeacher),
    path('logoutTeacher/', views.logoutTeacher),
    path('displayTeacher/', views.displayTeacher),
    path('deleteTeacher/', views.deleteTeacher),
    path('inClassStudent/', views.insertClassStudent),
    path('inStudentsClass/', views.insertStudentsIntoClass),
    path('inClassTeaher/', views.addClassToTeacher),
    path('createClass/', views.createClass)
]
