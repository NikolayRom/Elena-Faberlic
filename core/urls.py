from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path(route='', view=RedirectView.as_view(url='/home/', permanent=False)),
    path(route='home/', view=views.home, name='home'),
    path(route='news/', view=views.news, name='news'),
    path(route='money-by-phone', view=views.money_by_phone, name='money-by-phone'),
    path(route='work-as-leader', view=views.work_as_leader, name='work-as-leader'),
    path(route='family-shopping', view=views.family_shopping, name='family-shopping'),
]