from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name="about"),
    path('putlist/', putlist, name='putlist'),
    path('normrashod/', normrashod, name='normrashod'),
    path('othets/', othets, name='othets'),
    path('addauto/', addauto, name='addauto'),
    path('editauto/', editauto, name='editauto'),
    # path('post/<int:post_id>/', show_post, name='post'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),

    path('pers/<int:perid>/', personal),
    path('to/<slug:per>/', obslug),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]
