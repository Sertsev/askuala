"""askuala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import index

admin.site.site_header = "ASKUALA Admin"
admin.site.index_title = "Admin"
admin.site.site_title = "ASKUALA Site Administration"
# admin.site.doc_site_title = "white"

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user/', include('school_users.urls')),
    path('programs/', include('programs.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]
