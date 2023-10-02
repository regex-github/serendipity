from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.db.models import F
from .models import *
from django.utils.timezone import now
import datetime
import json


def create_post(request):
    return render(request, 'forum.html')


# def create_daily_aim(request):
#     """
#     创建新的日常目标
#
#     """
#
#     open_id = request.POST.get('open_id')
#
#     content = request.POST.get('content')
#     aim_type = request.POST.get('aim_type', 0)
#     icon_path = request.POST.get('icon_path', "null")
#
#     # 改正 布尔类型 获取
#     is_remind_str = request.POST.get('is_remind', "False")
#     is_remind = True if is_remind_str in ('true', 'True', '1') else False
#
#     remind_time = request.POST.get('remind_time', '01-01')
#
#     aim = DailyAim(open_id=open_id, content=content, aim_type=aim_type,
#                    is_remind=is_remind, remind_time=remind_time, icon_path=icon_path)
#     aim.save()
#
#     return JsonResponse({"log": "创建日常目标成功"})

