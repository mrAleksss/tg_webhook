"""helper function"""
import requests

URL = 'https://api.telegram.org/bot6203348316:AAGturPMm2UdFPkv91AWiL1_FK3HzwOSy_Q/'


def send_message(chat_id, text='How are you doing?!'):
    """function send messages"""
    url_send = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    response = requests.post(url_send, json=answer, timeout=10)
    return response.json()
