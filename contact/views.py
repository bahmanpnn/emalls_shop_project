from .forms import contact_us_model_form
from .models import contact,user_profile
from site_module.models import site_banner
from django.views.generic.edit import FormView,CreateView
from django.views.generic import ListView
from site_module.models import site_setting
# Create your views here.
class contact_us_view(CreateView):
    form_class=contact_us_model_form
    template_name='contact/contact_us.html'
    success_url='/contact'
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        setting=site_setting.objects.filter(is_main_setting=True).first()
        context['site_setting']=setting
        context['banners']=site_banner.objects.filter(is_active=True,position__iexact=site_banner.site_banner_choices.contact_us)

        return context
def store_profile(file):
    with open('temp/image.jpg',"wb+")as dest:
        for chunk in file.chunks():
            dest.write(chunk)
class create_profile_view(CreateView):
    template_name='contact/create_profile.html'
    model=user_profile
    fields='__all__'
    success_url='/contact/create_profile'
class profiles_list_view(ListView):
    model = user_profile
    template_name='contact/profiles.html'
    context_object_name='profiles'
