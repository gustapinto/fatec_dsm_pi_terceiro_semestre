from django.shortcuts import redirect
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/dashb')

        return super(HomePageView, self).get(request, *args, **kwargs)
