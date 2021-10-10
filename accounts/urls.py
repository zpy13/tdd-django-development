from django.conf.urls import url
from django.contrib.auth.views import logout_then_login
from accounts import views

urlpatterns = [
    url(r'^send_login_email$', views.send_login_email, name='send_login_email'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', logout_then_login, {'login_url': '/'}, name='logout'),
]
