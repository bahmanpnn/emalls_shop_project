from django.contrib import admin
from .models import site_banner, site_setting,footer_link_box,footer_link,slider
class footer_link_admin(admin.ModelAdmin):
    list_display=['title','url']
class slider_admin(admin.ModelAdmin):
    list_display=['title','url','is_active']
    list_editable=['url','is_active']
class site_banner_admin(admin.ModelAdmin):
    list_display=['title','url','position']
# Register your models here.
admin.site.register(site_setting)
admin.site.register(footer_link_box)
admin.site.register(slider,slider_admin)
admin.site.register(footer_link,footer_link_admin)
admin.site.register(site_banner)