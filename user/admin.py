# admin.py
from django.contrib import admin
from user.models import User as UserModel
from user.models import Hobby as HobbyModel
from user.models import UserProfile as UserProfileModel

admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)
