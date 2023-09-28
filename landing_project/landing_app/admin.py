from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','name','email','number')
    list_filter = ('name','email')
    search_fields = ('name',)

admin.site.register(Customer,CustomerAdmin)
# Register your models here.
