# from django.contrib import admin
# from .models import *
#
#
# # Register your models here.
#
#
# class DailyAimManager(admin.ModelAdmin):
#     list_display = ['id', 'open_id', 'content', 'record_times', 'create_time', 'is_active']
#
#
# admin.site.register(DailyAim, DailyAimManager)
#
#
# class PunchInManager(admin.ModelAdmin):
#     list_display = ['id', 'daily_aim', 'record_date']
#
#
# admin.site.register(PunchIn, PunchInManager)
#
#
# class FutureAimManager(admin.ModelAdmin):
#     list_display = ['id', 'open_id', 'content', 'description', 'deadline', 'schedule', 'is_active']
#
#
# admin.site.register(FutureAim, FutureAimManager)