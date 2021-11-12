from django.contrib import admin
from .models import home, about, service, project, contact
# Register your models here.

admin.site.register(home)
admin.site.register(about)
admin.site.register(service)
admin.site.register(project)
admin.site.register(contact)
