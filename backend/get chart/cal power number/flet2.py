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
        1: "The Leader: You are a natural leader and have a strong sense of purpose. You are confident and assertive, and you have a strong desire to succeed.",
        2: "The Diplomat: You are a peacemaker and a mediator. You are diplomatic and tactful, and you have a strong sense of justice and fairness.",
        3: "The Communicator: You are a natural communicator and have a gift for expressing yourself. You are creative and imaginative, and you have a strong sense of humor.",
        4: "The Organizer: You are a natural organizer and have a strong sense of order. You are practical and reliable, and you have a strong work ethic.",
        5: "The Adventurer: You are a natural adventurer and have a strong sense of freedom. You are versatile and adaptable, and you have a strong sense of curiosity.",
        6: "The Nurturer: You are a natural nurturer and have a strong sense of responsibility. You are caring and compassionate, and you have a strong sense of family.",
        7: "The Seeker: You are a natural seeker and have a strong sense of spirituality. You are introspective and intuitive, and you have a strong sense of purpose.",
        8: "The Achiever: You are a natural achiever and have a strong sense of ambition. You are determined and focused, and you have a strong sense of success.",
        9: "The Humanitarian: You are a natural humanitarian and have a strong sense of compassion. You are selfless and generous, and you have a strong sense of empathy.",
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
        'name_match': 'Your power number is the same as your birth number.',
        'odd': "Both numbers are a person's name and birthday.",
        'even': 'Both numbers of name and birthday are even.',
        'not_match': 'Your strength number does not match your birth number.'
    }
    match_type = ('name_match' if nameNumber == birthNumber else
                  'odd' if nameNumber % 2 and birthNumber % 2 else
                  'even' if not nameNumber % 2 and not birthNumber % 2 else
                  'not_match')
    return name_match_characteristics[match_type]

def main(page: Page):
    page.title = "Power Number and Name Number Calculator"
    page.scroll = ft.ScrollMode.AUTO

    name_input = ft.TextField(label="Enter your name")
    day_input = ft.TextField(label="Enter day", keyboard_type=ft.KeyboardType.NUMBER)
    month_input = ft.TextField(label="Enter month", keyboard_type=ft.KeyboardType.NUMBER)
    year_input = ft.TextField(label="Enter year", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text()

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
        
        result_text.value = f"Your Power Number is: {birth_number}\n"
        result_text.value += f"Your Name Number is: {name_number}\n\n"
        result_text.value += f"Power Characteristics:\n{power_characteristics}\n\n"
        result_text.value += f"Suitable Investments:\n{', '.join(investments)}\n\n"
        result_text.value += f"Name Match:\n{name_match_result}\n"

        page.update()

    calculate_button = ft.ElevatedButton(text="Calculate", on_click=calculate)

    page.add(
        ft.Column([
            name_input,
            day_input,
            month_input,
            year_input,
            calculate_button,
            result_text
        ])
    )

ft.app(target=main, assets_dir="assets")
