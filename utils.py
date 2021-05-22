import requests
from decimal import Decimal
from datetime import date

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def get_html(url):
    req = requests.get(url)
    return req


def find_char_code(string):
    stat_idx = string.find('<CharCode>') + len('<CharCode>')
    end_idx = stat_idx + 3
    char_code = string[stat_idx:end_idx]
    return char_code


def find_value(string):
    stat_idx = string.find('<Value>') + len('<Value>')
    end_idx = stat_idx + (string.find('</Value>') - stat_idx)
    valute = string[stat_idx:end_idx].split(',')
    return Decimal(f'{valute[0]}.{valute[1]}').quantize(Decimal("1.00"))


def find_date(string):
    stat_idx = string.find('Date="') + len('Date="')
    end_idx = stat_idx + (string.find('" name=') - stat_idx)
    dt = string[stat_idx:end_idx].split('.')
    today = date(int(dt[2]), int(dt[1]), int(dt[0]))
    return today


def currency_information():
    html = get_html(URL)
    currency = html.text.split('</Valute>')
    return currency


def currency_rates(char_code):
    info = currency_information()
    today = find_date(info[0])
    dict_currency_rates = {}
    for i in range(len(info) - 1):
        # print(find_char_code(info[i]), find_value(info[i]))
        dict_currency_rates.setdefault(find_char_code(info[i]), find_value(info[i]))
    return f'{dict_currency_rates.get(char_code.upper())} {today}'
