'''
یه تابع میخوام که به ادرس https://abadis.ir/name/all/ یک درخوست ارسال کنه.
کد html اون رو بگیره و با ریجکس تمام تگ های <span class="boxName boxGirl" onclick="window.open('/fatofa/فاطمه/')"> رو
با دیتا داخلش به صورت لیست برگردونه.
'''
import requests
import re
# import pandas as pd
import json

from bs4 import BeautifulSoup

import pandas as pd
from time import sleep

def extract_info(html):
    pattern = re.compile(r'<span class="boxName.*?">.*?<a href="(.*?)".*?>(.*?)</a>.*?<i><hr>(.*?)</i>.*?<i><hr>(.*?)</i>', re.DOTALL)
    matches = pattern.findall(html)
    
    results = []
    for match in matches:
        link, name, gender, language = match
        results.append([name, link, gender, language])
    
    return {'Name': results[0][0], 'Link': results[0][1], 'Gender': results[0][2], 'Language': results[0][3]}

def get_names():
    base_url = 'https://abadis.ir/name/all/?pn='
    result = []
    for i in range(1, 101):
        print(f'Start Page ==> {i}')
        url = base_url + str(i)

        response = requests.get(url)
        response.raise_for_status()
        names = re.findall(r'(<span class="boxName box(Girl|Boy)".*?>.*?<\/span>)', response.text)
    
        for j in names:
            info = extract_info(j[0])
            result.append(info)
        
    print(f'Finished!')
    
    # Save to JSON file
    with open('names_info.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    
    return names

# get_names()



def base():

    # مرحله 1: خواندن فایل جیسون ورودی
    with open('names_info.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # print(data)

    base_url = "https://abadis.ir"
    result = []

    # مرحله 2 و 3: ارسال درخواست HTTP به هر لینک و استخراج اطلاعات مورد نظر
    num = 0
    for entry in data:
        num += 1
        json_data = json.loads(extract_info(entry['Link']))
        print(type(json_data))

        final_data = {
            "Name": entry['Name'],
            "Link": entry['Link'],
            "Gender": entry['Gender'],
            "Language": entry['Language'],
            "persian_name": json_data['persian_name'],
            "english_name": json_data['english_name'],
            "pronunciation": json_data['pronunciation'],
            "description": json_data['description']
        }
        print(f'Name number {num} ==> {json_data['english_name']}')
        write_to_csv(final_data)
        sleep()
        # if num == 5:
        #     break
        

    # print("اطلاعات استخراج و ذخیره شد.")

def write_to_csv(data):
    '''
    یک بار یک فایل csv ایجاد کنه و اطلاعات رو دونه دونه به آخر اون فایل اضافه کنه

    ستون ها: Name, Link, Gender, Language, persian_name, english_name, pronunciation, description
    '''
    try:
        df = pd.read_csv('data.csv')
    except:
        '''
        if data.csv not exist
        '''
        columns = ['Name', 'Link', 'Gender', 'Language', 'persian_name', 'english_name', 'pronunciation', 'description']
        df = pd.DataFrame(columns=columns)
        csv_file_path = 'data.csv'
        df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

    df = df._append(data, ignore_index=True)
    df.to_csv('data.csv', index=False, encoding='utf-8-sig')





def extract_info(url,number):

    full_url = f"https://abadis.ir{url}"
    result = []

    print(f"Sending request to {full_url} <====")
    try:
        response = requests.get(full_url)
        # response = requests.get('https://abadis.ir/fatofa/%D9%81%D8%B1%DB%8C%D8%AF%D9%87/')
        response.raise_for_status()
        html_article = extract_article(response.text)
        # print(html_article)

        # Regular expressions to extract the required fields
        name_pattern = re.compile(r'<b>اسم:</b> ([^()]+)')
        pronunciation_pattern = re.compile(r'\(تلفظ: ([^\)]+)\)')
        persian_name_pattern = re.compile(r'\(فارسی: ([^\)]+)\)')
        english_name_pattern = re.compile(r'\(انگلیسی: ([^\)]+)\)')
        description_pattern = re.compile(r'<b> معنی:<\/b> (.+?)<br>')

        # Extracting the values using the regular expressions
        name_match = name_pattern.search(html_article)
        pronunciation_match = pronunciation_pattern.search(html_article)
        persian_name_match = persian_name_pattern.search(html_article)
        english_name_match = english_name_pattern.search(html_article)
        description_match = description_pattern.search(html_article)

        # Creating the JSON structure
        result = {
            "Name": name_match.group(1) if name_match else '',
            "description": description_match.group(1) if description_match else '',
            "persian_name": persian_name_match.group(1) if persian_name_match else '',
            "english_name": english_name_match.group(1) if english_name_match else '',
            "pronunciation": pronunciation_match.group(1) if pronunciation_match else ''
        }

        # Printing the result as a JSON string
        return json.dumps(result, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"number ===> {number} <===  \n Error: {e}")
        result = {
            "Name": '',
            "description": '',
            "persian_name": '',
            "english_name": '',
            "pronunciation": ''
        }

        # Printing the result as a JSON string
        return json.dumps(result, ensure_ascii=False, indent=4)



def extract_article(html):
    # ریجکس برای یافتن بخش تگ دارای t="فرهنگ اسم ها"
    # print(html)
    regex = r"<div class='lun' t='فرهنگ اسم ها'>.*?<\/article><\/div><\/div>"
    
    # یافتن بخش مورد نظر با ریجکس
    match = re.search(regex, html, re.DOTALL)
    if not match:
        return None
    
    # استخراج HTML بخش مورد نظر
    section_html = match.group(0)
    
    # تجزیه و تحلیل HTML با BeautifulSoup
    soup = BeautifulSoup(section_html, 'html.parser')
    
    # یافتن تگ article
    article_tag = soup.find('article')
    return str(article_tag)


# base()
for i in range(1, 10):
    print(f"Page number {i}")
    sleep(3)
    #     break
