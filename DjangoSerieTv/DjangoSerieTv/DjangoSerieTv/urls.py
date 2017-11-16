"""
Definition of urls for DjangoSerieTv.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^ver/(?P<id>[0-9]+)$', app.views.ver, name='ver'),
    url(r'^editar/(?P<id>[0-9]+)$', app.views.editar, name='editar'),
    url(r'^borrar/(?P<id>[0-9]+)$', app.views.borrar, name='borrar'),
    url(r'^listar/(?P<data>[a-zA-Z]+)$', app.views.listar, name='listar'),
    url(r'^verData/(?P<tipo>[a-zA-Z]+)/(?P<data>[a-zA-Z0-9\s]+)$', app.views.verData, name='verData'),
    url(r'^crear$', app.views.crear, name='crear'),
    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': app.forms.BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title': 'Log in',
    #            'year': datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
