from django.contrib import admin

from .models import *

admin.site.register([User,Profile,Skill,Education,Experience,Project,Contact])