
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class DashbView(TemplateView):
    template_name = "dashb.html"

#def dashb(request):
   # return HttpResponse('teste')
    