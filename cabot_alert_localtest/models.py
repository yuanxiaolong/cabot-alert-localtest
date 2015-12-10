from django.db import models
from cabot.cabotapp.alert import AlertPlugin, AlertPluginUserData
import time
import os

class LocalTestAlert(AlertPlugin):
    name = "LocalTest"
    author = "xiaolong.yuanxl"

    def send_alert(self, service, users, duty_officers):
        """Implement your send_alert functionality here."""

        # time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time()))
        os.open('/tmp/cabotTestLocalAlert' + time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time())),'a').close()

        return

class LocalTestAlertUserData(AlertPluginUserData):
    name = "LocalTest Plugin"
    favorite_bone = models.CharField(max_length=50, blank=True)

