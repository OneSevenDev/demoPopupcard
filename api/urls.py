from django.conf.urls import url

from api.views import hello_world, comment_list, CommentList

urlpatterns = [
    url(r'^commets/', CommentList.as_view(), name='ws_comments_all')
    # url(r'^commets/(?P<slug>[-\w]+)/$', comment_list, name='ws_comments_all')
]
