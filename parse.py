import requests
from webhook import write_json
import re


def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    print(crypto)


def get_stock():
    url = 'https://pro-api.coinmarketcap.com/v1/exchange/listings/latest'
    r = requests.get(url)
    write_json(r.json(), filename='stock.json')



def main():
    parse_text('/bitcoin')




if __name__ == '__main__':
    main()