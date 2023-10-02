from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('create_post', views.create_post),
    # path('delete_daily_aim', views.delete_daily_aim),
    # path('edit_daily_aim', views.edit_daily_aim),
    # path('get_daily_aim', views.get_daily_aim),
    # path('get_daily_aim_all', views.get_daily_aim_all),
    #
    # path('punch_in', views.punch_in),
    # path('get_punch_in', views.get_punch_in),
    #
    # path('create_future_aim', views.create_future_aim),
    # path('delete_future_aim', views.delete_future_aim),
    # path('edit_future_aim', views.edit_future_aim),
    # path('get_future_aim', views.get_future_aim),
    # path('get_future_aim_all', views.get_future_aim_all),
    # path('get_future_aim_detail', views.get_future_aim_detail),  # 查找一个未来目标的详情：包含他关联的日常目标
    # path('target_association', views.target_association),  # 查找一个未来目标的详情：包含他关联的日常目标
    # path('get_friend_aims', views.get_friend_aims),  # 查找一个朋友的全部未来目标及绑定的日常目标
]
