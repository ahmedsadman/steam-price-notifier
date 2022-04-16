# Steam Price Notifier (WIP)

Notifies you when steam price drops for monitored games. Notification is sent both as Windows Toast and also via Email. Currently it supports *Windows (7/10/11) only*. The script is dependent on Windows Task Scheduler for regualr polling.

*Please note, this is intended for personal use only and is created that way. It cannot serve more than one user because that is not the purpose here.*

**How price drop is considered?**

The price of games in Steam is not same in all countries. This application is made in a way to show you the lowest possible price internationally. So for example, one game might be 40$ in USD, but the same game can be 20$ in Turkish Lira. This script will notify you for the lowest price converted to USD, regardless if it's actually USD or Turkish Lira (or anything else).

## Usage

Currently the application is still under development. Usage will be updated soon. If you're developer, you can look into the *Development* section to start using it right away


## Development
1. Install requirements using `pip install -r requirements.txt`, inside a virtual env if preferred.
2. You will need the following variables in a `.env` file:
    ```
    SENDGRID_API_KEY=<SENDGRID_API_KEY>
    FROM_EMAIL=<FROM_EMAIL>
    TO_EMAIL=<TO_EMAIL>
    ```
    Sendgrid is used to send email notifications. You need to create a verified Sendgrid domain to send emails. Configuring Sendgrid properly is definitely not easy, beware of this. The verfiied sender will be `FROM_EMAIL`. On the other hand, `TO_EMAIL` is the intended receiver of the email
3. Collect the Steam game ids that you want to monitor. The easiest way is to go to [SteamDB](https://steamdb.info) and search for your game. If the URL looks like `https://steamdb.info/app/1506830` then the game id is `1506830`. Place this game id inside `app.py` -> `STEAM_IDS` variable. This process will be made easier soon so that you don't have to edit code to monitor games.
4. Now that it's done. Create a executable binary package and put it inside Windows Task Scheduler. How you want to schedule is totally upto you. If you ask me, I use it with the Trigger `During windows log in` and `repeat every 4 hour indefinitely`.

## Creating binary package
Pyinstaller can be used to create binary distribution with the following command. Pyinstaller should already be installed with the requirements:
```
pyinstaller main.py -n SteamPriceNotifier --noconsole --onefile
```

This will create a `exe` called `SteamPriceNotifier.exe` inside `dist` folder. This is the file that you're going to use with Windows Task Scheduler. Please make sure the following files exist in the binary distribution directory to make it work properly:

```
-- .env
-- steam-icon.ico
-- SteamPriceNotifier.exe
```