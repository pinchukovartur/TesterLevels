"""
The script describes the project models

created by: Pinchukov Artur
date: 13.10.17
"""
# framework libs
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
# project libs
from . import views


"""
The script is responsible for allocating URLs to controllers
"""

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^files/(?P<secret_key>.*)$', views.get_files_name, name='get_files_name'),
    url(r'^file/(?P<secret_key>.*)/(?P<level_name>.*)$', views.get_file_name, name='get_file_name'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)