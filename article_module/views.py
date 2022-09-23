from .models import article
from django.shortcuts import render
from django.views import View
from django.http import HttpRequest,HttpResponse
from django.views.generic.list import ListView
from django.views.generic import DetailView
from article_module.models import article_category,article,article_comment
from site_module.models import site_banner

class article_view(ListView):
    model=article
    paginate_by=2
    template_name='article_module/articles.html'
    context_object_name = 'articles'
    ordering=['-create_date']
    # def get_contex_data(self,*args,**kwargs):
    #     context=super(article_view, self).get_contex_data(*args,**kwargs)
    #     return context
    def get_queryset(self):
        query=super(article_view, self).get_queryset()
        query=query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_category__url_title__iexact=category_name)
        return query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners']=site_banner.objects.filter(is_active=True,position__iexact=site_banner.site_banner_choices.article_page)
        return context
    
class article_detail_view(DetailView):
    model=article
    template_name='article_module/article_detail.html'
    def get_queryset(self):
        query=super(article_detail_view, self).get_queryset()
        query=query.filter(is_active=True)
        return query
    def get_context_data(self,**kwargs):
        context=super(article_detail_view, self).get_context_data()
        article=kwargs.get('object')
        context['comments']=article_comment.objects.filter(article_id=article.id,parent=None).order_by('-create_date').prefetch_related('article_comment_set')
        context['comments_count']=article_comment.objects.filter(article_id=article.id).count()
        context['banners']=site_banner.objects.filter(is_active=True,position__iexact=site_banner.site_banner_choices.articles_detail_page)
        return context
def article_categoris_component(request):
    main_article_category=article_category.objects.prefetch_related('article_category_set').filter(is_active=True,parent_id=None)
    context={
        'main_article_categoris':main_article_category
    }
    return render(request,'article_module/components/article_categoris_component.html',context)
def add_article_comment(request:HttpRequest):
    if request.user.is_authenticated:
        article_id=request.GET.get('article_id')
        article__comment=request.GET.get('article_comment')
        parent_id=request.GET.get('parent_id')
        new_comment= article_comment(article_id=article_id,text=article__comment,user_id=request.user.id,parent_id=parent_id)
        new_comment.save()
        context={
            'comments':article_comment.objects.filter(article_id=article_id,parent=None).order_by('-create_date').prefetch_related('article_comment_set'),
            'comments_count':article_comment.objects.filter(article_id=article_id).count()
        }
        return render(request,'article_module/includes/article_component_partial.html',context)
    return HttpResponse('hello')