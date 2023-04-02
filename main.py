from flask import Flask
from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()

# app = Flask(__name__)


url = 'https://api.telegram.org/bot6203348316:AAGturPMm2UdFPkv91AWiL1_FK3HzwOSy_Q/'


def write_json(data, filename='messages.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_updates():
    url_up = url + 'getUpdates'
    r = requests.get(url_up)
    # write_json(r.json())
    return r.json()


def send_message(chat_id, text='How are you doing?!'):
    url_send = url + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url_send, json=answer)
    return r.json()


def main():
    # r = requests.get(url+'getMe')
    # write_json(r.json())
    r = get_updates()
    chat_id = r['result'][-1]['message']['chat']['id']
    send_message(chat_id)




if __name__ == '__main__':
    main()