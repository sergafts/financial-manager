from django.conf.urls import patterns, url

from views import index, login_user

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'financial_manager.views.home', name='home'),
    # url(r'^financial_manager/', include('financial_manager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^', index, name='index'),
    url(r'^login/$', login_user, name='login')
)
