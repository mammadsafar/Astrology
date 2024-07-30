import pandas as pd

def persian_to_finglish(text):
    persian_to_latin = {
        'ا': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 's', 'ج': 'j', 'چ': 'ch', 'ح': 'h',
        'خ': 'kh', 'د': 'd', 'ذ': 'z', 'ر': 'r', 'ز': 'z', 'ژ': 'zh', 'س': 's', 'ش': 'sh',
        'ص': 's', 'ض': 'z', 'ط': 't', 'ظ': 'z', 'ع': 'a', 'غ': 'gh', 'ف': 'f', 'ق': 'gh',
        'ک': 'k', 'ك': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n', 'و': 'v', 'ه': 'h', 
        'ی': 'y', 'ي': 'y', ' ': ' ', 'آ': 'a', 'ء': 'a', 'ئ': 'y', 'ؤ': 'v'
    }
    
    arabic_diacritics = {
        'َ': 'a', 'ُ': 'o', 'ِ': 'e', 'ً': 'an', 'ٌ': 'on', 'ٍ': 'en', 
        'ْ': '', 'ّ': '', 'ٰ': 'a', 'ٖ': 'e', 'ٗ': 'o'
    }

    # حذف اعراب و تبدیل حروف فارسی به لاتین
    normalized_text = ''.join(arabic_diacritics.get(char, char) for char in text)
    finglish = ''.join(persian_to_latin.get(char, char) for char in normalized_text)
    return finglish



df = pd.read_excel('FirstNames.xls', engine='xlrd')

names_to_translate = df['Naam'][:6175].tolist()
translated_names = [persian_to_finglish(name) for name in names_to_translate]

df['Translated_Naam'] = None  
df.loc[:6175, 'Translated_Naam'] = translated_names  

df.to_excel('translated_names.xlsx', index=False)

