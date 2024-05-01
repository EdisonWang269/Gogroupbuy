from flask import Flask, abort, render_template, request, jsonify

import mysql.connector

app = Flask(__name__)

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'gogroupbuy',
}


@app.route('/')
def home():
    return 'server ok'

# 建立用戶資料
@app.route("/api/<string:company_id>/user", methods=["POST"])
def create_user(company_id):
    data = request.json
    line_id = data.get('customer_lineid')
    name = data.get('customer_name')
    picture = data.get('customer_picture')
    email = data.get('customer_mail')
    phone = int(data.get('phone'))

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customer (customer_lineid, phone) VALUES (%s, %s)", (line_id, phone))
        conn.commit()

        return jsonify({'message': 'New user created successfully'}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    
    finally:
        conn.close()

if __name__ == "__main__":
    app.run()