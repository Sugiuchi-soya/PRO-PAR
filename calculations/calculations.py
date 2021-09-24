# from django.utils import timezone
from datetime import *
import math

datetime_format = "%Y-%m-%d %H:%M"

now = datetime.now()
today = now.today()
today_date = today.strftime("%Y-%m-%d")
today_time = today.strftime("%H:%M")
tomorrow = today + timedelta(days=1)
tomorrow_date = tomorrow.strftime("%Y-%m-%d")

# 利用時間と単位と基本料金を渡して小計を算出
def get_subtotal(time, unit, basic_charge):
    target = time / unit
    round_up_number = math.ceil(target)
    usage_charge = round_up_number * basic_charge
    return usage_charge

# 料金と最大料金を渡して割引を適用させる
def apply_discount(usage_charge, MAX_CHARGE):
    if usage_charge >= MAX_CHARGE:
        usage_charge = MAX_CHARGE
    return usage_charge

# 小計の関数と割引適用の関数をまとめて利用料金を算出
def get_usage_charge(minuend, subtrahend, unit, basic_charge, max_charge):
    usage_time = minuend - subtrahend
    subtotal = get_subtotal(usage_time, unit, basic_charge)
    usage_charge = apply_discount(subtotal, max_charge)
    return usage_charge



# APパーク高知東の料金を計算
def calc_ap_park_kochi_higashi(entry, leaving):

    total_price = 0
    BASIC_CHARGE = 100
    DAYTIME_MAX_CHARGE = 800
    NIGHTTIME_MAX_CHARGE = 600
    DAYTIME_UNIT = timedelta(minutes=20)
    NIGHTTIME_UNIT = timedelta(minutes=60)
    DAYTIME_SERVICE_START = datetime.strptime(f"{today_date} 08:00", datetime_format)
    DAYTIME_SERVICE_END = datetime.strptime(f"{today_date} 20:00", datetime_format)
    DAYTIME_END = datetime.strptime(f"{tomorrow_date} 00:00", datetime_format)
    TOMORROW_DAYTIME_START = datetime.strptime(f"{tomorrow_date} 08:00", datetime_format)

    # 8時より前に入庫、8〜20時の間に出庫
    if entry < DAYTIME_SERVICE_START < leaving <= DAYTIME_SERVICE_END:

        usage_charge1 = get_usage_charge(DAYTIME_SERVICE_START, entry, NIGHTTIME_UNIT, BASIC_CHARGE, NIGHTTIME_MAX_CHARGE)
        usage_charge2 = get_usage_charge(leaving, DAYTIME_SERVICE_START, DAYTIME_UNIT, BASIC_CHARGE, DAYTIME_MAX_CHARGE)
        total_price = usage_charge1 + usage_charge2

    # 8時以降に入庫、20時までに出庫
    elif DAYTIME_SERVICE_START <= entry < leaving <= DAYTIME_SERVICE_END:

        total_price = get_usage_charge(leaving, entry, DAYTIME_UNIT, BASIC_CHARGE, DAYTIME_MAX_CHARGE)

    # 8時以降に入庫、20時よりあとに出庫
    elif DAYTIME_SERVICE_START <= entry < DAYTIME_SERVICE_END < leaving:

        usage_charge1 = get_usage_charge(DAYTIME_SERVICE_END, entry, DAYTIME_UNIT, BASIC_CHARGE, DAYTIME_MAX_CHARGE)
        usage_charge2 = get_usage_charge(leaving, DAYTIME_END, DAYTIME_UNIT, BASIC_CHARGE, NIGHTTIME_MAX_CHARGE)
        total_price = usage_charge1 + usage_charge2

    # 20〜0時に入庫、翌日8時までに出庫
    elif DAYTIME_SERVICE_END <= entry < DAYTIME_END <= leaving <= TOMORROW_DAYTIME_START:

        usage_charge1 = get_usage_charge(entry, DAYTIME_SERVICE_END, DAYTIME_UNIT, BASIC_CHARGE, NIGHTTIME_MAX_CHARGE)
        usage_charge2 = get_usage_charge(leaving, DAYTIME_END, NIGHTTIME_UNIT, BASIC_CHARGE, NIGHTTIME_MAX_CHARGE)
        total_price = usage_charge1 + usage_charge2
        total_price = apply_discount(total_price, NIGHTTIME_MAX_CHARGE)

    # 20〜0時に入庫、翌日8時以降に出庫
    elif DAYTIME_SERVICE_END <= entry < DAYTIME_END < TOMORROW_DAYTIME_START < leaving:

        usage_charge1 = get_usage_charge(entry, DAYTIME_SERVICE_END, DAYTIME_UNIT, BASIC_CHARGE, NIGHTTIME_MAX_CHARGE)
        usage_charge2 = get_usage_charge(TOMORROW_DAYTIME_START, DAYTIME_END, NIGHTTIME_UNIT, BASIC_CHARGE, NIGHTTIME_MAX_CHARGE)
        usage_charge3 = get_usage_charge(leaving, TOMORROW_DAYTIME_START, DAYTIME_UNIT, BASIC_CHARGE, DAYTIME_MAX_CHARGE)
        total_price = usage_charge1 + usage_charge2 + usage_charge3

    return total_price



def calc_okuruma_park_daisei_konyamati_1(entry, leaving):

    total_price = 0
    BASIC_CHARGE = 100
    TIME_UNIT = timedelta(minutes=20)
    NIGHTTIME_MAX_CHARGE = 600
    NIGHTTIME_SERVICE_START = datetime.strptime(f"{today_date} 20:00", datetime_format)
    NIGHTTIME_SERVICE_END = datetime.strptime(f"{tomorrow_date} 08:00", datetime_format)

    # 20時までに出庫する
    if leaving <= NIGHTTIME_SERVICE_START:
        usage_time = leaving - entry
        total_price = get_subtotal(usage_time,TIME_UNIT,BASIC_CHARGE)

    elif entry < NIGHTTIME_SERVICE_START <= leaving <= NIGHTTIME_SERVICE_END:
        usage_time1 = NIGHTTIME_SERVICE_START - entry
        usage_charge1 = get_subtotal(usage_time1,TIME_UNIT,BASIC_CHARGE)
        usage_charge2 = get_usage_charge(leaving, NIGHTTIME_SERVICE_START, TIME_UNIT, BASIC_CHARGE, NIGHTTIME_MAX_CHARGE)
        total_price = usage_charge1 + usage_charge2
    
    elif NIGHTTIME_SERVICE_START <= entry < leaving <= NIGHTTIME_SERVICE_END:
        total_price = get_usage_charge(leaving, entry, TIME_UNIT, BASIC_CHARGE, NIGHTTIME_MAX_CHARGE)

    return total_price
    



def calculations():
    calc_ap_park_kochi_higashi()
    calc_okuruma_park_daisei_konyamati_1()





