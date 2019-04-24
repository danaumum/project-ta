from django.conf.urls import url

from . import views

app_name = 'jar_irigasi'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^corong/(?P<slugInput>[\w-]+)/$', views.detailCorong, name='detCorong'),
	url(r'^sadap/(?P<slugInput>[\w-]+)/$', views.detailSadap, name='detSadap'),
	url(r'^bendung/(?P<slugInput>[\w-]+)/$', views.detailBendung, name='detBendung'),
	url(r'^laporan/$', views.laporan, name='laporan'),
	url(r'^listbangunan/', views.listBangunan),
	url(r'^skema/', views.skema),
	

]