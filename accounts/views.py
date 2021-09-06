from django.shortcuts import render
from django.views import generic


# def management_screen(request):
#     return render(request, "accounts/management_screen.html",{})

class ManagementScreen(generic.TemplateView):
    template_name = "accounts/management_screen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "管理画面"
        return context


