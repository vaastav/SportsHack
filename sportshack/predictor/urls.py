from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'), # ADD NEW PATTERN!
	url(r'^login/$', views.login, name='login'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^select/$', views.select, name='select'),
	url(r'^profile/$', views.profile, name='profile'),
]
