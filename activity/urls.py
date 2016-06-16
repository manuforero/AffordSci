from django.conf.urls import url
from . import views
#from reviewsy.views import review_detail
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.activity_list, name='activity list'),
	url(r'^exercises/(?P<activity_id>[0-9]+)/$', views.activity_detail, 
		name= 'activity_detail'),
	url(r'^exercises/new', views.new_activity, name="new"),
	url(r'^exercises/(?P<activity_id>\d+)/edit/$', views.activity_edit, 
		name='activity_edit'),
	url(r'^exercises/(?P<activity_id>[0-9]+)/new_review/$', views.new_review, 
		name='new_review'),
	url(r'^reviews/(?P<review_id>[0-9]+)/$', views.review_detail, 
		name='review_detail'),
]