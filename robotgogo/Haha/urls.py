from django.conf.urls import url, include

from . import view

 
urlpatterns = [
    url(r'^$', view.hello),


    url(r'^envsetting/', include("envSetting.urls")),
    url(r'^runAPItest/', include("runAPItest.urls")),
]