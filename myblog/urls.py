from django.contrib import admin
from django.template.context_processors import static
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    url('admin/$', admin.site.urls),
    url('blog/', include('blog.urls')),
    url(r'^$', views.index_unlog, name='index_unlog'),
    url('login/', views.login, name='login'),
    url('log/', views.logsuccess, name='login-success'),
    url('register/', views.register, name='register'),
    url('forget/', views.forget_password, name='forget'),
    url('reset/', views.reset, name='reset'),
    url('summernote/', include('django_summernote.urls')),
    url('logout', views.log_out, name='logout'),
]
