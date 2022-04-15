from win10toast import ToastNotifier
from steam_app import SteamApp

STEAM_IDS = ['1506830', '359550']

class App:
    def __init__(self):
        self.toast = ToastNotifier()
        self.apps = [SteamApp(app_id) for app_id in STEAM_IDS]

    def notify(self, name, price):
        self.toast.show_toast(
            f'"{name}" Price Drop',
            f'As low as {price} today',
            threaded = False,
        )

    def check_price(self):
        for app in self.apps:
            lowest_price = f'{app.get_price_list()[0]["usd"]}$'
            self.notify(app.name, lowest_price)
