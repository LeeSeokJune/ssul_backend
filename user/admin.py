from django.contrib import admin
from .models import CustomUser, SsulCategoryCount
# Register your models here.


class CategoryCountInline(admin.TabularInline):
    model = SsulCategoryCount


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [CategoryCountInline, ]


admin.site.register(CustomUser, CustomUserAdmin)
