from django.contrib import admin
from event_app.models import *

# Register your models here.

admin.site.register([EventUserModel, EventModel])
