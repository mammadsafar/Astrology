# Powered by: https://mammadsafar.ir/
import os
import msvcrt

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

    print(f"Your birth date in Gregorian: {int(month)}/{int(day)}/{int(year)}\n")
    return int(day), int(month), int(year)

def convert_date(day, month, year):
    if year < 1500:
        print(f"Your birth date in jalali: {year}/{month}/{day}")
        jd = persian_to_jd(day, month, year)
        return jd_to_gregorian(jd)
    
    print(f"Your birth date in Gregorian: {month}/{day}/{year}\n")
    return day, month, year

def reduce_to_single_digit(number):
    while number > 9:
        number = sum(int(digit) for digit in str(number))
        if number == 11 or number == 22 or number == 33:
            return number
    return number

def find_name_number(name):
    letter_weights = {chr(i): (i - 96) % 9 or 9 for i in range(97, 123)}
    name_number = ''.join(str(letter_weights[char]) for char in name.lower() if char.isalpha())
    return reduce_to_single_digit(int(name_number))

def print_power_characteristics(birthNumber):
    # Define the power characteristics for each number
    power_characteristics_caption = {
        1: ''''

        The Leader: You are a natural leader and have a strong sense of purpose. You are confident and assertive, and you have a strong desire to succeed.

        Your superpower is leadership:
        A beacon of light, energetic, generous, meeting the needs of those around, proud and selfish

        the key of success:
        1- They should help and pay attention to others by increasing their knowledge in the fields of leadership

        Dominant and important houses:
        1-4-6-12

        Dominant and important planets:
        Sun - Pluto - Neptune - Jupiter

        ''',
        2: ''''

        The Diplomat: You are a peacemaker and a mediator. You are diplomatic and tactful, and you have a strong sense of justice and fairness.

        Your superpower is diplomacy:
        Extremely high public relations and timely in public relations

        the key of success:
        1- They need very good advisors to succeed.
        2- They should use their abilities in communication.

        Dominant and important houses:
        2-3-4-8

        Dominant and important planets:
        Moon - Saturn - Venus - North Node

        ''',
        3: ''''

        The Communicator: You are a natural communicator and have a gift for expressing yourself. You are creative and imaginative, and you have a strong sense of humor.

        Your superpower is optimism:
        Extremely interested in life, not disappointed, lucky, these are very lucky and lucky people.
        They will have a good inheritance.

        the key of success:
        1- They need to try to improve and develop themselves.
        2- They should study a lot.

        Dominant and important houses:
        2-8-10-12

        Dominant and important planets:
        Sun - Moon - Jupiter - Uranus


        ''',
        4: ''''

        The Organizer: You are a natural organizer and have a strong sense of order. You are practical and reliable, and you have a strong work ethic.

        Your superpower is work:
        Extremely hardworking, they don't count on anyone's words at all, they have a desire for stability.
        Trade is not good for these people

        the key of success:
        1- They should reach their goals with work and effort.

        Dominant and important houses:
        1 - 4 - 6 - 12

        Dominant and important planets:
        Jupiter - Pluto - Uranus


        ''',
        5: ''''

        The Adventurer: You are a natural adventurer and have a strong sense of freedom. You are versatile and adaptable, and you have a strong sense of curiosity.

        Your superpower is corner mining:
        Information sponge, extremely free, fascinated by information and research and new science.
        They like to be independent.

        the key of success:
        1- Strengthen their communication skills so that they can have a good relationship with others.
        They can convey their meaning well.

        Dominant and important houses:
        8-9-10-12

        Dominant and important planets:
        Sun - Neptune - Lilith - Mercury

        ''',
        6: ''''

        The Nurturer: You are a natural nurturer and have a strong sense of responsibility. You are caring and compassionate, and you have a strong sense of family.

        Your superpower is love:
        extremely beautiful, alluring, charming,
        There are six devils, that's why these people look devilish.

        the key of success:
        1- The more they spend this love to help others, the more successful they will be.
        In the fields of medicine and...

        Dominant and important houses:
        2-4-7-12

        Dominant and important planets:
        Sun - Moon - Saturn - Venus

        ''',
        7: ''''

        The Seeker: You are a natural seeker and have a strong sense of spirituality. You are introspective and intuitive, and you have a strong sense of purpose.

        Your superpower is movement:
        Constantly active, devoted, fond of studying, fond of research, fond of sports, fond of traveling

        the key of success:
        1- High insight and knowledge in various fields, both career and personal life

        Dominant and important houses:
        4-6-9-11

        Dominant and important planets:
        Sun - Jupiter - Mercury - Mars

        ''',
        8: ''''

        The Achiever: You are a natural achiever and have a strong sense of ambition. You are determined and focused, and you have a strong sense of success.

        Your superpower is scale:
        The brain is constantly being systematized, it is a financial magnet.
        They all calculate
        Lucky dogs are in the trade

        the key of success:
        1- Read economics

        Dominant and important houses:
        2-4-6-8

        Dominant and important planets:
        Jupiter - Mars - Chiron

        ''',9: ''''

        The Humanitarian: You are a natural humanitarian and have a strong sense of compassion. You are selfless and generous, and you have a strong sense of empathy.

        Your superpower is wisdom:
        Smart and talented

        the key of success:
        1- Help and advise others

        Dominant and important houses:
        9-10-11-12

        Dominant and important planets:
        Sun - Mercury - Jupiter - Mars

        ''',
    }

    # Print the power characteristics for the birth number
    characteristic = power_characteristics_caption.get(birthNumber, 'Unknown characteristic')
    print(f"\nThe power characteristics for the birth number {birthNumber} are:\n\n")
    print('-' * 60)
    print(characteristic)
    print('-' * 60 + '\n')

