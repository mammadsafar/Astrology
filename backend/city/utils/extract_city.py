import pandas as pd
from django.core.management.base import BaseCommand

from pathlib import Path

from ..models import City, Province, Country

BASE_DIR = Path(__file__).resolve().parent.parent


def load_cities():
    help = 'Load data from cities.xlsx and province.xlsx into the database'
    # Load the Excel files
    cities_df = pd.read_excel(f'{BASE_DIR}/utils/city.xlsx')
    provinces_df = pd.read_excel(f'{BASE_DIR}/utils/province.xlsx')

    # Create a default country (assuming you have a Country model)
    country, _ = Country.objects.get_or_create(name='ایران')

    # Process and save provinces
    
    for _, row in provinces_df.iterrows():
        # print(_, row)

        province, created = Province.objects.get_or_create(
            name=row['State'],
            defaults={
                'english_name': row['State'],  # Assuming no English names are given
                'country': country,
                'latitude': row['lat'],
                'longitude': row['lng']
            }
        )

    # # Process and save cities
    for _, row in cities_df.iterrows():
        
        # print(_, row)
        province = Province.objects.get(name=row['State'])
        city = City(
            name=row['City'],
            province=province,
            latitude=row['lat'],
            longitude=row['lng']
        )
        city.save()
    return True