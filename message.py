import requests

url = 'https://api.telegram.org/bot6203348316:AAGturPMm2UdFPkv91AWiL1_FK3HzwOSy_Q/'


def send_message(chat_id, text='How are you doing?!'):
    url_send = url + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url_send, json=answer)
    return r.json()