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

# 回傳所有用戶資料
@app.route("/api/<string:company_id>/user", methods=["GET"])
def get_users(company_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer")
    user_datas = cursor.fetchall()
    conn.close()
    
    data = []
    if user_datas:
        for user_data in user_datas:
            data.append(
                {
                    "customer_id": user_data[0],
                    "customer_name": user_data[1],
                }
            )
        return jsonify(data)
    
    else:
        return "User not found", 404
    
# 獲取商家的所有商品列表
@app.route("/api/<string:company_id>/product", methods=["GET"])
def get_products(company_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product WHERE company_name = %s", (company_id,))
    products = cursor.fetchall()
    conn.close()

    data = []
    if products:
        for product in products:
            data.append(
                {
                    "product_id" : product[0],
                    "company_name" : product[1],
                    "product_name" : product[2]
                }
            )
        return jsonify(data)

    else:
        return "Products not found", 404

# 獲取商家的一筆商品
@app.route("/api/<string:company_id>/product/<int:product_id>", methods=["GET"])
def get_product(company_id, product_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product WHERE company_name = %s AND product_id = %s", (company_id, product_id,))
    product = cursor.fetchone()
    conn.close()
    if product:
        product_dict = {
            "product_id": product[0],
            "company_name": product[1],
            "product_name": product[2] 
        }
        return jsonify(product_dict)
    
    else:
        return "Product not found", 404
    
# 提交訂單
@app.route("/api/<string:company_id>/order", methods=["POST"])
def create_order(company_id):
    data = request.json

    order_id = data.get('order_id')
    product_id = data.get('product_id')
    product_name = data.get('product_name')
    customer_id = data.get('customer_id')

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `Order` VALUES (%s, %s, %s, %s, %s)", (order_id, product_id, product_name, customer_id, company_id))
        conn.commit()

        return jsonify({'message': 'Order created successfully'}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    
    finally:
        conn.close()

# 查詢一筆訂單
@app.route("/api/<string:company_id>/order/<string:order_id>", methods=["GET"])
def get_order(company_id, order_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `Order` WHERE company_id = %s AND order_id = %s", (company_id, order_id,))
    order = cursor.fetchone()
    conn.close()
    if order:
        order_dict = {
            "order_id": order[0],
            "product_id": order[1],
            "product_name": order[2],
            "customer_id": order[3]
        }
        return jsonify(order_dict)
    
    else:
        return "Order not found", 404

if __name__ == "__main__":
    app.run()