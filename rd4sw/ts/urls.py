from django.conf.urls import url
from .views import hello_world, home, rd_home, training, training_android, training_tv, training_other
from . import views

app_name = 'ts'
urlpatterns = [
    #url(r'^$', views.home, name='home'),
	url(r'^hello/$', hello_world),
	url(r'^$', rd_home, name='home'),
	url(r'^rd4sw/$', rd_home),
	url(r'^training/$', training, name='training'),
	url(r'^android$', training_android, name='android'),
	url(r'^tv$', training_tv, name='tv'),
	url(r'^other$', training_other, name='other'),
]