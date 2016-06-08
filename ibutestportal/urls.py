from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    url(r'^(?P<api_id>[0-9]+)/save/$',views.save_detail, name='save_detail'),
]