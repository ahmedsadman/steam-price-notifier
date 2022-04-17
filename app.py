import os
from dotenv import load_dotenv
from win10toast import ToastNotifier
from steam_app import SteamApp
from storage import Storage
from email_notifier import Email

load_dotenv()

STEAM_IDS = os.environ.get('APP_IDS', '')

class App:
    def __init__(self):
        self.toast = ToastNotifier()
        self.apps = [SteamApp(app_id) for app_id in STEAM_IDS.split(',')]
        self.storage = Storage()

    def notify(self, name, price):
        self.toast.show_toast(
            f'{name} in {price}',
            'This is the lowest price',
            icon_path='steam-icon.ico',
            threaded = False,
        )
        Email.notify_price_drop(name, price)

    def check_price(self):
        for app in self.apps:
            current_price = app.get_price_list()[0]['usd']
            formatted_price = f'{current_price}$'
            prev_data = self.storage.get(app.app_id)

            if prev_data and current_price < float(prev_data['price']):
                self.notify(app.name, formatted_price)

            if not prev_data or float(prev_data['price']) != current_price:
                prev_data = self.storage.upsert(app.app_id, app.name, current_price)
