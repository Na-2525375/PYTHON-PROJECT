"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from.views import *


              
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', homePage,name="homePageUrl"),
    path('studentPage', studentPage,name="studentPageUrl"),
    path('teacherPage', teacherPage,name="teacherPageUrl"),
    path('employeePage',employeePage,name="employeePageUrl"),
    path('authorityPage',authorityPage,name="authorityPageUrl"),
    path('libraryPage',libraryPage,name="libraryPageUrl"),
    path('',loginPage,name="loginPageUrl"),
    path('signupPage',signupPage,name="signupPageUrl"),
    
    

    
    path('studentAdd',studentAdd,name="studentAdd"),
    path('teacherAdd',teacherAdd,name="teacherAdd"),
    path('employeeAdd',employeeAdd,name="employeeAdd"),
    path('authorityAdd',authorityAdd,name="authorityAdd"),
    path('libraryAdd',libraryAdd,name="libraryAdd"),
    
    path('editStudent/<str:myid>',editStudent,name="editStudent"),
    path('deleteStudent/<str:myid>',deleteStudent,name="deleteStudent"),
    path('updateStudent',updateStudent,name="updateStudent"),
    
    path('editTeacher/<str:myid>',editTeacher,name="editTeacher"),
    path('deleteTeacher/<str:myid>',deleteTeacher,name="deleteTeacher"),
    path('updateTeacher',updateTeacher,name="updateTeacher"),
   
    path('editEmployee/<str:myid>',editEmployee,name="editEmployee"),
    path('deleteEmployee/<str:myid>',deleteEmployee,name="deleteEmployee"),
    path('updateEmployee',updateEmployee,name="updateEmployee"),
    
    path('editAuthority/<str:myid>',editAuthority,name="editAuthority"),
    path('deleteAuthority/<str:myid>',deleteAuthority,name="deleteAuthority"),
    path('updateAuthority',updateAuthority,name="updateAuthority"),
   
    
    path('editlibrary/<str:myid>',editlibrary,name="editlibrary"),
    path('deletelibrary/<str:myid>',deletelibrary,name="deletelibrary"),
    path('updatelibrary',updatelibrary,name="updatelibrary"),
    path('myprofile',myprofile,name="myprofile"),
       
       
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)