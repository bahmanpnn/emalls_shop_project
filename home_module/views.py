from product_module.models import Product, ProductCategory
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from site_module.models import site_setting,footer_link,footer_link_box,slider
from utils.convertor import group_list
from django.db.models import Count

# Create your views here.
from django.db.models import Sum

class index_page_view2(TemplateView):
    template_name='home_module/index_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"] = slider.objects.filter(is_active=True)
        
        latests_products=Product.objects.filter(is_active=True,is_delete=False).order_by('-id')[:12]
        context['latest_products']=group_list(latests_products)

        most_visited_products=Product.objects.annotate(visit_count=Count('product_visit')).filter(is_active=True,is_delete=False,visit_count__gt=0).order_by('-visit_count')[:12]
        context['most_visited_products']=group_list(most_visited_products)
        
        most_bought_products=Product.objects.filter(order_detail__order__is_paid=True
        ).annotate(order_count=Sum('order_detail__count')).order_by('-order_detail__count')[:12]
        context['most_bought_products']=group_list(most_bought_products)

        categories=list(ProductCategory.objects.annotate(products_count=Count('product_categories')).filter(is_active=True,is_delete=False,products_count__gt=0)[:10])
        categories_products=[]
        for category in categories:
            item={
                'id':category.id,
                'title':category.title,
                # related_name e category too product,product_categories e
                'products':list(category.product_categories.all()[:4])
            }
            categories_products.append(item)
        
        context['categories_products']=categories_products
        return context
    
def site_header_component(request):
    sitesetting=site_setting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting':sitesetting
    }
    return render(request, 'shared/site_header_component.html', context)

def site_footer_component(request):
    sitesetting=site_setting.objects.filter(is_main_setting=True).first()
    footer_link_boxes=footer_link_box.objects.all()
    for item in footer_link_boxes:
        item.footer_link_set
    context = {
        'site_setting':sitesetting,
        'footer_link_boxes':footer_link_boxes
    }
    return render(request, 'shared/site_footer_component.html',context)

def about_us_view(request):
    sitesetting: site_setting = site_setting.objects.filter(is_main_setting=True).first()
    context={
        'site_setting':sitesetting
    }
    return render(request,'home_module/about_us.html',context)