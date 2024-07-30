# import requests
# from bs4 import BeautifulSoup
# import json
# import time
# import random

# def extract_english_name(text):
#     start = text.find("(انگلیسی: ") + len("(انگلیسی: ")
#     end = text.find(")", start)
#     return text[start:end] if start != -1 and end != -1 else ""

# def get_random_user_agent():
#     user_agents = [
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
#         'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
#         'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
#     ]
#     return random.choice(user_agents)

# with open('names.json', 'r', encoding='utf-8') as f:
#     names = json.load(f)

# updated_names = []

# try:
#     counter = 0
#     while names:
#         counter += 1
#         print(f"Counter: {counter}, Remaining names: {len(names)}")
#         name_info = names.pop(0)
#         link = name_info['link']
        
#         while True:
#             headers = {'User-Agent': get_random_user_agent()}
#             response = requests.get(link, headers=headers)
            
#             if response.status_code != 200:
#                 print(f"Error {response.status_code}.Sleep for 1 minute.")
#                 time.sleep(60)  # 1 دقیقه صبر
#                 continue

#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             if "صفحه مورد نظر قفل شده است. لطفا لحظاتی بعد مراجعه کنید." in soup.text:
#                 print("Locked. Sleep for 10 minutes.")
#                 time.sleep(600)  # 10 دقیقه صبر
#             else:
#                 break
        
#         article = soup.find('article')
#         if article:
#             text = article.get_text()
#             english_name = extract_english_name(text)
#             name_info['english_name'] = english_name
#             print(f"Updated {name_info['name']} with English name: {english_name}")
        
#         updated_names.append(name_info)
        
#         with open('names_updated-1.json', 'w', encoding='utf-8') as f:
#             json.dump(updated_names, f, ensure_ascii=False, indent=4)
        
#         with open('names.json', 'w', encoding='utf-8') as f:
#             json.dump(names, f, ensure_ascii=False, indent=4)
        
#         sleep_time = random.randint(2, 7)
#         print(f"Sleep for {sleep_time} seconds.")
#         time.sleep(sleep_time)  # 5 تا 10 ثانیه صبر

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     # ذخیره داده‌های نهایی در فایل‌های JSON
#     with open('names_updated-1.json', 'w', encoding='utf-8') as f:
#         json.dump(updated_names, f, ensure_ascii=False, indent=4)
#     with open('names.json', 'w', encoding='utf-8') as f:
#         json.dump(names, f, ensure_ascii=False, indent=4)
#     print("Data saved to names_updated-1.json and names.json")


#! ============================================================================
import eng_to_ipa as ipa

import json


with open('names.json', 'r', encoding='utf-8') as f:
    names = json.load(f)

# دیکشنری تبدیل نمادهای IPA به متن انگلیسی
ipa_to_english = {
    'ə': 'a', 'ɪ': 'i', 'ʌ': 'u', 'ʊ': 'oo', 'æ': 'a', 'eɪ': 'ay',
    'ɔ': 'aw', 'ɔɪ': 'oy', 'aʊ': 'ow', 'aɪ': 'i', 'ɛ': 'e', 'oʊ': 'o',
    'ɑ': 'ah', 'dʒ': 'j', 'tʃ': 'ch', 'θ': 'th', 'ð': 'th', 'ʃ': 'sh',
    'ʒ': 'zh', 'ŋ': 'ng', 'ɡ': 'g', 'ɹ': 'r', 'ɾ': 't', 'ʔ': 'uh',
    'p': 'p', 'b': 'b', 't': 't', 'd': 'd', 'k': 'k', 'm': 'm',
    'n': 'n', 'f': 'f', 'v': 'v', 's': 's', 'z': 'z', 'h': 'h',
    'l': 'l', 'w': 'w', 'j': 'y', 'r': 'r', 'g': 'g', 'x': 'kh',
    'ā': 'a','š': 'sh','ā': '(w)','': 'a','ā': 'a',
}

# تابع تبدیل IPA به متن انگلیسی
def ipa_to_text(ipa_string):
    words = ipa_string['pronunciation'].split('/')[1]
    english_translation = []

    for word in words:
        translated_word = ''
        i = 0
        while i < len(word):
            for j in range(3, 0, -1):  # بررسی ترکیب‌های طولانی‌تر
                if i + j <= len(word) and word[i:i+j] in ipa_to_english:
                    translated_word += ipa_to_english[word[i:i+j]]
                    i += j
                    break
            else:
                translated_word += word[i]  # اگر نماد شناخته نشده باشد
                i += 1

        english_translation.append(translated_word)
    name = ''.join(english_translation)
    print(f'name: {name} - persian_name: {ipa_string["name"]}')
    return name
    

count = 0 
for name_info in names:
    ipa_to_text(name_info)
    count += 1
    # if count == 10:
    #     break


data =    {
        "name": "محمد مهدی",
        "link": "https://abadis.ir/fatofa/محمد-مهدی/",
        "gender": "پسر",
        "pronunciation": "/m.-mahdi/",
        "description": "ترکیب دو اسم محمد و مهدی ( ستوده و هدایت شده )، از نام های مرکب، محمّد و مهدی، مرکب از محمدبه معنای ...",
        "details": [
            "پسر",
            "عربی",
            "مذهبی و قرآنی"
        ],
        "english_name": "mohammad-mahdi",
        "numerology": {
            "destiny_number": 3,
            "personality_number": 6,
            "heart_desire_number": 1,
            "subconscious_self_number": 7,
            "alfabet_number" : [
                ["m", 4],
                ["o", 7],
                ["h", 5],
                ["a", 1],
                ["m", 4],
                ["m", 4],
                ["a", 1],
                ["d", 4],
                ["m", 4],
                ["a", 1],
                ["h", 5],
                ["d", 4],
                ["i", 9]
            ],
            "personality_traits": [
                "خلاق",
                "درمانگر",
                "مهربان",
                "متعهد",
                "مسئولیت پذیر"
            ]
        }
    }