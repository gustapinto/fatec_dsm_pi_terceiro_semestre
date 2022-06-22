from dataclasses import dataclass
from random import randint


@dataclass
class DashboardDataset:
    dados: list
    border_radius: int = 20

    def __gera_rgb(self):
        r = randint(0, 150)
        g = randint(0, 150)
        b = 255

        return f'rgb({r}, {g}, {b})'

    def as_dict(self):
        colors = [self.__gera_rgb() for _ in self.dados]
        data = [{'x': l, 'y': d} for l, d in self.dados]

        return {
            'data': data,
            'backgroundColor': colors,
            'borderColor': colors,
            'borderRadius': self.border_radius,
        }
