from django.conf.urls import url
from location import views as location_views

urlpatterns = [
	url(r'^$', location_views.welcome, name="location_welcome"),
]
