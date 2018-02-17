

from django.conf.urls import url
from ParticleHooks.views import ProcessHookView, index


urlpatterns = [
	url(r'^hooks/$', ProcessHookView.as_view(), name='home'),
    url(r'^$', index, name='index'),
]
