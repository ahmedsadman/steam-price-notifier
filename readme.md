# Steam Price Notifier (WIP)

Notifies you when steam price drops for monitored games. Notification is sent both as Windows Toast and also via Email. Currently it supports *Windows (7/10/11) only*. The script is dependent on Windows Task Scheduler for regualr polling.

*Please note, this is intended for personal use only and is created that way. It cannot serve more than one user because that is not the purpose here.*

**How price drop is considered?**

The price of games in Steam is not same in all countries. This application is made in a way to show you the lowest possible price internationally. So for example, one game might be 40$ in USD, but the same game can be 20$ in Turkish Lira. This script will notify you for the lowest price converted to USD, regardless if it's actually USD or Turkish Lira (or anything else).

## Usage

1. Download the zip file from the *Release* section
2. Extract the zip and create a `.env` file in that directory with the following values:
    ```
    SENDGRID_API_KEY=<SENDGRID_API_KEY>
    FROM_EMAIL=<FROM_EMAIL>
    TO_EMAIL=<TO_EMAIL>
    APP_IDS=<APP_ID_1>,<APP_ID_2>
    ```
    Sendgrid is used to send email notifications. You need to create a verified Sendgrid domain to send emails. The verfiied sender will be `FROM_EMAIL`. On the other hand, `TO_EMAIL` is the intended receiver of the email. Collect the Steam game ids that you want to monitor. The easiest way is to go to [SteamDB](https://steamdb.info) and search for your game. If the URL looks like `https://steamdb.info/app/1506830` then the game id is `1506830`. So the env variable would look something like this: `APP_IDS=1506830,1606832` for two different games.
3. Create a scheduled job with Windows Task Scheduler and add `SteamPriceNotifier.exe` to be ran. How you want to schedule is totally upto you. If you ask me, I use it with the Trigger `During windows log in` and `repeat every 1 hour indefinitely`.


## Development
1. Install requirements using `pip install -r requirements.txt`, inside a virtual env if preferred.
2. Create the `.env` file and put the required variables as described in Usage section
3. Modify and test as required

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