from django.template.backends import django
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import  static
urlpatterns = [
    path(route='', view=RedirectView.as_view(url='/home/', permanent=False)),
    path(route='home/', view=views.home, name='home'),
    path(route='news/', view=views.news, name='news'),
    path(route='money-by-phone/', view=views.money_by_phone, name='money-by-phone'),
    path(route='work-as-leader/', view=views.work_as_leader, name='work-as-leader'),
    path(route='family-shopping/', view=views.family_shopping, name='family-shopping'),
    path(route='about-products/', view=views.about_products, name='about-products'),
    path(route='load-more-deals/', view=views.load_more_deals, name='load_more_deals'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)