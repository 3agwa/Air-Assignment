from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout')
]