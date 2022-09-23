"""eshop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('account_module.urls')),
    path('articles/',include('article_module.urls')),
    path('contact/',include('contact.urls')),
    path('', include('home_module.urls')),
    path('products/', include('product_module.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user_panel_module.urls')),
    path('order/', include('order_module.urls')),
    path('zarin_pal/', include('zarin_pal_module.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns=urlpatterns++static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)