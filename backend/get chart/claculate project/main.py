# Powered by: https://mammadsafar.ir/
import os
import msvcrt

from utils.extentions import convert_date
from utils.data import Data


def reduce_to_single_digit(number):
    while number > 9:
        number = sum(int(digit) for digit in str(number))
        if number == 11 or number == 22 or number == 33:
            return number
    return number


def find_desteni_name_number(name):
    # عدد تقدیر اسم
    letter_weights = {chr(i): (i - 96) % 9 or 9 for i in range(97, 123)}
    name_number = ''.join(str(letter_weights[char]) for char in name.lower() if char.isalpha())
    return reduce_to_single_digit(int(name_number))

def find_motivation_name_number(name):
    # عدد روح اسم
    # جمع اعداد حروف باصدا اسم  [a,e,i,o,u,y]
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    split_name = list(name.lower())
    # Use list comprehension to filter vowels
    filtered_name = [i for i in split_name if i in vowels]
    filtered_name = ''.join(filtered_name)
    letter_weights = {chr(i): (i - 96) % 9 or 9 for i in range(97, 123)}
    name_number = ''.join(str(letter_weights[char]) for char in filtered_name if char.isalpha())
    
    return reduce_to_single_digit(int(name_number))


def print_power_characteristics(birthNumber):
    # Define the power characteristics for each number
    power_characteristics_caption = Data.power_characteristics_caption

    # Print the power characteristics for the birth number
    characteristic = power_characteristics_caption.get(birthNumber, 'Unknown characteristic')
    print(f"\nThe power characteristics for the birth number {birthNumber} are:\n\n")
    print('-' * 60)
    print(characteristic)
    print('-' * 60 + '\n')

def investment(birthNumber):
    investment_options = Data.investment_options
    investment_caption = {key: key.replace('_', ' ').title() for key in investment_options}
    print(f"\nThe investment characteristics for the birth number {birthNumber} are:\n")
    print("------------------------------------------------------------")
    for key, numbers in investment_options.items():
        if birthNumber in numbers:
            print(investment_caption[key])
    print("------------------------------------------------------------\n")

def name_match(nameNumber, birthNumber):
    name_match_characteristics = Data.name_match_characteristics
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
        # choice = 2
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice.isdigit():
        # if choice:
            choice = int(choice)
            if choice == 1:
                name = input("Please enter your name: ")
                day, month, year = (int(input(f"Please enter the {x}: ")) for x in ["day", "month", "year"])
                os.system('cls' if os.name == 'nt' else 'clear')

                day, month, year = convert_date(day, month, year)
                birthNumber = reduce_to_single_digit(int(f"{day}{month}{year}"))
                nameNumber = find_desteni_name_number(name)
                print(f"Your Power Number is: {birthNumber}")
                print(f"Your Name Number is: {nameNumber}\n")
                print_power_characteristics(birthNumber)
                investment(birthNumber)
                name_match(nameNumber, birthNumber)

                print("\n\n\n Press any key to continue...")
                msvcrt.getch()
                
                os.system('cls' if os.name == 'nt' else 'clear')
            elif choice == 2:
                # name = input("Please enter your name: ")
                name = 'Tr'
                os.system('cls' if os.name == 'nt' else 'clear')

                print(f"Your Name Number is: {find_desteni_name_number(name)}")

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




# from googletrans import Translator

# def translate_names(names_list):
#     translator = Translator()
#     translated_names = []
    
#     for name in names_list:
#         translation = translator.translate(name, src='fa', dest='en')
#         translated_names.append(translation.text)
    
#     return translated_names

# # مثال استفاده
# names = ['اسماعيل', 'اَبيش', 'اَپروَند', 'اَوَخشيا', 'فاطمه', 'علی', 'زهرا', 'فاطمه', 'علی', 'زهرا', 'فاطمه', 'ادريس', 'ابالفضل']
# translated_names = translate_names(names)
# print(translated_names)







