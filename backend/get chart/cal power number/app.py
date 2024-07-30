import os
from tkinter import *
from tkinter import messagebox

def persian_to_jd(day, month, year):
    epbase = year - 474
    epyear = 474 + (epbase % 2820)
    mdays = (month - 1) * 31 if month <= 7 else (month - 1) * 30 + 6
    jd = day + mdays + ((epyear * 682 - 110) // 2816) + \
         (epyear - 1) * 365 + (epbase // 2820) * 1029983 + (1948320.5 - 1)
    return jd

def jd_to_gregorian(jd):
    jd += 0.5
    z = int(jd)
    f = jd - z
    a = z if z < 2299161 else z + 1 + int((z - 1867216.25) / 36524.25) - int(int((z - 1867216.25) / 36524.25) / 4)
    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)
    day = b - d - int(30.6001 * e) + f
    month = e - 1 if e < 14 else e - 13
    year = c - 4716 if month > 2 else c - 4715

    return int(day), int(month), int(year)

def convert_date(day, month, year):
    if year < 1500:
        jd = persian_to_jd(day, month, year)
        return jd_to_gregorian(jd)
    return day, month, year

def reduce_to_single_digit(number):
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number

def find_name_number(name):
    letter_weights = {chr(i): (i - 96) % 9 or 9 for i in range(97, 123)}
    name_number = ''.join(str(letter_weights[char]) for char in name.lower() if char.isalpha())
    return reduce_to_single_digit(int(name_number))

def print_power_characteristics(birthNumber):
    power_characteristics_caption = {
        1: '''
        
        The Leader: You are a natural leader and have a strong sense of purpose. You are confident and assertive, and you have a strong desire to succeed.
        
        ابر قدرت شما رهبری است:
        چراغ راه، پرانرژی، العام بخش، رفع نیاز اطرافیان ، مغرور و خودخواه

        کلید موفقیت:
        1- باید با افزایش دانش خود در زمینه های رهبری به دیگران کمک هم کمک کنند و توجه کنند

        خانه های غالب و مهم:
        1-4-6-12

        سیاره های غالب و مهم:
        خورشید - پلوتو - نپتون - مشتری
        Sun - Pluto - Neptune - Jupiter

        ''',
        2: '''
        
        The Diplomat: You are a peacemaker and a mediator. You are diplomatic and tactful, and you have a strong sense of justice and fairness.
        
        ابر قدرت شما دیپلماتی است:
        به شدت روابط عمومی بالا و موقع در روابط عمومی

        کلید موفقیت:
        1- برای موفقیت نیاز به مشاوران خیلی خوبی دارند.
        2- باید از توانایی های خود در ارتباطات استفاده کنند.
        
        خانه های غالب و مهم:
        2-3-4-8

        سیاره های غالب و مهم:
        ماه - زحل - زهره - نود شمالی
        Moon - Saturn - Venus - North Node

        ''',
        3: '''
        
        The Communicator: You are a natural communicator and have a gift for expressing yourself. You are creative and imaginative, and you have a strong sense of humor.
        
        ابر قدرت شما خوش بینی است:
        به شدت علاقه به زندگی، ناامید نشدن، خوش شانس، این ها افراد بشدت خوش شانسی و خر شانسی هستند.
        یه ارث خوبی بهشون میرسه.

        کلید موفقیت:
        1- نیاز دارن به تلاش برای ارتقا و توسعه خودشون.
        2- باید مطالعه زیاد بکنند.
        
        خانه های غالب و مهم:
        2 - 8 - 10 - 12

        سیاره های غالب و مهم:
        خورشید - ماه - مشتری - اورانوس
        Sun - Moon - Jupiter - Uranus
        

        ''',
        4: '''
        
        The Organizer: You are a natural organizer and have a strong sense of order. You are practical and reliable, and you have a strong work ethic.
        
        ابر قدرت شما کار است:
        به شدت سخت کوش، اصلا روی حرف کسی حساب نمیکنند، میل به ثبات دارند.
        ترید برای این افراد اصلا خوب نیست

        کلید موفقیت:
        1- باید با کار و تلاش به هدف های خود برسند.
        
        خانه های غالب و مهم:
        1 - 4 - 6 - 12

        سیاره های غالب و مهم:
        مشتری - پلوتو - اورانوس
        Jupiter - Pluto - Uranus
        
        
        ''',
        5: '''
        
        The Adventurer: You are a natural adventurer and have a strong sense of freedom. You are versatile and adaptable, and you have a strong sense of curiosity.
        
        ابر قدرت شما کنج کاوی است:
        اسفنج اطلاعات، به شدت آزاد، شیفته اطلاعات و تحقیق و علم جدید،
        دوست دارن مستقل باشند.

        کلید موفقیت:
        1- مهارت های ارتباطی خودشون رو تقویت کنند تا بتونند ارتباط خوبی با دیگران داشته باشند،
        بتونن منظورشون رو به خوبی برسونند.
        
        خانه های غالب و مهم:
        8 - 9 - 10 - 12

        سیاره های غالب و مهم:
        خورشید - نپتون - لیلیت - عطارد
        Sun - Neptune - Lilith - Mercury
        
        ''',
        6: '''
        
        The Nurturer: You are a natural nurturer and have a strong sense of responsibility. You are caring and compassionate, and you have a strong sense of family.
        
        ابر قدرت شما عشق است:
        به شدت زیبا، فریبنده، جذاب،
        شش عدد شیطان هست به همین خاطر این افراد ظاهر شیطانی دارند.

        کلید موفقیت:
        1- هرچه قدر این عشق رو خرج کمک به دیگران بکنند موفقتر میشند.
        در زمینه های پزشکی و ...
        
        خانه های غالب و مهم:
        2 - 4 - 7 - 12

        سیاره های غالب و مهم:
        خورشید - ماه - زحل - زهره
        Sun - Moon - Saturn - Venus
        
        ''',
        7: '''
        
        The Seeker: You are a natural seeker and have a strong sense of spirituality. You are introspective and intuitive, and you have a strong sense of purpose.
        
        ابر قدرت شما حرکت است:
        دائما فعال، فداکار، اهل مطالعه، اهل تحقیق، اهل ورزش، اهل سفر

        کلید موفقیت:
        1- بینش و دانش بالا در زمینه های مختلف چه شغلی و چه زندگی شخصی
        
        خانه های غالب و مهم:
        4 - 6 - 9 - 11

        سیاره های غالب و مهم:
        خورشید - مشتری - عطارد - مریخ
        Sun - Jupiter - Mercury - Mars
        
        ''',
        8: '''
        
        The Achiever: You are a natural achiever and have a strong sense of ambition. You are determined and focused, and you have a strong sense of success.
        
        ابر قدرت شما مقیاس است:
        مغز دائما درحال سیستم سازی است، آهن ربا مالی هستند.
        همش محاسبه میکنند، 
        سگ شانس هستند در ترید

        کلید موفقیت:
        1- اقتصاد بخونند
        
        خانه های غالب و مهم:
        2 - 4 - 6 - 8

        سیاره های غالب و مهم:
        مشتری - مریخ - کایرون
        Jupiter - Mars - Chiron
        
        ''',
        9: '''
        
        The Humanitarian: You are a natural humanitarian and have a strong sense of compassion. You are selfless and generous, and you have a strong sense of empathy.
        
        ابر قدرت شما خِرَد است:
        باهوش و با استعداد

        کلید موفقیت:
        1- به دیگران کمک کنند و مشاوره بدن
        
        خانه های غالب و مهم:
        9 - 10 - 11 - 12

        سیاره های غالب و مهم:
        خورشید - عطارد - مشتری - مریخ
        Sun - Mercury - Jupiter - Mars
        
        ''',
    }
    return power_characteristics_caption.get(birthNumber, 'Unknown characteristic')

def investment(birthNumber):
    investment_options = {
        'Stock Market': [1,2,3,4,6,7,8,9],
        'Tried': [1,7,8,9],
        'Gold and Metals': [2,3,5]
    }
    suitable_investments = [key for key, numbers in investment_options.items() if birthNumber in numbers]
    return suitable_investments

def name_match(nameNumber, birthNumber):
    if nameNumber == birthNumber:
        return 'Your power number is the same as your birth number.'
    elif nameNumber % 2 and birthNumber % 2:
        return "Both numbers are a person's name and birthday."
    elif not nameNumber % 2 and not birthNumber % 2:
        return 'Both numbers of name and birthday are even.'
    else:
        return 'Your strength number does not match your birth number.'

def main_menu():
    def calculate():
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        day, month, year = convert_date(day, month, year)
        birthNumber = reduce_to_single_digit(int(f"{day}{month}{year}"))
        nameNumber = find_name_number(name)
        
        power_char = print_power_characteristics(birthNumber)
        investments = investment(birthNumber)
        name_match_res = name_match(nameNumber, birthNumber)
        
        result = f"Power Number: {birthNumber}\nName Number: {nameNumber}\n\nPower Characteristics:\n{power_char}\n\nInvestment Options:\n{', '.join(investments)}\n\nName Match:\n{name_match_res}"
        
        messagebox.showinfo("Results", result)
    
    root = Tk()
    root.title("Power Number and Name Number Calculator")

    # text.tag_configure('tag-right', justify='right')
    # text.insert('end', 'text ' * 10, 'tag-right')
    # text.grid()
    
    Label(root, text=":نام به انگلیسی").grid(row=0, column=1, padx=10, pady=10)
    name_entry = Entry(root)
    name_entry.grid(row=0, column=0, padx=10, pady=10)
    
    Label(root, text=": روز تولد").grid(row=1, column=1, padx=10, pady=10)
    day_entry = Entry(root)
    day_entry.grid(row=1, column=0, padx=10, pady=10)
    
    Label(root, text=": ماه تولد").grid(row=2, column=1, padx=10, pady=10)
    month_entry = Entry(root)
    month_entry.grid(row=2, column=0, padx=10, pady=10)
    
    Label(root, text=": سال تولد").grid(row=3, column=1, padx=10, pady=10)
    year_entry = Entry(root)
    year_entry.grid(row=3, column=0, padx=10, pady=10)
    
    Button(root, text="محاسبه", command=calculate).grid(row=4, column=0, columnspan=2, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main_menu()
