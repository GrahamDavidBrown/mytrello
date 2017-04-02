"""trello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from rest_framework import routers
from trello_app import views
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'api/boards', views.BoardViewSet)
router.register(r'api/lists', views.ListViewSet)
router.register(r'api/cards', views.CardViewSet)
router.register(r'api/user_profile', views.UserProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^home/', views.home),
]
