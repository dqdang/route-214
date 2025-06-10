# route_214/packs/management/commands/load_pack_data.py

from django.core.management.base import BaseCommand
from packs.models import BoosterPack
from bs4 import BeautifulSoup
import datetime
import json
import requests

class Command(BaseCommand):
    help = 'Loads Pokémon booster pack data into the database'

    def handle(self, *args, **kwargs):
        price_chart_url = "https://www.pricecharting.com/search-products?type=prices&ignore-preferences=true&q=booster+pack"
        release_date_url = "https://api.pokemontcg.io/v2/sets"
        # test = ""
        # with open('test.html', "r") as f:
        #     test = f.read()
        price_chart_soup = BeautifulSoup(requests.get(price_chart_url).text, 'html.parser')
        # price_chart_soup = BeautifulSoup(test, 'html.parser')
        release_date_request = json.loads(requests.get(release_date_url).text)
        sets = release_date_request['data']
        release_date_dictionary = {}
        for s in sets:
            if "HS—" in s['name']:
                s['name'] = s['name'].split("—")[1].strip()
            if "Pokémon" in s['name']:
                s['name'] = s['name'].split("Pokémon")[1].strip()
            release_date_dictionary[s['name'].lower()] = datetime.datetime.strptime(s['releaseDate'], '%Y/%m/%d').date()
        # print(release_date_dictionary)
        price_table = price_chart_soup.find('table', id='games_table')
        set_name = ""
        release_date = ""
        price = ""
        link = ""
        pack_data = []
        if price_table:
            # Assuming the structure has specific rows/cells for prices
            # This is a generic approach; actual selectors might be more specific.
            # Example: Find all rows and iterate to find the price types.
            rows = price_table.find_all('tr')
            counter = 0
            for row in rows:
                set_name = row.find('td', class_='phone-landscape-hidden')
                if set_name:
                    set_name = set_name.find('a')
                    set_name = set_name.get_text(strip=True).replace('$', '').replace(',', '')
                title = row.find('td', class_='title')
                if title:
                    title = title.find('a')
                    link = title.get('href')
                    title = title.get_text(strip=True).replace('$', '').replace(',', '')
                price = row.find('td', class_='used_price')
                if price:
                    price = price.get_text(strip=True).replace('$', '').replace(',', '')
                if "Booster Pack" != title or "Chinese" in set_name or "Japanese" in set_name or "Pokemon" not in set_name \
                    or "McDonalds" in set_name or "Trick or Trade" in set_name:
                    continue
                set_name = set_name.split("Pokemon")[1].strip()
                try:
                    release_date = release_date_dictionary[set_name.lower()]
                except:
                    if set_name == "Base Set":
                        release_date = datetime.datetime.strptime("1999/01/09", '%Y/%m/%d').date()
                    elif set_name == "Scarlet & Violet 151":
                        release_date = release_date_dictionary["151"]
                    elif set_name == "Fire Red & Leaf Green":
                        release_date = release_date_dictionary["firered & leafgreen"]
                    elif set_name == "Expedition":
                        release_date = release_date_dictionary["expedition base set"]
                    elif set_name == "Team Magma & Team Aqua":
                        release_date = release_date_dictionary["team magma vs team aqua"]
                    else:
                        print(set_name)
                pack_data.append({"set_name": set_name, "release_date": release_date, "price_range": float(price), "price_charting_link": link})
                counter += 1
        self.stdout.write(self.style.SUCCESS('Deleting existing data...'))
        BoosterPack.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Existing data deleted.'))

        for data in pack_data:
            BoosterPack.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Successfully added: {data["set_name"]}'))

        self.stdout.write(self.style.SUCCESS('Data loading complete!'))
