from . import views
from django.urls import path
urlpatterns=[
    path('',views.user_panel_dashboard_page.as_view(),name="user_panel_dashboard"),
    path('edit-profile',views.edit_user_profile_page.as_view(),name="edit_user_profile_page"),
    path('change_password',views.change_password.as_view(),name="change_password_page"),
    path('user_basket',views.user_basket,name="user_basket_page"),
    path('shopping_history',views.shopping_history.as_view(),name="shopping_history"),
    path('shopping_detail_history/<order_id>',views.shopping_detail_history,name="shopping_detail_history"),
    path('remove_order_detail',views.remove_order_detail,name="remove_order_detail"),
    path('change_order_detail',views.change_order_detail,name="change_order_detail")
]