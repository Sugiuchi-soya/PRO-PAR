from django.db import models,migrations
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# class CustomUser(AbstractUser):
#     pass



class Area(models.Model):
    area_name = models.CharField("エリア名", max_length=15)
    def __str__(self):
        return self.area_name

class Parking(models.Model):
    name = models.CharField("パーキング名", max_length=50)
    image = models.ImageField("画像", blank=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT, default=None)
    address = models.CharField("住所", max_length=100)
    distance = models.IntegerField("ゲストハウスからの距離")
    charge = models.IntegerField("利用料金", default=0)
    # max_digits(数字の最大桁数),decimal_places(少数の桁数)
    latitude = models.DecimalField("緯度", max_digits=22, decimal_places=16)
    longitude = models.DecimalField("経度", max_digits=22, decimal_places=16)
    number_of_parking_spaces = models.IntegerField("駐車台数")
    created_at = models.DateTimeField("追加日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.name



