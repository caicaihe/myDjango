from django.conf.urls import url
 
from . import view
from . import search
from . import search2
from . import pre_test
from . import run_test
from . import aft_test
 
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^hello$', view.hello),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', pre_test.search_post),
    url(r'^pre-test$', pre_test.search_post),
    #url(r'^insectsql$', pre_test.run),
    url(r'^run-test$', run_test.run),
    url(r'^gotest$', run_test.run),
    url(r'^aft-test$', aft_test.run),
    url(r'^result$', aft_test.reportshow),
    url(r'^test-env$', run_test.postenv),

    ]

