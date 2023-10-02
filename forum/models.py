# import json
#
# from django.db import models
#
#
# # Create your models here.
#
#
# class DailyAim(models.Model):
#     id = models.AutoField(primary_key=True)
#
#     open_id = models.CharField(max_length=50, default='')
#     content = models.CharField(max_length=50, default='')
#     aim_type = models.IntegerField(default=0)
#     icon_path = models.CharField(max_length=50, default='/images/aim.png')
#     is_remind = models.BooleanField(default=False)
#     remind_time = models.CharField(max_length=50, default='null')
#
#     create_time = models.DateTimeField(auto_now_add=True)
#     record_times = models.IntegerField(default=0)
#     # today_punch = models.BooleanField(default=False)
#
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.content
#
#
# class PunchIn(models.Model):
#     id = models.AutoField(primary_key=True)
#
#     daily_aim = models.ForeignKey(DailyAim, on_delete=models.CASCADE)
#     record_date = models.DateField(auto_now_add=True)
#
#
# class FutureAim(models.Model):
#     id = models.AutoField(primary_key=True)
#
#     open_id = models.CharField(max_length=50, default='null')
#     content = models.CharField(max_length=50, default='null')
#     description = models.CharField(max_length=100, default='null')
#
#     deadline = models.DateField(default='2022-05-01')
#     schedule = models.DecimalField(max_digits=4, decimal_places=3, default=0)
#     is_active = models.BooleanField(default=True)
#     daily_aims = models.CharField(max_length=200, default='')
#
#     create_time = models.DateTimeField(auto_now_add=True)
#     estimated_completion_time = models.DateField(default='2022-05-01')
#
#     def update_schedule(self):
#         binds = json.loads(self.daily_aims)
#         schedule_arr = []
#         # print(binds)
#         for bind in binds:
#             schedule = DailyAim.objects.get(id=bind['daily_aim_id']).record_times / bind['target_times']
#             if schedule > 1:
#                 schedule = 1.0
#             schedule_arr.append(schedule)
#
#         self.schedule = sum(schedule_arr) / len(schedule_arr)
#         self.save()
#
#     def __str__(self):
#         return self.content
#
# # class FutureDailyBind(models.Model):
# #     """
# #     未来目标和日常目标的绑定
# #     """
# #     id = models.AutoField(primary_key=True)
# #
# #     future_aim = models.ForeignKey(FutureAim, on_delete=models.CASCADE)
# #     daily_aim = models.ForeignKey(DailyAim, on_delete=models.CASCADE)
# #     target_times = models.IntegerField(default=0)
# #     is_active = models.BooleanField(default=True)
