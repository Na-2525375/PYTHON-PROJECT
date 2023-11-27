from django.db import models

# Create your models here.

class Students_Model(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    myImage=models.ImageField(upload_to="media/profile_pic", null=True)

    def __str__(self):
     return self.First_Name+" "+self.Last_Name


class Teachers_Model(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    myImage=models.ImageField(upload_to="media/profile_pic", null=True)
    def __str__(self):
     return self.First_Name+" "+self.Last_Name



class Employees_Model(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    myImage=models.ImageField(upload_to="media/profile_pic", null=True)
    def __str__(self):
     return self.First_Name+" "+self.Last_Name


class Authority_Model(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    myImage=models.ImageField(upload_to="media/profile_pic", null=True)
    def __str__(self):
     return self.First_Name+" "+self.Last_Name

    

class Library_Model(models.Model):
    Book_Name=models.CharField(max_length=100,)
    Writer_Name=models.CharField(max_length=100,)
    Serial_No=models.CharField(max_length=100,)
    Acquisition_Date=models.CharField(max_length=100,)
    Return_Date=models.CharField(max_length=100,)
    myImage=models.ImageField(upload_to="media/profile_pic", null=True)
    def __str__(self):
     return self.Book_Name+" "+self.Writer_Name
