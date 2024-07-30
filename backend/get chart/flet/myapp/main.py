import flet as ft
from flet import Page

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
    return power_characteristics_caption.get(birthNumber, "Unknown characteristic")

def investment(birthNumber):
    investment_options = {
        'Stock Market': [1, 2, 3, 4, 6, 7, 8, 9],
        'Trade': [1, 7, 8, 9],
        'Gold and Metals': [2, 3, 5]
    }
    investments = [key for key, numbers in investment_options.items() if birthNumber in numbers]
    return investments

def name_match(nameNumber, birthNumber):
    name_match_characteristics = {
        'name_match': 'اسمت به چارت تولدت میخوره.',
        'odd': "اسمت به چارت تولدت میخوره.",
        'even': 'اسمت به چارت تولدت میخوره.',
        'not_match': 'اسمت به چارت تولدت نمیخوره برای موفقیت بهتره عوض کنی.'
    }
    match_type = ('name_match' if nameNumber == birthNumber else
                  'odd' if nameNumber % 2 and birthNumber % 2 else
                  'even' if not nameNumber % 2 and not birthNumber % 2 else
                  'not_match')
    return name_match_characteristics[match_type]




def main(page: Page):
    page.title = "محاسبه‌گر عدد قدرت و عدد نام"
    page.scroll = ft.ScrollMode.AUTO
    description= ft.Text("""
    سلام و دورد

    اسم رو حتما به انگلیسی وارد کنید
    تارخ تولد رو میتونید هم به فارسی و هم به انگلیسی وارد کنید

    
    """, rtl= True)

    page.add(description)

    name_input = ft.TextField(label="نام خود را وارد کنید")
    day_input = ft.TextField(label="روز را وارد کنید", keyboard_type=ft.KeyboardType.NUMBER)
    month_input = ft.TextField(label="ماه را وارد کنید", keyboard_type=ft.KeyboardType.NUMBER)
    year_input = ft.TextField(label="سال را وارد کنید", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text(rtl=True)

    def calculate(e):
        name = name_input.value
        day = int(day_input.value)
        month = int(month_input.value)
        year = int(year_input.value)

        day, month, year = convert_date(day, month, year)
        birth_number = reduce_to_single_digit(int(f"{day}{month}{year}"))
        name_number = find_name_number(name)
        
        power_characteristics = print_power_characteristics(birth_number)
        investments = investment(birth_number)
        name_match_result = name_match(name_number, birth_number)
        
        result_text.value = f"عدد قدرت شما: {birth_number}\n"
        result_text.value += f"عدد نام شما: {name_number}\n\n"
        result_text.value += f"ویژگی های شما:\n{power_characteristics}\n\n"
        result_text.value += f"بهترین بازار برای سرمایه گذاری شما:\n{', '.join(investments)}\n\n"
        result_text.value += f"نام شما :\n{name_match_result}\n"

        page.update()

    def clear_fields(e):
        name_input.value = ""
        day_input.value = ""
        month_input.value = ""
        year_input.value = ""
        result_text.value = ""
        page.update()

    calculate_button = ft.ElevatedButton(text="محاسبه", on_click=calculate)
    clear_button = ft.ElevatedButton(text="پاک کردن", on_click=clear_fields)
    
    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        change_theme.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()
        
    page.theme_mode = ft.ThemeMode.DARK
    
    change_theme = ft.Switch(label="Light theme", on_change=theme_changed)
    page.add(
        ft.Column([
            change_theme,
            name_input,
            day_input,
            month_input,
            year_input,
            ft.Row([calculate_button, clear_button]),
            result_text
        ])
    )

ft.app(target=main, assets_dir="assets")