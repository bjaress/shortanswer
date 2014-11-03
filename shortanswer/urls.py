from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'shortapp.views.home_page', name='home'),
    url(r'^question$', 'shortapp.views.question_form'),
    url(r'^question/(\d+)$', 'shortapp.views.question'),
    url(r'^accounts/login/debug$', 'shortapp.views.login_debug'),
    url(r'^accounts/logout$', 'shortapp.views.logout'),
    # Examples:
    # url(r'^$', 'shortanswer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
