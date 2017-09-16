from django.conf.urls import url
from action import views as action_views

urlpatterns = [
    url(r'^$', action_views.welcome, name="action_welcome"),
    url(r'^text/$', action_views.user_actions_text, name="user_actions_text"),
]
