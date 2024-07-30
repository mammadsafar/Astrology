from kerykeion import Report, AstrologicalSubject

kanye = AstrologicalSubject("Marjan", 1979, 6, 12, 3, 30, "Mashhad")
report = Report(kanye)
report.print_report()
# from kerykeion import Report, AstrologicalSubject#, KerykeionChartSVG

# kanye = AstrologicalSubject("Marjan", 1979, 6, 12, 3, 30, "Mashhad")
# svg = KerykeionChartSVG(kanye, new_output_directory='svg')
# svg.makeSVG()
# print(kanye)
# print(kanye.sun)
# print(kanye.moon)
# print(kanye.mercury)
# print(kanye.venus)
# print(kanye.mars)
# print(kanye.jupiter)
# print(kanye.saturn)
# print(kanye.uranus)
# print(kanye.neptune)
# print(kanye.pluto)
# print(kanye.mean_node)
# print(kanye.true_node)
# print(kanye.chiron)

# print(kanye.first_house)
# print(kanye.moon.element)

# report = Report(kanye)
# report.print_report()
# print(report.get_report_title())
# print(report.get_data_table())
# print(report.get_planets_table())
# print(report.get_houses_table())
# print(report.get_full_report())
# print(kanye)


# import requests

# cookies = {
#     # 'cidleft': 'nocid',
#     # '_gid': 'GA1.2.76981680.1718211229',
#     # '_ga': 'GA1.1.2117042574.1718211229',
#     # 'pcount': '2',
#     # '_ga_B5RG4ZCVN7': 'GS1.1.1718211228.1.1.1718211238.0.0.0',
# }

# headers = {
#     # 'Accept': '*/*',
#     # 'Accept-Language': 'en-GB,en;q=0.9,fa-IR;q=0.8,fa;q=0.7,en-US;q=0.6',
#     # 'Connection': 'keep-alive',
#     # # 'Cookie': 'cidleft=nocid; _gid=GA1.2.76981680.1718211229; _ga=GA1.1.2117042574.1718211229; pcount=2; _ga_B5RG4ZCVN7=GS1.1.1718211228.1.1.1718211238.0.0.0',
#     # # 'Referer': 'https://www.astro.com/cgi/ade.cgi?ract=xx68747470733a2f2f7777772e617374726f2e636f6d2f6367692f63686172742e6367693f&lang=e&btyp=w2gw',
#     # 'Sec-Fetch-Dest': 'empty',
#     # 'Sec-Fetch-Mode': 'cors',
#     # 'Sec-Fetch-Site': 'same-origin',
#     # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
#     # 'X-Requested-With': 'XMLHttpRequest',
#     # 'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#     # 'sec-ch-ua-mobile': '?0',
#     # 'sec-ch-ua-platform': '"Windows"',
# }

# params = {
#     'q': 'tehran',
#     'func': 'place_query',
#     'sctr': 'IRAN',
#     'lang': 'e',
# }

# response = requests.get('https://www.astro.com/cgi/adejs.cgi', params=params, cookies=cookies, headers=headers)

# print(response.text)