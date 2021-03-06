from django.contrib import admin
from .models import Post, Category, Comment, Country

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Country)


class MyAdminView(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
       super(MyAdminView, self).save_model(request, obj, form, change)