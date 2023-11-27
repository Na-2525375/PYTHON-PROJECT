from django.shortcuts import redirect, render
from myApp.models import *


def homePage(request):
   return render(request,"home.html")

def loginPage(request):
   return render(request,"login.html")

def signupPage(request):
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
       student.save()

       return redirect("studentPageUrl")

    return render(request, "student.html")

#Teacher Page
def teacherAdd(request):

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
        teacher.save()

        return redirect("teacherPageUrl")

    return render(request, "teacher.html")

#Employee Page
def employeeAdd(request):

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
        employee.save()

        return redirect("employeePageUrl")

    return render(request, "employee.html")


#Authority Page
def authorityAdd(request):

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
        authority.save()

        return redirect("authorityPageUrl")

    return render(request, "authority.html")

#Library Page
def libraryAdd(request):

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
        library.save()

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
        employee.save()

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
        library.save()

        return redirect("libraryPageUrl")

    
