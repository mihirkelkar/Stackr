from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stackr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'stackr.views.homepage', name = 'landing'),
    url(r'^packr/', 'stackr.views.packr', name = 'packr'),
    url(r'^stackr/', 'stackr.views.stackr', name = 'stackr'),
    #User Auth Urls
    url(r'^login/$', 'stackr.views.login', name = "Login Page"),
    url(r'^login/auth/$', 'stackr.views.auth_view'),
    url(r'^logout', 'stackr.views.logout', name = "Logout Thingy"),
    url(r'^loggedin', 'stackr.views.loggedin', name = "Internal landing page"),
    url(r'^invalid', 'stackr.views.invalid', name = "Invalid Log In"),
)
