import pandas as pd
from deep_translator import GoogleTranslator

# خواندن فایل اکسل
df = pd.read_excel('FirstNames.xls', engine='xlrd')

# ایجاد شیء ترجمه
translator = GoogleTranslator(source='fa', target='en')

# تعریف تابع برای ترجمه دسته‌ای از نام‌ها
def translate_batch(translator, names):
    translations = []
    for name in names:
        translation = translator.translate(name)
        translations.append(translation)
    return translations

# ترجمه فقط 10 نام اول
names_to_translate = df['Naam'][:10].tolist()
translated_names = translate_batch(translator, names_to_translate)

# افزودن ترجمه‌ها به دیتافریم
df['Translated_Naam'] = None  # ایجاد ستون برای ترجمه‌ها
df.loc[:10, 'Translated_Naam'] = translated_names  # ترجمه‌ها را اضافه کنید

# ذخیره به فایل اکسل جدید
df.to_excel('translated_names.xlsx', index=False)


