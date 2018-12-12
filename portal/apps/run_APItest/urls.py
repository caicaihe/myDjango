from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.run),
    url(r'devops/$', views.postenv),
    url(r'registry/$',views.registry),
]
