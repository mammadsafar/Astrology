import requests
from bs4 import BeautifulSoup
import json
import time

names = []

for page_number in range(96, 101):
    url = f"https://abadis.ir/name/?pn={page_number}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch page {page_number}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')

    for box in soup.find_all("span", class_=["boxName boxGirl", "boxName boxBoy"]):
        name_tag = box.find("a")
        name = name_tag.text if name_tag else ""
        link = f"https://abadis.ir{name_tag['href']}" if name_tag else ""
        gender = "دختر" if "boxGirl" in box["class"] else "پسر"
        pronunciation = box.find("pr").text if box.find("pr") else ""
        description = box.find("p").text if box.find("p") else ""
        details = [i.text for i in box.find_all("i")]

        names.append({
            "name": name,
            "link": link,
            "gender": gender,
            "pronunciation": pronunciation,
            "description": description,
            "details": details
        })

    print(f"page {page_number} done.")
    
    time.sleep(5)

with open('names.json', 'w', encoding='utf-8') as f:
    json.dump(names, f, ensure_ascii=False, indent=4)
