from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quantocustaparadjango.views.home', name='home'),
    # url(r'^quantocustaparadjango/', include('quantocustaparadjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.quero_fazer'),
    #url(r'^quero/', include(app.urls)),
    #url(r'^update/', 'blogapp.views.update'),
    #url(r'^delete/', 'blogapp.views.delete'),
)
