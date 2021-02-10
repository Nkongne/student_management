
"""student_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.conf.urls import url
from  django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from registration import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()
urlpatterns=[

        path('admin/',admin.site.urls),
       # url(r'^registration/(?P<slug>[-\w]+)/$','registration.views.detail'),

        path('registration/', include('registration.urls'), name='registration'),
        path('report_card/', include('report_card.urls'), name='report_card'),
        path('staff/', include('staff.urls'), name='staff'),
        path('', include('registration.urls'), name='registration'),
        #path('',views.index, name='index'),
        ]



        #url(r'^jsi18n/(?P<package>\S+?)/$', 'django.views.i18n.js_catalog_template'),

