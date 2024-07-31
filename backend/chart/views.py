from django.shortcuts import render
from django.http import HttpResponse
from kerykeion import Report, AstrologicalSubject, KerykeionChartSVG

from .models import Home, Zodiac, Plant, PlantLayer, Detail, Psychology
from city.models import City


def get_chart(request):
    if request.method == "GET":
        city = City.objects.all()

        return render(request, "get_data.html", {'city': city})

    if request.method == "POST":
        name = request.POST.get("name", "")
        birthday = request.POST.get("birthday", "")
        year, month, day = map(int, birthday.split('-'))
        time = request.POST.get("time", "")
        hour, minute = map(int, time.split(':'))
        city_id = request.POST.get("city", "")
        map_city = City.objects.get(id=city_id)

        subject = AstrologicalSubject(
            name,
            year,
            month,
            day,
            hour,
            minute,
            lng=map_city.latitude,
            lat=map_city.longitude,
            city=map_city.name,
            online=False,
            tz_str="Asia/Tehran",
            geonames_username='mammadsafar'
        )
        
        svg = KerykeionChartSVG(subject, new_output_directory='media/chart/svg')
        svg.makeSVG()

        astro_chart = {
            'sun': subject.sun,
            'moon': subject.moon,
            'mercury': subject.mercury,
            'venus': subject.venus,
            'mars': subject.mars,
            'jupiter': subject.jupiter,
            'saturn': subject.saturn,
            'uranus': subject.uranus,
            'neptune': subject.neptune,
            'pluto': subject.pluto,
            'mean_node': subject.mean_node,
            'true_node': subject.true_node,
            'chiron': subject.chiron,
        }

        # print(get_plant_id(request, astro_chart['sun']))
        # print(get_zodiac_id(request, astro_chart['sun']))
        data = {'plants': []}

        for  _, astro_obj in astro_chart.items():

            try:
                # print(astro_obj)
                plant = Plant.objects.get(nationalName=astro_obj.name)
                zodiac = Zodiac.objects.get(sign=astro_obj.sign)
                # print(plant, zodiac)
                data_detail = Detail.objects.get(plant=plant.id, zodiac=zodiac.id)
                
                if data_detail:
                    # print(data_detail)
                    astro_chart_data = dict()
                    astro_chart_data['plant'] = astro_obj.name
                    astro_chart_data['p_image'] = plant.image.url
                    astro_chart_data['zodiac'] = zodiac.nationalName
                    astro_chart_data['z_image'] = zodiac.image.url
                    astro_chart_data['description'] = data_detail
                    data['plants'].append(astro_chart_data)

            except Exception as e:
                # print(e)
                continue
        svg_path = '/media/chart/svg/' + name + ' - Natal Chart.svg'
        print({'data': data, 'svg': svg_path})
        return render(request, "Astrology_chart.html", {'data': data, 'svg': svg_path})


def get_plant_id(plant):
    plant = Plant.objects.get(nationalName=plant.name)
    return plant.id


def get_zodiac_id(zodiac):
    zodiac = Zodiac.objects.get(sign=zodiac.sign)
    return zodiac.id
