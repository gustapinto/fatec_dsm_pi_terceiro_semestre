from json import dumps

from django.views.generic import TemplateView

from .connectors import MongoConnector
from .structs import DashboardDataset


class DashbView(TemplateView):
    template_name = "dashb.html"

    def get_context_data(self, **kwargs):
        connector = MongoConnector()

        mongo_data = connector.obtem_dados_grafico()
        chart_data = {'datasets': [DashboardDataset(mongo_data).as_dict()]}

        context = super(DashbView, self).get_context_data(**kwargs)
        context['chart_data'] = dumps(chart_data)
        context['animes'] = connector.obtem_dados_lista()

        return context
