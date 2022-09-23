from django.contrib import admin
from . import models
from .models import article
# Register your models here.
class articlecategory_admin(admin.ModelAdmin):
    list_display=['title','parent','url_title','is_active']
    list_editable=['url_title','parent','is_active']
class article_admin(admin.ModelAdmin):
    list_display=['title','slug','is_active','author']
    list_editable=['is_active']
    def save_model(self,request,obj:article,form,change):
        if not change:
            obj.author = request.user
        return super().save_model(request,obj,form,change)

class article_comment_admin(admin.ModelAdmin):
    list_display=['user','create_date','parent']

admin.site.register(models.article_category,articlecategory_admin)
admin.site.register(models.article,article_admin)
admin.site.register(models.article_comment,article_comment_admin)