from django.urls import path
from . import views
urlpatterns=[
    path('register',views.register_view.as_view(),name='register_page'),
    path('login',views.login_view.as_view(),name='login_page'),
    path('logout',views.logout_view.as_view(),name='logout_page'),
    path('forget_password', views.forget_password_view.as_view(), name='forget_password_page'),
    path('reset_password/<active_code>', views.reset_password_view.as_view(), name='reset_password_page'),
    path('activate_account/<email_active_code>', views.activate_account.as_view(), name='activate_account'),
]