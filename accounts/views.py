from django.shortcuts import render

def management_screen(request):
    return render(request, "accounts/management_screen.html",{})

