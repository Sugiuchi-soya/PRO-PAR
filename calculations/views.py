from django.shortcuts import render
from django.views import generic
from accounts.models import Parking
from .calculations import *


# def top(request):
#     return render(request, "calculations/top.html",{})

Time = DateTime(today)

class Top(generic.ListView):
    template_name = "calculations/top.html"
    model = Parking
    ordering = "-created_at"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "トップ"
        context["today_date"] = Time.get_today_date()
        context["today_time"] = Time.get_today_time()
        context["tomorrow_date"] = Time.get_tomorrow_date()
        return context



