from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
import os
import pandas as pd
from dataclasses import dataclass
import datetime

@dataclass
class DD:
    day: str
    month: str
    year: str

    def __str__(self):
        d = datetime.date(year=int(self.year), month=int(self.month), day=int(self.day))
        return d.strftime("%d.%m.%Y")


def index(request):
    template = "predict/index.html"
    title = "Главная страница"
    description = "Главная страница сайта!"
    context = {
        "description": description,
        "title": title,
    }
    return render(request, template, context)


def seasons(request):
    template = "predict/seasons.html"
    title = "Сезоны"
    graphics = "Тут будут графики сезоны. МНОГО!"
    context = {
        "graphics": graphics,
        "title": title,
    }
    return render(request, template, context)


def dynamics(request):
    template = "predict/dynamic.html"
    title = "Динамика спроса"
    graphics = "Тут будут графики динамика спроса. МНОГО!"
    context = {
        "graphics": graphics,
        "title": title,
    }
    return render(request, template, context)


def select_dynamics(sorg:str, sdst: str, flight, date_flight: DD, class_type: str) -> pd.DataFrame:
    print(sorg, sdst, flight, date_flight, class_type)
    df = pd.read_csv(os.path.join(settings.DATASETS_DIR,
        f"{date_flight.year}/CLASS_{date_flight.month}{date_flight.year}",
        f"CLASS_{date_flight.month}{date_flight.year}.csv"), sep=";")
    print(df.columns)


    df = df[(df["FLT_NUM"] == int(flight)) & (df["SEG_CLASS_CODE"] == class_type) &
            (df["DD"] == str(date_flight)) & (df["SORG"] == sorg) & (df["SDST"] == sdst)]
    return df

def select(*args):
    from math import cos
    x = range(100)
    y = list(map(lambda el: el ** 2 - 4*el * cos(el), x))
    return (x, [y])

@dataclass
class DataClass:
    pass

def profile_demand(request):

    # http://127.0.0.1:8000/demand/?sorg=AER&sdst=SVO&flight=1125&date_flight=01-07-2018&class_type=L
    template = "predict/demand.html"
    title = "Динамика спроса"
    graphics = []

    params = ["sorg", "sdst", "flight", "date_flight", "class_type"]
    values = {}
    for param in params:
        v = request.GET.get(param)
        if v is not None:
            if param == "date_flight":
                values[param] = v.split("-")
                continue
            values[param] = v

    dynamics_df = select_dynamics(sorg=values.get("sorg"), sdst=values.get("sdst"), flight=values.get("flight"),
                                  date_flight=DD(day=values.get("date_flight")[0],
                                                 month=values.get("date_flight")[1],
                                                 year=values.get("date_flight")[2]),
                                  class_type="L")

    data_unit = [list(dynamics_df["SDAT_S"]), [list(dynamics_df["AU"])]]

    graphics.append({"id": f"AU", "name": f"Доступные кресла по салонам (к продаже с учётом перебронирования) [AU]", "xvalues": data_unit[0], "data": []})
    for line in data_unit[1]:
        graphics[-1]["data"] += [
            {"label": "AU", "array": list(line)},
        ]

    data_unit = [list(dynamics_df["SDAT_S"]), [list(dynamics_df["SA"])]]

    # ---

    graphics.append({"id": f"SA", "name": f"Доступные кресла по салонам [SA]",
                     "xvalues": data_unit[0], "data": []})
    for line in data_unit[1]:
        graphics[-1]["data"] += [
            {"label": "SA", "array": list(line)},
        ]

    # ---

    data_unit = [list(dynamics_df["SDAT_S"]), [list(dynamics_df["PASS_BK"])]]

    graphics.append({"id": f"PASS_BK", "name": f"Колличество забронированных пассажиров [PASS_BK]",
                     "xvalues": data_unit[0], "data": []})
    for line in data_unit[1]:
        graphics[-1]["data"] += [
            {"label": "PASS_BK", "array": list(line)},
        ]


    # --

    ata_unit = [list(dynamics_df["SDAT_S"]), [list(dynamics_df["PASS_DEP"])]]

    graphics.append({"id": f"PASS_DEP", "name": f"Колличество пролетевших пассажиров [PASS_DEP]",
                     "xvalues": data_unit[0], "data": []})
    for line in data_unit[1]:
        graphics[-1]["data"] += [
            {"label": "PASS_DEP", "array": list(line)},
        ]

    histograms = []

    histograms.append(
        {"id": f"Hist",
         "name": f"name",
         "data": [3, 1, 2, 5, 3, 10, 6, 7, 4],
         "xvalues": [],
         "text": f'Длина последней свечи: '
         },
    )

    context = {
        "graphics": graphics,
        "histograms": histograms,
        "title": title,
    }

    return render(request, template, context)
