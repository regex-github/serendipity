"""wxcloudrun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from wxcloudrun import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = (
    # 计数器接口
    url(r'^^api/count(/)?$', views.counter),

    # 获取主页
    url(r'(/)?$', views.index),

    # 论坛
    path('forum/', include('forum.urls')),

    # 首次尝试页面
    url('first_try', views.first_try),

)
