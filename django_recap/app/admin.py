from django.contrib import admin
from .models import MyModel

# Register your models here.
@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name',)
    list_filter = ('name',)
    # ordering = ('-created_at',)

    def has_add_permission(self, request):
        return True