from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from myApp.models import *


def homePage(request):
   return render(request,"home.html")

def loginPage(request):
     myMessage={
        'Password_Error':'User Not Found',
        'Password_Success':'Login Successfully',
    }
    
     if request.method=="POST":

       user_name=request.POST.get("username")
       myPassword=request.POST.get("pass")
       
       print(user_name,myPassword)
       
       user=authenticate(request,username=user_name,password=myPassword)
       if user is not None:
           login(request,user)
           return redirect("homePageUrl")
       else:
           messages.warning(request,myMessage["Password_Error"])
           
       print(user)
    
     return render(request,"login.html")

def signupPage(request):
    
    myMessage={
        'Password_Error':'Password and Confirm Password Not Match',
        'Password_Success':'User Create Successfully',
    }
    if request.method=="POST":

       user_name=request.POST.get("username")
       myemail=request.POST.get("email")
       pass1=request.POST.get("password1")
       pass2=request.POST.get("password2")
       
       if pass1!=pass2:
           messages.error(request,myMessage['Password_Error'])
       else:
           myuser=User.objects.create_user(user_name,myemail,pass2)
           
           myuser.save()
           
           messages.success(request,myMessage['Password_Success'])
           
           return redirect("loginPageUrl")
       
    return render(request,"signup.html")

def myprofile(request):
   return render(request,"myprofile.html")



def studentPage(request):
    student = Students_Model.objects.all()

    context={
        "std":student,
    }

    return render(request,"student.html",context)


def teacherPage(request):

    teacher = Teachers_Model.objects.all()

    context={
        "tch":teacher,
    }

    return render(request,"teacher.html",context)


def employeePage(request):

    employee = Employees_Model.objects.all()

    context={
        "emp":employee,
    }

    return render(request,"employee.html",context)


def authorityPage(request):

    authority = Authority_Model.objects.all()

    context={
        "auth":authority,
    }

    return render(request,"authority.html",context)


def libraryPage(request):

    library = Library_Model.objects.all()

    context={
        "lib":library,
    }

    return render(request,"library.html",context)




#Student Page
def studentAdd(request):
    
    my_Message= {
        'Error_Message':'Student Add Failed',
        'Success_Message':'Student Add Successfully',
    }

    if request.method=="POST":

       f_name=request.POST.get("firstname")
       l_name=request.POST.get("lastname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")
       Profile_pic=request.FILES.get("Profile_pic")

       student=Students_Model(
        First_Name=f_name,
        Last_Name=l_name,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,
        myImage=Profile_pic

       )
       
       if Profile_pic:
           student.myImage=Profile_pic
       else:
           student.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg' 
              
       student.save()
       
       messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])
        
        return redirect("studentPageUrl")

    return render(request, "student.html")

#Teacher Page
def teacherAdd(request):
    
    my_Message= {
        'Error_Message':'Teacher Add Failed',
        'Success_Message':'Teacher Add Successfully',
    }

    if request.method=="POST":

        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        teacher=Teachers_Model(
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        
        if Profile_pic:
         teacher.myImage=Profile_pic
        else:
           teacher.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg' 
            
        teacher.save()
        messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])

        return redirect("teacherPageUrl")

    return render(request, "teacher.html")

#Employee Page
def employeeAdd(request):
    
    my_Message= {
        'Error_Message':'Employee Add Failed',
        'Success_Message':'Employee Add Successfully',
    }

    if request.method=="POST":

        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        employee=Employees_Model(
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        if Profile_pic:
           employee.myImage=Profile_pic
        else:
           employee.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        employee.save()
        
        messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])
            
        return redirect("employeePageUrl")

    return render(request, "employee.html")


#Authority Page
def authorityAdd(request):
    my_Message= {
        'Error_Message':'Authority Add Failed',
        'Success_Message':'Authority Add Successfully',
    }

    if request.method=="POST":

        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        authority=Authority_Model(
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        
        if Profile_pic:
           authority.myImage=Profile_pic
        else:
          authority.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        
        authority.save()
        messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])
        return redirect("authorityPageUrl")

    return render(request, "authority.html")

#Library Page
def libraryAdd(request):
    
    my_Message= {
        'Error_Message':'Library Add Failed',
        'Success_Message':'Library Add Successfully',
    }

    if request.method=="POST":

        b_name=request.POST.get("Book_Name")
        w_name=request.POST.get("Writer_Name")
        s_num=request.POST.get("Serial_No")
        a_date=request.POST.get("Acquisition_Date")
        r_date=request.POST.get("Return_Date")
        Profile_pic=request.FILES.get("Profile_pic")
        library=Library_Model(
            Book_Name=b_name,
            Writer_Name=w_name,
            Serial_No=s_num,
            Acquisition_Date=a_date,
            Return_Date=r_date,
            myImage=Profile_pic
            )
        
        if Profile_pic:
           library.myImage=Profile_pic
        else:
           library.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        
        library.save()
        messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])
        
        return redirect("libraryPageUrl")

    return render(request, "library.html")


def editStudent(request,myid):
    student=Students_Model.objects.filter(id=myid)
    
    context={
        "student":student,
             }
    
    return render(request,"editStudent.html",context)

