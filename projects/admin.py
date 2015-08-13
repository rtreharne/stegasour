from django.contrib import admin
from projects.models import *

admin.site.register(Project)
admin.site.register(Cohort)
admin.site.register(Upload)
admin.site.register(Upload_Type)

