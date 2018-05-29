from django.contrib import admin

from .models import Address, Transaction


admin.site.register(Address)
admin.site.register(Transaction)
