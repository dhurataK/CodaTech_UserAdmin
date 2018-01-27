from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^account/logout/$', views.Logout),
    url(r'^new$', views.new, name='new_user'),
    url(r'^create$', views.create, name='create_user'),
    url(r'^show/(?P<id>\d+$)', views.show, name='show_user'),
    url(r'^edit/(?P<id>\d+$)',views.edit, name='edit_user'),
    url(r'^update$',views.update, name='update_user'),
    url(r'^delete/(?P<id>\d+$)',views.delete, name='delete')
]
