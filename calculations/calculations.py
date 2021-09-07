from django.utils import timezone
from datetime import *
import math

now = datetime.now()
today = now.today()

class DateTime:
    
    def __init__(self, today):
        self.today = today

    def get_today_date(self):
        today_date = self.today.strftime("%Y-%m-%d")
        return today_date
    
    def get_today_time(self):
        today_time = self.today.strftime("%H:%M")
        return today_time
    
    def get_tomorrow_date(self):
        tomorrow = self.today + timedelta(days=1)
        tomorrow_date = tomorrow.strftime("%Y-%m-%d")
        return tomorrow_date



