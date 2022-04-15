import timeit
from steam_app import SteamApp
from pprint import pprint
from win10toast import ToastNotifier

start = timeit.default_timer()
app = SteamApp('1506830')
print(app.name)
pprint(app.get_price_list())
stop = timeit.default_timer()

print(f'Time: {stop - start}')

# toast = ToastNotifier()
# toast.show_toast(
#     "Notification",
#     "Notification body",
#     duration = 5,
#     threaded = False,
# )
# toast.show_toast(
#     "Notification 2",
#     "Notification body 2",
#     duration = 5,
#     threaded = False,
# )

