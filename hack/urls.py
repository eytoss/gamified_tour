from django.conf.urls import url
from hack import views as hack_views

urlpatterns = [
	url(r'^$', hack_views.welcome, name="welcome"),
	url(r'^user/positions/reach/$', hack_views.hack_positions_reach, name="hack_positions_reach"),
]