def deleteStudent(request,myid):
    student=Students_Model.objects.filter(id=myid)
    student.delete()
    
    return redirect("studentPageUrl")
def updateStudent(request):
    
    my_Message= {
        'Error_Message':'Student Add Failed',
        'Success_Message':'Student Add Successfully',
    }

    if request.method=="POST":
       studentid=request.POST.get("studentid")
       f_name=request.POST.get("firstname")
       l_name=request.POST.get("lastname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")
       Profile_pic=request.FILES.get("Profile_pic")
       student=Students_Model(
        id=studentid,                    
        First_Name=f_name,
        Last_Name=l_name,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,
        myImage=Profile_pic
       )
         
       if Profile_pic:
           student.myImage=Profile_pic
       else:
           student.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg' 
              
       student.save()
       
       messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])
        student.save()

    return redirect("studentPageUrl")

  

def editTeacher(request,myid):
    teacher=Teachers_Model.objects.filter(id=myid)
    context={
        "teacher":teacher,
             }
    
    
    return render(request,"editteacher.html",context)

def deleteTeacher(request,myid):
    teacher=Teachers_Model.objects.filter(id=myid)
    
    teacher.delete()
    
    return redirect("teacherPageUrl")

def updateTeacher(request):
    my_Message= {
        'Error_Message':'Teacher Add Failed',
        'Success_Message':'Teacher Add Successfully',
    }

    if request.method=="POST":
        teacherid=request.POST.get("teach")
        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        teacher=Teachers_Model(
            id= teacherid,
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        if Profile_pic:
         teacher.myImage=Profile_pic
        else:
           teacher.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg' 
            
        teacher.save()
        messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])
        teacher.save()

        return redirect("teacherPageUrl")
    
    
def editEmployee(request,myid):
    
   
      
    employee=Employees_Model.objects.filter(id=myid)
    
    
    context={
        "employee":employee,
             }
    
    
    return render(request,"editemm.html",context)

def deleteEmployee(request,myid):
    employee=Employees_Model.objects.filter(id=myid)
    
    employee.delete()
    
    return redirect("employeePageUrl")

def updateEmployee(request):
    
    my_Message= {
        'Error_Message':'Employee Add Failed',
        'Success_Message':'Employee Add Successfully',
    }

    if request.method=="POST":
        employeeid=employee.POST.get("emm")
        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        employee=Employees_Model(
            id=employeeid,
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        
        if Profile_pic:
           employee.myImage=Profile_pic
        else:
           employee.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        employee.save()
        
        messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])
            
        return redirect("employeePageUrl")
    

def editAuthority(request,myid):
    Authority=Authority_Model.objects.filter(id=myid)
    
    
    context={
        "Authority":Authority,
             }
    
    
    return render(request,"editaut.html",context)

def deleteAuthority(request,myid):
    Authority=Authority_Model.objects.filter(id=myid)
    
    Authority.delete()
    
    return redirect("authorityPageUrl")

def updateAuthority(request):
    my_Message= {
        'Error_Message':'Authority Add Failed',
        'Success_Message':'Authority Add Successfully',
    }

    if request.method=="POST":
        Authorityid=Authority.POST.get("aut")
        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        Profile_pic=request.FILES.get("Profile_pic")
        Authority=Authority_Model(
            id=Authorityid,
            First_Name=f_name,
            Last_Name=l_name,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            myImage=Profile_pic
            )
        if Profile_pic:
           Authority.myImage=Profile_pic
        else:
          Authority.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        
        Authority.save()
        messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])
        Authority.save()

        return redirect("authorityPageUrl")
    
def editlibrary(request,myid):
        
    library=Library_Model.objects.filter(id=myid)
    
    
    context={
        "library":library,
             }
    
    
    return render(request,"editlib.html",context)

def deletelibrary(request,myid):
    library=Library_Model.objects.filter(id=myid)
    
    library.delete()
    
    return redirect("libraryPageUrl")

def updatelibrary(request):
    
     
    my_Message= {
        'Error_Message':'Library Add Failed',
        'Success_Message':'Library Add Successfully',
    }


    if request.method=="POST":

        b_name=request.POST.get("Book_Name")
        w_name=request.POST.get("Writer_Name")
        s_num=request.POST.get("Serial_No")
        a_date=request.POST.get("Acquisition_Date")
        r_date=request.POST.get("Return_Date")
        Profile_pic=request.FILES.get("Profile_pic")
        library=Library_Model(
            Book_Name=b_name,
            Writer_Name=w_name,
            Serial_No=s_num,
            Acquisition_Date=a_date,
            Return_Date=r_date,
            myImage=Profile_pic
            )
        if Profile_pic:
           library.myImage=Profile_pic
        else:
           library.myImage=Profile_pic='C:/Users/lab 504-1/Desktop/Project/myProject/template/default.jpg'  
        
        library.save()
        messages.success(request,my_Message["Success_Message"])
    else:
        messages.success(request,my_Message["Error_Message"])
        
       
        return redirect("libraryPageUrl")

    
