from dataclasses import dataclass
from json import dumps
from random import randint

from django.http import HttpResponse
from django.views.generic import TemplateView

@dataclass
class DashboardDataset:
    label_data_relation: list
    border_radius: int = 20

    def __generate_color(self):
        r = randint(0, 150)
        g = randint(0, 150)
        b = 255

        return f'rgb({r}, {g}, {b})'

    def as_dict(self):
        colors = [self.__generate_color() for _ in self.label_data_relation]
        data = [{'x': l, 'y': d} for l, d in self.label_data_relation]

        return {
            'data': data,
            'backgroundColor': colors,
            'borderColor': colors,
            'borderRadius': 20,
        }


class DashbView(TemplateView):
    template_name = "dashb.html"

    def get_context_data(self, **kwargs):
        dataset = DashboardDataset([
            ('Spy x Family', 314),
            ('Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu', 64),
            ('Kaguya-sama wa Kokurasetai: Ultra Romantic', 44),
            ('Aharen-san wa Hakarenai', 41),
            ('Tate no Yuusha no Nariagari Season 2', 35),
            ('Tomodachi Game', 22),
            ('Agotome Game Sekai wa Mob ni Kibishii Sekai desuo', 22)
        ])

        chart_data = {
            'datasets': [dataset.as_dict()]
        }

        context = super(DashbView, self).get_context_data(**kwargs)
        context['chart_data'] = dumps(chart_data)

        return context
