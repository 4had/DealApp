from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.


class BuyerAddressInLine(admin.TabularInline):
    model = Address
    extra = 0


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username']
    fields = ['photo','username', 'first_name', 'last_name', 'user_type']
    inlines = [BuyerAddressInLine]


admin.site.register(UserProfile, UserProfileAdmin, )


class BuyerAddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]


admin.site.register(Address, BuyerAddressAdmin)