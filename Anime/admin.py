from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *

admin.site.register(Anime)
admin.site.register(Character)
admin.site.register(Category)
admin.site.register(Producer)
admin.site.register(Episode)

admin.site.unregister(User)
admin.site.unregister(Group)
