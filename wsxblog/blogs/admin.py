from django.contrib import admin
from blogs.models import Categorys, Blogs, Tags, Comments, Vlogs

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'visiting', 'created_time', 'modifyed_time']

admin.site.register(Categorys)
admin.site.register(Blogs, BlogAdmin)
admin.site.register(Tags)
admin.site.register(Comments)
admin.site.register(Vlogs)