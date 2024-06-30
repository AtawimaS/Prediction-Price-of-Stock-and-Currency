import requests
from datetime import datetime
import pandas as pd

class TwitterScraper:
    def __init__(self, find, num):
        self.find = find
        self.num = num
        self.api_key = 'a08167cfc0974292ee8630738b9f4364'
        self.base_url = 'https://api.scraperapi.com/structured/twitter/search'

    def scrape(self, dataframe=False):
        payload = {
            'api_key': self.api_key,
            'query': self.find,
            'render': 'true',
            'num': self.num
        }
        try:
            response = requests.get(self.base_url, params=payload)
            response.raise_for_status()
            data = response.json()
            datetime_list = []
            message_list = []
            position_list = []
            title_list = []
            highlight_list = []
            link_list = []
            display_link_list = []

            results = data['organic_results']
            for result in results:
                teks = result['snippet']
                position_list.append(result['position'])
                title_list.append(result['title'])
                highlight_list.append(result['highlighs'])
                link_list.append(result['link'])
                display_link_list.append(result['displayed_link'])

                if '(UTC)' in teks:
                    datetime_part, message = teks.split('(UTC)', 1)
                    datetime_part = datetime_part.strip() + " (UTC)"
                else:
                    datetime_part = ""
                    message = teks
                
                try:
                    if datetime_part:
                        datetime_obj = datetime.strptime(datetime_part, '%B %d, %Y @ %I:%M %p (UTC)')
                        datetime_list.append(datetime_obj)
                    else:
                        datetime_list.append(None)
                    message_list.append(message.strip())
                except ValueError as V:
                    print("Error: ", V)
                    datetime_list.append(None)
                    message_list.append(message.strip())
                    continue

            hasil = {
                'Position': position_list,
                'Title': title_list,
                'Time': datetime_list,
                'Message': message_list,
                'Highlight': highlight_list,
                'link': link_list,
                'display_link': display_link_list
            }

            if dataframe:
                return pd.DataFrame(hasil)
            else:
                return hasil
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            print(f"Other error occurred: {err}")

# Testing
# find = "btc-usd"
# scraper = TwitterScraper(find, num=1)
# ini = scraper.scrape(dataframe=True)
# print(ini)
