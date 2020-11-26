from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
    url('', views.home, name='home'),
    url('category/<int:id>', views.category, name='category'),
    url('tags/', views.tags, name='tags'),
    url('tags/<int:id>/', views.tag_detail, name='tags_detail'),
    url('articles/<int:id>/', views.detail, name='detail'),
    url('commentpost', views.commentpost, name='commentpost'),
    url('userinfo', views.user_info, name='userinfo'),
    url('info/<comment_id>', views.comment_del, name="comm_del"),
    url('commentdel', views.comment_del, name='comment_del'),
    url('search/', views.search, name='search'),
]
