"""sc-identity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
# from inventory.views import InventoryView, AllInventoryView, SubsetInventoryView
# from django.utils.translation import ugettext_lazy as _

schema_view = get_swagger_view(title='Secure Cloud API')

urlpatterns = [
    url(r'^$', schema_view),
    #url(r'^api/auth', include('knox.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/auth/', include('identity.urls', namespace='auth')),
    url(r'^api/v1/jobs/', include('jobs.urls', namespace='jobs')),
    url(r'^api/v1/deployment/', include('deployment.urls', namespace='deployment')),
    url(r'^api/v1/inventory/', include('inventory.urls', namespace='inventory')),
    url(r'^api/v1/cp/', include('cp.urls', namespace='cp')),
    url(r'^admin/', admin.site.urls),
]