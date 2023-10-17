from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ['username','first_name','last_name','blue_tick','golden_tick','black_tick']


admin.site.register(User,UserAdmin)
