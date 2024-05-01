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

# 回傳一筆用戶資料
@app.route("/api/<string:company_id>/user/<string:customer_id>", methods=["GET"])
def get_user(company_id, customer_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer WHERE customer_lineid = %s", (customer_id,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        user_dict = {
            "customer_id": user_data[0],
            "customer_name": user_data[1],
        }
        return jsonify(user_dict)
    
    else:
        return "User not found", 404



if __name__ == "__main__":
    app.run()