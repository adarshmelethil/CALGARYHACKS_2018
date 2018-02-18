

from django.conf.urls import url
from ParticleHooks.views import ProcessHookView, profile, logoutuser

from ParticleHooks.views import addDevice, removeDevice, addNumber, removeNumber

app_name = 'ParticleHooks'

urlpatterns = [
	url(r'^hooks$', ProcessHookView.as_view(), name='hooks'),
    url(r'^profile$', profile, name='profile'),
    url(r'^logoutuser$', logoutuser, name='logoutuser'),
    
    url(r'^addDevice$', addDevice, name="addDevice"),
    url(r'^removeDevice$', removeDevice, name='removeDevice'),

    url(r'^addNumber$', addNumber, name='addNumber'),
    url(r'^removeNumber$', removeNumber, name='removeNumber')
    # url(r'^signup$', signup, name='signup')
]
