from steam_app import SteamApp
from pprint import pprint

app = SteamApp('1506830')
print(app.name)
pprint(app.get_price_list())
input('')
