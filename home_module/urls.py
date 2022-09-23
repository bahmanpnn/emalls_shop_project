from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page_view2.as_view(),name='home_page'),
    path('about_us', views.about_us_view,name='about_us_page'),
    # path('site-header', views.site_header_partial, name='site_header_partial')
]
