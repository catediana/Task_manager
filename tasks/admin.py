from django.contrib import admin
from .models import Category, Task, UserProfile,Subtask, Comment

admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register( Comment)