from flask import Flask, abort, render_template, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser
import git
import mysql.connector

app = Flask(__name__)

config_path = '/home/wangpython/Gogroupbuy/backend/config.ini'

config = configparser.ConfigParser()
config.read(config_path)

line_bot_api = LineBotApi(config['line-bot']['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(config['line-bot']['CHANNEL_SECRET'])

host = 'wangpython.mysql.pythonanywhere-services.com'
database = 'wangpython$test'
username = 'wangpython'
password = 'gogroupbuy'

def check_db_connection():
    try:
        conn = mysql.connector.connect(
            host = host,
            database = database,
            username = username,
            password = password
        )
        return True
    except mysql.connector.Error as e:
        return False


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'

@app.route("/db")
def db():


@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):

    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
