from django.urls import path
from . import views
urlpatterns = [
    path('request/', views.send_request, name='request_payment'),
    path('verify/', views.verify , name='verify'),
]
