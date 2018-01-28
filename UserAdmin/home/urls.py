from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^account/logout/$', views.Logout),
    url(r'^new$', views.new, name='new_client'),
    url(r'^create$', views.create, name='create_client'),
    url(r'^show/(?P<id>\d+$)', views.show, name='show_client'),
    url(r'^edit/(?P<id>\d+$)',views.edit, name='edit_client'),
    url(r'^update$',views.update, name='update_client'),
    url(r'^delete/(?P<id>\d+$)',views.delete, name='delete')
]
