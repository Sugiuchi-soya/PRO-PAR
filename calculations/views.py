from django.shortcuts import render, redirect
from accounts.models import Parking
from .calculations import *
from django.conf import settings


def top(request):
    Time = DateTime(today)
    return render(request, "calculations/top.html", {
        "today_date" : Time.get_today_date(),
        "today_time" : Time.get_today_time(),
        "tomorrow_date" : Time.get_tomorrow_date()
    })

def list(request):
    parkings = Parking.objects.all()

    if request.method == "POST":
        entry_date = request.POST.get("entry_date")
        entry_time = request.POST.get("entry_time")
        leaving_date = request.POST.get("leaving_date")
        leaving_time = request.POST.get("leaving_time")

        entry = datetime.strptime(f"{entry_date} {entry_time}", "%Y-%m-%d %H:%M")
        leaving = datetime.strptime(f"{leaving_date} {leaving_time}", "%Y-%m-%d %H:%M")
        usage_charge = calculate_ap_park_kochi_higashi(entry, leaving)

        for parking in parkings:
            parking.charge = usage_charge
        Parking.objects.bulk_update(parkings, fields = ["charge"])
        
    return render(request, "calculations/list.html", {
        "GOOGLEMAPS_API_KEY" : getattr(settings, "GOOGLEMAPS_API_KEY"),
        "parkings" : parkings,
        "init_adress" : "高知県高知市はりまや町１丁目６−１１"
    })

def reflect_the_address(request, id):
    
    parking = Parking.objects.get(id=id)

    return render(request, "calculations/map.html", {
        "GOOGLEMAPS_API_KEY" : getattr(settings, "GOOGLEMAPS_API_KEY"),
        "parking" : parking,
        "init_adress" : "高知県高知市はりまや町１丁目６−１１"
    })

