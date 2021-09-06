from django.shortcuts import render
from django.views import generic

# def top(request):
#     return render(request, "calculations/top.html",{})

class Top(generic.TemplateView):
    template_name = "calculations/top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "トップ"
        return context



