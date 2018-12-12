from django.conf.urls import url, include

from . import view

 
urlpatterns = [
    url(r'^$', view.main),
    url(r'^environments$', view.addEnvironment),
    url(r'^environments/(\w+)$', view.deleteEnvironment),

    url(r'^env_setting/', include("env_setting.urls")),
    url(r'^run_APItest/', include("run_APItest.urls")),
]