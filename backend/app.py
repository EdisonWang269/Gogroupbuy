from flask import Flask, abort, render_template, request, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flaskext.mysql import MySQL

import configparser
import mysql.connector

app = Flask(__name__)

config_path = '/home/wangpython/Gogroupbuy/backend/config.ini'

config = configparser.ConfigParser()
config.read(config_path)

line_bot_api = LineBotApi(config['line-bot']['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(config['line-bot']['CHANNEL_SECRET'])

app.config['MYSQL_DATABASE_HOST'] = config['db']['host']
app.config['MYSQL_DATABASE_USER'] = config['db']['username']
app.config['MYSQL_DATABASE_PASSWORD'] = config['db']['password']
app.config['MYSQL_DATABASE_DB'] = config['db']['database']

mysql = MySQL(app)

@app.route('/')
def home():

    # cursor = mysql.get_db().cursor()
    # cursor.execute('''INSERT INTO `goods` VALUES ('4710367347574', '喔規', '高雄市左營區', '2023-12-17 10:28:31');''')
    # mysql.get_db().commit()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO `goods` VALUES ('4710367347574', '喔規', '高雄市左營區', '2023-12-17 10:28:31');''')
    conn.commit()
    cursor.close()
    conn.close()

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

@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):

    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

# 建立用戶資料
@app.route("/api/<string:company_id>/user", methods=["POST"])
def create_user(company_id):
    data = request.json
    line_id = data.get('customer_lineid')
    name = data.get('customer_name')
    picture = data.get('customer_picture')
    email = data.get('customer_mail')
    phone = data.get('phone')

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customer (customer_lineid, phone) VALUES (%s, %d)", (line_id, phone))
        conn.commit()

        return jsonify({'message': 'New user created successfully'}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    
    finally:
        cursor.close()
        conn.close()


# 回傳一筆用戶資料
@app.route("/api/<string:company_id>/user/<string:customer_id>", methods=["GET"])
def get_user(company_id, customer_id):
    pass

# 回傳所有用戶資料
@app.route("/api/<string:company_id>/user", methods=["GET"])
def get_users(company_id):
    pass

# 獲取商家的所有商品列表
@app.route("/api/<string:company_id>/product", methods=["GET"])
def get_products(company_id):
    pass
    # if company_id not in products_db:
    #     abort(404, "Company not found")

    # return jsonify()

# 獲取商家的一筆商品
@app.route("/api/<string:company_id>/product/<int:product_id>", methods=["GET"])
def get_product(company_id, product_id):
    pass

# 提交訂單
@app.route("/api/<string:company_id>/order", methods=["POST"])
def create_order(company_id):
    pass
    # if company_id not in products_db:
    #     abort(404, "Company not found")
    
    # data = request.json
    # product_id = data.get("product_id")
    # quantity = data.get("quantity")

    # # 確認商品是否存在
    # products = products_db[company_id]
    # product = next((p for p in products if p["id"] == product_id), None)
    # if product is None:
    #     abort(404, "Product not found")
    
    # # 創建訂單
    # order = {
    #     "product_id": product_id,
    #     "quantity": quantity,
    #     "company_id": company_id
    # }
    # orders_db.append(order)
    # return jsonify(order), 201

# 查詢一筆訂單
@app.route("/api/<string:company_id>/order/<int:order_id>", methods=["GET"])
def get_order(company_id, order_id):
    pass

# 查詢所有定單
@app.route("/api/<string:company_id>/order", methods=["GET"])
def get_orders(company_id):
    pass

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
