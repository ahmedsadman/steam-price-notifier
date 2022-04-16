from dotenv import load_dotenv
from app import App

load_dotenv()


if __name__ == '__main__':
    app = App()
    app.check_price()
