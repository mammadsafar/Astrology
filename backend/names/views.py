from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator

from pathlib import Path
import csv
import json

# from django_ratelimit.decorators import ratelimit

from .models import Name
from .moduls import moduls


BASE_DIR = Path(__file__).resolve().parent.parent

def import_data_from_text_file(file_path, error_file_path):
    print(file_path)
    # باز کردن فایل اطلاعات
    with open(file_path, 'r', encoding='utf-8') as f:
        names = json.load(f)

        error = []
        counter = 0
        print('Start!!!')
        for name in names:
            counter += 1
            print(f'{counter} - {name["name"]} - {name["persian-name"]}')
            try:
                # ایجاد یک نمونه از مدل و ذخیره آن
                Name.objects.create(
                    name=name['name'],
                    persian_name = name['persian-name'],
                    gender='boy' if name['gender'] == 'boy' else 'girl',
                    country = name['source'],
                    meaning = name['explain'],

                    desteni_number =moduls.find_desteni_name_number(name['name']),
                    motivation_number =moduls.find_motivation_name_number(name['name']),
                )
            except Exception as e:
                error.append({
                    'name': name,
                    'error': [str(e)]
                })
        print('Finish!!!')

    with open(error_file_path, 'w', encoding='utf-8') as f:
        json.dump(error, f, ensure_ascii=False, indent=4)

def import_data(request):
    if request.method == 'GET':
        file_path = f'/names/moduls/utils/full_nameniko.json'
        file_path = str(BASE_DIR) + str(file_path)

        error_file_path = f'/error_names1.json'
        error_file_path = str(BASE_DIR) + str(error_file_path)

        import_data_from_text_file(file_path, error_file_path)


# def import_data_from_text_file(file_path, error_file_path):
#     print(file_path)
#     # باز کردن فایل اطلاعات
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
        
#         # باز کردن فایل خطاها
#         with open(error_file_path, 'w') as error_file:
#             error_writer = csv.writer(error_file)
            
#             for row in reader:
#                 name, gender, usage_percentage = row
#                 try:
#                     # ایجاد یک نمونه از مدل و ذخیره آن
#                     Name.objects.create(
#                         name=name,
#                         gender='boy' if gender == 'M' else 'girl',
#                         Usage_percentage=usage_percentage
#                     )
#                 except ValidationError as e:
#                     # نوشتن خطاها به فایل خطاها
#                     error_writer.writerow(row + [str(e)])
#                 except Exception as e:
#                     # نوشتن خطاها به فایل خطاها
#                     error_writer.writerow(row + [str(e)])
# def import_data(request):
#     if request.method == 'GET':
#         for i in range(1880, 2024):
#             file_path = f'/get chart/claculate project/names/yob{i}.txt'
#             error_file_path = f'/error_names{i}.txt'
#             file_path = str(BASE_DIR) + str(file_path)
#             error_file_path = str(BASE_DIR) + str(error_file_path)
#             import_data_from_text_file(file_path, error_file_path)

def change_data(request):
    if request.method == 'GET':
        '''
        من یک مدل دارم به نام Name
        میخوام یک محاسبه روی تک تک رکوردها انجام بدم
        و پاسخش رو روی همون رکورد ذخیره کنم
        حدود 100 هزار رکورد دارم
        چطوری این کار رو انجام بدم؟
        '''
        names = Name.objects.all()
        counter = 0
        for name in names:
            counter += 1
            print(f'{counter} - {name.name}')
            desteni_name_number = moduls.find_desteni_name_number(name.name)
            motivation_name_number = moduls.find_motivation_name_number(name.name)
            name.desteni_number = desteni_name_number
            name.motivation_number = motivation_name_number
            name.save()

        return HttpResponse(f"counter: {counter} is done")



# @ratelimit(key='ip', rate='10000/h', method='ALL', block=True)
def names_list(request):
    if request.method == 'GET':
        valid_desteni_number = request.GET.get('desteni_number', 1)
        valid_motivation_number = request.GET.get('motivation_number', 1)
        valid_gender = request.GET.get('gender', 'both')
        
        query = {}
        if valid_desteni_number != 'False':
            query['desteni_number'] = valid_desteni_number
        if valid_motivation_number != 'False':
            query['motivation_number'] = valid_motivation_number
        if valid_gender != 'both':
            query['gender'] = valid_gender

        results = Name.objects.filter(**query).order_by('-created_at')
        count = results.count()
        # results = Name.objects.filter(
        #     desteni_number=desteni_number,
        #     motivation_number=motivation_number,
        #     gender=gender
        # ).order_by('-created_at')

        # Get the page number from the query parameters
        page_number = request.GET.get('page', 1)
        
        # Create a Paginator object with the results and the desired number of items per page
        paginator = Paginator(results, 100)  # 100 items per page
        # Get the paginated page
        page_obj = paginator.get_page(page_number)

        # Serialize the results
        results_list = list(page_obj.object_list.values())

        # Return the paginated results along with pagination info
        response_data = {
            'desteni_number': valid_desteni_number,
            'motivation_number': valid_motivation_number,
            'gender': valid_gender,
            'results': results_list,
            'count': count,
            'page': page_obj.number,
            'num_pages': paginator.num_pages,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
        }
        # print(response_data)
        # return JsonResponse(response_data, safe=False)

        return render(request, 'names_list.html', response_data)
