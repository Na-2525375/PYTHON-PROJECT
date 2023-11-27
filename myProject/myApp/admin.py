from django.contrib import admin

# Register your models here.

from myApp.models import Students_Model
from myApp.models import Teachers_Model
from myApp.models import Employees_Model
from myApp.models import Authority_Model
from myApp.models import Library_Model

admin.site.register(Students_Model)
admin.site.register(Teachers_Model)
admin.site.register(Employees_Model)
admin.site.register(Authority_Model)
admin.site.register(Library_Model)