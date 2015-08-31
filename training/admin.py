from django.contrib import admin
from training.models import *

class ElementAdmin(admin.ModelAdmin):
	list_display=('title', 'module', 'tag')

class ResourceAdmin(admin.ModelAdmin):
	list_display=('name', 'element', 'resource_type', 'public')

admin.site.register(Module)
admin.site.register(Element, ElementAdmin)
admin.site.register(Assessment)
admin.site.register(Submission)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Resource_Type)
admin.site.register(Feedback)

