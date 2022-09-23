from django.shortcuts import render,redirect
from site_module.models import site_banner
from .models import Product, ProductCategory,ProductBrand,product_visit,product_gallery_images,product_comment
from django.views.generic import ListView,DetailView
from django.views import View
from django.http import HttpRequest,HttpResponse
from django.db.models import Count
from utils.http_service import get_client_ip
from utils.convertor import group_list
# Create your views here.
class product_list_view(ListView):
    template_name='product_module/product_list.html'
    model=Product
    context_object_name='products'
    ordering=['-price']
    paginate_by=8
    def get_context_data(self,*,object_list=None,**kwargs):
        context=super(product_list_view,self).get_context_data()
        query=Product.objects.all()
        prooduct=query.order_by('-price').first()
        db_max_price=prooduct.price if prooduct is not None else 100000
        context['db_max_price']=db_max_price
        context['start_price']=self.request.GET.get('start_price') or 0
        context['end_price']=self.request.GET.get('end_price') or db_max_price
        context['banners']=site_banner.objects.filter(is_active=True,position__iexact=site_banner.site_banner_choices.product_list)
        return context
    def get_queryset(self):
        data=super(product_list_view,self).get_queryset()

        category_name=self.kwargs.get('cat')
        brand_name=self.kwargs.get('brand')
        request:HttpRequest=self.request
        start_price=request.GET.get('start_price')
        end_price=request.GET.get('end_price')

        if start_price is not None:
            data=data.filter(price__gte=start_price)

        if end_price is not None:
            data=data.filter(price__lte=end_price)

        if brand_name is not None:
            data=data.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            data=data.filter(category__url_title__iexact=category_name) 
        return data

class product_detail_view(DetailView):
    template_name='product_module/product_detail.html'
    model=Product 
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        loaded_product=self.object
        request=self.request
        favorite_product_id=request.session.get("product_favorites")
        context['is_favorite']=favorite_product_id==str(loaded_product.id)
        context['banners']=site_banner.objects.filter(is_active=True,position__iexact=site_banner.site_banner_choices.product_detail)
        
        galleries=list(product_gallery_images.objects.filter(product_id=loaded_product.id).all())
        galleries.insert(0,loaded_product)
        context['product_galleries_group']=group_list(galleries,3)
        context['related_products']=group_list(list(Product.objects.filter(brand_id=loaded_product.brand_id).exclude(pk=loaded_product.id).all()[:12]),3)

        user_ip=get_client_ip(self.request)
        user_id=None
        if self.request.user.is_authenticated:
            user_id=self.request.user.id
        has_been_visited=product_visit.objects.filter(ip__iexact=user_ip,product_id=loaded_product.id).exists()
        if not has_been_visited:
            new_visit=product_visit(ip=user_ip,user_id=user_id,product_id=loaded_product.id)
            new_visit.save()
        product=kwargs.get('object')
        context['comments_count']=product_comment.objects.filter(product_id=product.id).count()
        context['comments']=product_comment.objects.filter(product_id=product.id)
        return context

# def add_product_comment(request:HttpRequest):
#     if request.user.is_authenticated:
#         product_id=request.GET.get('product_id')
#         product__comment=request.GET.get('product_comment')
#         parent_id=request.GET.get('parent_id')
#         print(product_id, product_comment, parent_id)
#         new_comment= product_comment(product_id=product_id,text=product__comment,user_id=request.user.id,parent_id=parent_id)
#         new_comment.save()
#         context={
#             'comments':product_comment.objects.filter(product_id=product_id,parent=None).order_by('-create_date').prefetch_related('product_comment_set'),
#             'comments_count':product_comment.objects.filter(product_id=product_id).count()
#         }
#         return render(request,'product_module/components/product_component_partial.html',context)
#     return HttpResponse('comment_add')

def product_category_components(request:HttpRequest):
    product_categories=ProductCategory.objects.filter(is_active=True,is_delete=False)
    context={
        'categories':product_categories
    }
    return render(request,'product_module/components/product_category_component.html',context)


def product_brand_components(request:HttpRequest):
    product_brands=ProductBrand.objects.annotate(products_count=Count('product_brand')).filter(is_active=True)
    context={
        'brands':product_brands
    }
    return render(request,'product_module/components/product_brand_component.html',context)