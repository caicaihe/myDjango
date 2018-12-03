from django.conf.urls import url
from .views import env_setting

urlpatterns = [
    url(r'^', env_setting)
]
