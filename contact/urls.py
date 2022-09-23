from django.urls import path
from . import views
urlpatterns=[
    path('',views.contact_us_view.as_view(),name='contact_page'),
    path('create_profile/',views.create_profile_view.as_view(),name='create_profile_page'),
    path('profiles/', views.profiles_list_view.as_view(), name='profile_page')
]