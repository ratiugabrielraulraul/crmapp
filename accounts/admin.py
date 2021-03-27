from django.contrib import admin
from .models import *

# register added manually.Django does not recognize it.

admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Tag)
