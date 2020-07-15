from django.contrib import admin

# Register your models here.
from django.contrib import admin
from  . models import Profile,Projects,Comments


admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Comments)