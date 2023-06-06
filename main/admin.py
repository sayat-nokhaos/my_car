from django.contrib import admin
from .models import Car, OldCarInformation, Order

class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')  # отображаемые поля в списке объектов
    search_fields = ('title',)


admin.site.register(Car, CarAdmin)
admin.site.register(OldCarInformation)
admin.site.register(Order)