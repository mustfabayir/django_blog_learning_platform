from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home","slug","selected_category",)
    list_editable = ("is_home", "is_active",)
    search_fields = ("title","description",)
    # readonly_fields = ("description",) # Admin de blog icindeki title larin icindeki aciklamalarin sadece okunabilir olmasini saglar. Isimize yaramayabilir
    readonly_fields = ("slug",)
    list_filter = ("is_active","is_home","title","categories",)   # Adminde blog icinde sag tarafta liste filtreleme ozelligini getirir.

    def selected_category(self, obj):
        html = "<ul>"

        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"    

        html += "</ul>"

        return mark_safe(html)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)