from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
import json
import sqlite3
import message


load_dotenv()

app = Flask(__name__)

url = 'https://api.telegram.org/bot6203348316:AAGturPMm2UdFPkv91AWiL1_FK3HzwOSy_Q/'


def write_json(data, filename='messages.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# def send_message(chat_id, text='How are you doing?!'):
#     url_send = url + 'sendMessage'
#     answer = {'chat_id': chat_id, 'text': text}
#     r = requests.post(url_send, json=answer)
#     return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        # write_json(r)
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        message.send_message(chat_id=chat_id, text=message)
        if 'hello' in message:
            message.send_message(chat_id, text='Hello, sir! Can i help you?')
        # Connect to the database
        conn = sqlite3.connect('store.db')
        # Create a cursor to execute SQL queries
        cur = conn.cursor()
        # Create the table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY,
            chat_id INTEGER,
            message TEXT
            )
        """)
        # Retrieve all the records from the database
        cur.execute("""
            SELECT * FROM messages
        """)
        records = cur.fetchall()
        # Check if the message is already in the database

        if (chat_id, message) not in records:
            cur.execute("""
            INSERT INTO messages (chat_id, message)
            VALUES (?, ?)
            """, (chat_id, message))

        # Commit the changes to the database
        conn.commit()
        # Close the connection
        conn.close()


        return jsonify(r)

    return '<h1>Hello Dear!</h1>'

# https://api.telegram.org/bot6203348316:AAGturPMm2UdFPkv91AWiL1_FK3HzwOSy_Q/setWebhook?url=https://ea7a-178-74-213-63.eu.ngrok.io/



if __name__ == '__main__':
    app.run()