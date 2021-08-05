import requests
from pprint import pprint


ls = list()
dup = list()

cmc_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY':'7ea684c7-dc5e-4be7-ad9e-23668fff40e4',
}

r = requests.get(cmc_url, headers=headers)

json = r.json()
data_cap = json['data']

#This will sort through all the ranks of crpyto currencies and display the first 10
all_crypto = json['data']

def get_rank(all_crypto):
    return all_crypto.get('rank')

all_crypto.sort(key=get_rank)
all_crypto = all_crypto[:10]

for x in all_crypto:
    dup.append(x['name'].lower())

#error_coins = ['binance-coin','usd-coin','binance-usd','xrp']

def coin_replace(coin):
  if coin == 'usd-coin':
    pass
  elif coin == 'binance-coin':
    pass
  elif coin == 'binanace-coin':
    pass
  elif coin == 'xrp':
    pass
  else:
    #could def make this better where it gets the info from the server once instead of each time for a different coin
    url = (
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=dogecoin"
    )
    url = url.replace('dogecoin', coin)
    send_server = requests.get(url)
    r2_json = send_server.json()
    r3_json = r2_json[0]
    price = r3_json['current_price']
    for x in all_crypto:
      if coin == x['name'].lower():
        ls.append((x['name'],price,'rank',x['rank']))

dup.pop(3)
dup.insert(3,'binance-coin')
dup.pop(6)
dup.insert(6,'usd-coin')
dup.pop(9)
dup.insert(9,'binance-usd')

print(dup)

for x in dup:
  coin_replace(x)

ls.insert(3,'Binance Coin Info not availble')
ls.insert(4,'XRP Info not availble')
ls.insert(5,'USD Coin Info not availble')
ls.insert(9,'Binance USD Info not availble')

pprint(ls)
prices = dict

#get rid of the rank part if we succesfully complete the whole mission if the program or use it as a fun fact sheet at the end of the program?

#--------------------------------

#How to implement the trade function?

trade_coin = input(f'Which crypto out of these {dup} would you like to trade today?')
if trade_coin == 'usd-coin'or 'binance-coin'or'binanace-coin'or'xrp':
  print('Sorry, but the current coin is unavaible to trade right now...\nPlease select another coin')
else:
  pass
daily_dollars = input('Starting $? ')


try:
  floating_point = float(daily_dollars)
except:
  print('Please only enter numerical value and no dollar sign')
  quit()

print(daily_dollars)

#find coin name and price and put into seperate dictioanry
for x in ls:
  for a in x:
    print(a[0])

# say we start with 1 hundred dollars

# we could do a function where if a certain crypto currency price falls a certain % or drops to a specifed value then the program will execeute a buy command

#make into a GUI? Also add scrolling text like the news

