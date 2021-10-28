from django.conf.urls import url
from zscore import views

urlpatterns = [
    url(r'^company$', views.post_request, name='post-request'),
    url(r'^company/(?P<pk>[0-9]+)$', views.put_request, name='put-request')
]