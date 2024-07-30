import pandas as pd
from django.core.management.base import BaseCommand
from ...models import City, Province, Country

class Command(BaseCommand):
    help = 'Load data from cities.xlsx and province.xlsx into the database'

    def handle(self, *args, **kwargs):
        # Load the Excel files
        cities_df = pd.read_excel('./city/management/commandscity.xlsx')
        provinces_df = pd.read_excel('./city/management/commandsprovince.xlsx')

        # Create a default country (assuming you have a Country model)
        country, _ = Country.objects.get_or_create(name='Iran')

        # Process and save provinces
        for _, row in provinces_df.iterrows():
            province, created = Province.objects.get_or_create(
                name=row['State'],
                defaults={
                    'english_name': row['State'],  # Assuming no English names are given
                    'country': country,
                    'latitude': row['φ(d)'],
                    'longitude': row['λ(d)']
                }
            )

        # Process and save cities
        for _, row in cities_df.iterrows():
            province = Province.objects.get(name=row['State'])
            city = City(
                name=row['City'],
                province=province,
                latitude=row['φ(d)'],
                longitude=row['λ(d)']
            )
            city.save()

        self.stdout.write(self.style.SUCCESS('Data successfully loaded into the database'))