import requests
import utils
from concurrent.futures import ThreadPoolExecutor, wait

# Country Codes: https://www.iban.com/country-codes
# API Doc: https://wiki.teamfortress.com/wiki/User:RJackson/StorefrontAPI#Known_methods

BASE_URL = 'https://store.steampowered.com/api'

CURRENCY_CODES = utils.USD_CONVERSION_RATES.keys()

class SteamApp:
  def __init__(self, app_id):
    self.app_id = app_id
    self.response_content = None
    self.name = None
    self._get_content()

  def _get_field(self, content, field):
    return content[self.app_id]['data'][field]

  def _get_content(self):
    url = f'{BASE_URL}/appdetails?appids={self.app_id}'
    res = requests.get(url)
    self.response_content = res.json()
    self.name = self._get_field(self.response_content, 'name')
    
  def get_price(self, currency):
    url = f'{BASE_URL}/appdetails?appids={self.app_id}&cc={currency}&filters=price_overview'
    res = requests.get(url)
    field = self._get_field(res.json(), 'price_overview')
    raw_price = field['final']/100
    return {
      'currency': field['currency'], 
      'formatted': field['final_formatted'], 
      'raw': raw_price, 
      'usd': utils.convert_to_usd(raw_price, currency)
    }

  def get_price_list(self):
    # prices = [self.get_price(curr) for curr in CURRENCY_CODES]
    # return sorted(prices, key=lambda d: d['usd'])

    futures = []
    prices = []

    with ThreadPoolExecutor(max_workers=16) as executor:
      for curr in CURRENCY_CODES:
        futures.append(executor.submit(self.get_price, curr))

      futures, _ = wait(futures)
      for future in futures:
        prices.append(future.result())

    return sorted(prices, key=lambda d: d['usd'])
