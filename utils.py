USD_CONVERSION_RATES = {
    'us': 1,
    'in': 76.3,
    'tr': 14.61,
    'ar': 112.89,
    'vn': 22901.50,
    'kz': 457.18,
    'id': 14385.70,
}

def convert_to_usd(price, currency):
    return float(format(price/USD_CONVERSION_RATES[currency], '.2f'))