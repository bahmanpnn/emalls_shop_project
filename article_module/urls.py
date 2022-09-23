from django.urls import path
from . import views
urlpatterns=[
    path('',views.article_view.as_view(),name='article_page'),
    path('category/<str:category>',views.article_view.as_view(),name='articles_by_category_page'),
    path('<pk>/',views.article_detail_view.as_view(),name='articles_detail_page'),
    path('add-article-comment',views.add_article_comment,name='add_article_comment'),

]