def investment(birthNumber):
    investment_options = {
        'stock_market': [1,2,3,4,6,7,8,9],
        'tried': [1,7,8,9],
        'gold_and_metals': [2,3,5]
    }
    investment_caption = {key: key.replace('_', ' ').title() for key in investment_options}
    print(f"\nThe investment characteristics for the birth number {birthNumber} are:\n")
    print("------------------------------------------------------------")
    for key, numbers in investment_options.items():
        if birthNumber in numbers:
            print(investment_caption[key])
    print("------------------------------------------------------------\n")

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
    print(f"\nThe name match characteristics for the name number {nameNumber} and birth number {birthNumber} are:\n")
    print("------------------------------------------------------------")
    print(name_match_characteristics[match_type])
    print("------------------------------------------------------------\n")


# Main program loop
def main_menu():
    print("""
    ____________________________________________________________________________________________________________
    |                                                                                                           |    
    |    This app calculates your Power Number and Name Number based on your birthdate and name.                |
    |    The Power Number is a single digit number that represents your personality traits.                     |
    |    The Name Number is a single digit number that represents your name's influence on your personality.    |
    |___________________________________________________________________________________________________________|


        """)
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')

        print("Menu:")
        print("1. Enter Name and Birthdate")
        print("2. Enter Name")
        print("3. Enter Birthdate")
        print("0. Exit")
        
        
        print("\n\nPlease choose an option: ")
        choice = msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                name = input("Please enter your name: ")
                day, month, year = (int(input(f"Please enter the {x}: ")) for x in ["day", "month", "year"])
                os.system('cls' if os.name == 'nt' else 'clear')

                day, month, year = convert_date(day, month, year)
                birthNumber = reduce_to_single_digit(int(f"{day}{month}{year}"))
                nameNumber = find_name_number(name)
                print(f"Your Power Number is: {birthNumber}")
                print(f"Your Name Number is: {nameNumber}\n")
                print_power_characteristics(birthNumber)
                investment(birthNumber)
                name_match(nameNumber, birthNumber)

                print("\n\n\n Press any key to continue...")
                msvcrt.getch()
                
                os.system('cls' if os.name == 'nt' else 'clear')
            elif choice == 2:
                name = input("Please enter your name: ")
                os.system('cls' if os.name == 'nt' else 'clear')

                print(f"Your Name Number is: {find_name_number(name)}")

                print("\n\n\n Press any key to continue...")
                msvcrt.getch()
                
                os.system('cls' if os.name == 'nt' else 'clear')
            elif choice == 3:
                day, month, year = (int(input(f"Please enter the {x}: ")) for x in ["day", "month", "year"])
                os.system('cls' if os.name == 'nt' else 'clear')

                day, month, year = convert_date(day, month, year)
                print(f"Your Power Number is: {reduce_to_single_digit(int(f'{day}{month}{year}'))}")

                print("\n\n\n Press any key to continue...")
                msvcrt.getch()
                
                os.system('cls' if os.name == 'nt' else 'clear')
            elif choice == 0:
                break
            else:
                print("Invalid choice. Please choose again.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main_menu()






def persian_translate():
    pass
    # power_characteristics_caption = {
    #     1: '''
        
    #     The Leader: You are a natural leader and have a strong sense of purpose. You are confident and assertive, and you have a strong desire to succeed.
        
    #     ابر قدرت شما رهبری است:
    #     چراغ راه، پرانرژی، العام بخش، رفع نیاز اطرافیان ، مغرور و خودخواه

    #     کلید موفقیت:
    #     1- باید با افزایش دانش خود در زمینه های رهبری به دیگران کمک هم کمک کنند و توجه کنند

    #     خانه های غالب و مهم:
    #     1-4-6-12

    #     سیاره های غالب و مهم:
    #     خورشید - پلوتو - نپتون - مشتری
    #     Sun - Pluto - Neptune - Jupiter

    #     ''',
    #     2: '''
        
    #     The Diplomat: You are a peacemaker and a mediator. You are diplomatic and tactful, and you have a strong sense of justice and fairness.
        
    #     ابر قدرت شما دیپلماتی است:
    #     به شدت روابط عمومی بالا و موقع در روابط عمومی

    #     کلید موفقیت:
    #     1- برای موفقیت نیاز به مشاوران خیلی خوبی دارند.
    #     2- باید از توانایی های خود در ارتباطات استفاده کنند.
        
    #     خانه های غالب و مهم:
    #     2-3-4-8

    #     سیاره های غالب و مهم:
    #     ماه - زحل - زهره - نود شمالی
    #     Moon - Saturn - Venus - North Node

    #     ''',
    #     3: '''
        
    #     The Communicator: You are a natural communicator and have a gift for expressing yourself. You are creative and imaginative, and you have a strong sense of humor.
        
    #     ابر قدرت شما خوش بینی است:
    #     به شدت علاقه به زندگی، ناامید نشدن، خوش شانس، این ها افراد بشدت خوش شانسی و خر شانسی هستند.
    #     یه ارث خوبی بهشون میرسه.

    #     کلید موفقیت:
    #     1- نیاز دارن به تلاش برای ارتقا و توسعه خودشون.
    #     2- باید مطالعه زیاد بکنند.
        
    #     خانه های غالب و مهم:
    #     2 - 8 - 10 - 12

    #     سیاره های غالب و مهم:
    #     خورشید - ماه - مشتری - اورانوس
    #     Sun - Moon - Jupiter - Uranus
        

    #     ''',
    #     4: '''
        
    #     The Organizer: You are a natural organizer and have a strong sense of order. You are practical and reliable, and you have a strong work ethic.
        
    #     ابر قدرت شما کار است:
    #     به شدت سخت کوش، اصلا روی حرف کسی حساب نمیکنند، میل به ثبات دارند.
    #     ترید برای این افراد اصلا خوب نیست

    #     کلید موفقیت:
    #     1- باید با کار و تلاش به هدف های خود برسند.
        
    #     خانه های غالب و مهم:
    #     1 - 4 - 6 - 12

    #     سیاره های غالب و مهم:
    #     مشتری - پلوتو - اورانوس
    #     Jupiter - Pluto - Uranus
        
        
    #     ''',
    #     5: '''
        
    #     The Adventurer: You are a natural adventurer and have a strong sense of freedom. You are versatile and adaptable, and you have a strong sense of curiosity.
        
    #     ابر قدرت شما کنج کاوی است:
    #     اسفنج اطلاعات، به شدت آزاد، شیفته اطلاعات و تحقیق و علم جدید،
    #     دوست دارن مستقل باشند.

    #     کلید موفقیت:
    #     1- مهارت های ارتباطی خودشون رو تقویت کنند تا بتونند ارتباط خوبی با دیگران داشته باشند،
    #     بتونن منظورشون رو به خوبی برسونند.
        
    #     خانه های غالب و مهم:
    #     8 - 9 - 10 - 12

    #     سیاره های غالب و مهم:
    #     خورشید - نپتون - لیلیت - عطارد
    #     Sun - Neptune - Lilith - Mercury
        
    #     ''',
    #     6: '''
        
    #     The Nurturer: You are a natural nurturer and have a strong sense of responsibility. You are caring and compassionate, and you have a strong sense of family.
        
    #     ابر قدرت شما عشق است:
    #     به شدت زیبا، فریبنده، جذاب،
    #     شش عدد شیطان هست به همین خاطر این افراد ظاهر شیطانی دارند.

    #     کلید موفقیت:
    #     1- هرچه قدر این عشق رو خرج کمک به دیگران بکنند موفقتر میشند.
    #     در زمینه های پزشکی و ...
        
    #     خانه های غالب و مهم:
    #     2 - 4 - 7 - 12

    #     سیاره های غالب و مهم:
    #     خورشید - ماه - زحل - زهره
    #     Sun - Moon - Saturn - Venus
        
    #     ''',
    #     7: '''
        
    #     The Seeker: You are a natural seeker and have a strong sense of spirituality. You are introspective and intuitive, and you have a strong sense of purpose.
        
    #     ابر قدرت شما حرکت است:
    #     دائما فعال، فداکار، اهل مطالعه، اهل تحقیق، اهل ورزش، اهل سفر

    #     کلید موفقیت:
    #     1- بینش و دانش بالا در زمینه های مختلف چه شغلی و چه زندگی شخصی
        
    #     خانه های غالب و مهم:
    #     4 - 6 - 9 - 11

    #     سیاره های غالب و مهم:
    #     خورشید - مشتری - عطارد - مریخ
    #     Sun - Jupiter - Mercury - Mars
        
    #     ''',
    #     8: '''
        
    #     The Achiever: You are a natural achiever and have a strong sense of ambition. You are determined and focused, and you have a strong sense of success.
        
    #     ابر قدرت شما مقیاس است:
    #     مغز دائما درحال سیستم سازی است، آهن ربا مالی هستند.
    #     همش محاسبه میکنند، 
    #     سگ شانس هستند در ترید

    #     کلید موفقیت:
    #     1- اقتصاد بخونند
        
    #     خانه های غالب و مهم:
    #     2 - 4 - 6 - 8

    #     سیاره های غالب و مهم:
    #     مشتری - مریخ - کایرون
    #     Jupiter - Mars - Chiron
        
    #     ''',
    #     9: '''
        
    #     The Humanitarian: You are a natural humanitarian and have a strong sense of compassion. You are selfless and generous, and you have a strong sense of empathy.
        
    #     ابر قدرت شما خِرَد است:
    #     باهوش و با استعداد

    #     کلید موفقیت:
    #     1- به دیگران کمک کنند و مشاوره بدن
        
    #     خانه های غالب و مهم:
    #     9 - 10 - 11 - 12

    #     سیاره های غالب و مهم:
    #     خورشید - عطارد - مشتری - مریخ
    #     Sun - Mercury - Jupiter - Mars
        
    #     ''',
    # }