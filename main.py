from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time

# Get data
# cmc = requests.get('https://coinmarketcap.com/')
# soup = BeautifulSoup(cmc.content, 'html.parser')

cmc = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
soup = BeautifulSoup(cmc.content, 'html.parser')
print(soup.title)
print(soup.prettify())


# This will give us the entire web page
# print(soup.title)

### Fetching Data
## Scouting

# Parsing the website
# print(soup.prettify())

# This matches the key ‘slug’ so at a minimum, I know that I’ll need to save slug.
# {"id":1,"name":"Bitcoin","symbol":"BTC","slug":"bitcoin"

# <script id="__NEXT_DATA__" type="application/json">
# data = soup.find('script', id='__NEXT_DATA__', type='application/json')
#
# coins = {}
#
# # using data.contents[0] to remove script tags
# coin_data = json.loads(data.contents[0])
# listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
#
# for i in listings:
#     coins[str(i['id'])] = i['slug']

# Print 100 List of coins
# print(coins)

# we now have a dictionary of coin IDs and slugs we can use to scrape historical data.
# print(listings)

## Fetching Historical Data

# for i in coins:
#     page = requests.get(f'https://coinmarketcap.com/currencies/{coins[i]}/historical-data/?start=20200101&end=20200630')
#     soup = BeautifulSoup(page.content, 'html.parser')
#     data = soup.find('script', id='__NEXT_DATA__', type='application/json')
#     historical_data = json.loads(data.contents[0])
#
# quotes = historical_data['props']['initialState']['cryptocurrency']['ohlcvHistorical'][i]['quotes']

# print(quotes)

# info = historical_data['props']['initialState']['cryptocurrency']['ohlcvHistorical'][i]
#
# ### Putting everything together with pandas
#
# market_cap = []
# volume = []
# timestamp = []
# name = []
# symbol = []
# slug = []
#
# for j in quotes:
#     market_cap.append(j['quote']['USD']['market_cap'])
#     volume.append(j['quote']['USD']['volume'])
#     timestamp.append(j['quote']['USD']['timestamp'])
#     name.append(info['name'])
#     symbol.append(info['symbol'])
#     slug.append(coins[i])
#
# df = pd.DataFrame(columns = ['marketcap', 'volume', 'timestamp', 'name', 'symbol', 'slug'])
#
# df['marketcap'] = market_cap
# df['volume'] = volume
# df['timestamp'] = timestamp
# df['name'] = name
# df['symbol'] = symbol
# df['slug'] = slug
#
# # we want to save this to a csv file
# df.to_csv('criptoes.csv', index = False)
#
# print('Saved on ')
