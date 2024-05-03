from flask import Flask, request, jsonify

import mysql.connector

app = Flask(__name__)

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'Groupbuy',
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
        return jsonify(data), 200
    
    else:
        return "User not found", 404
    
# 獲取商家的所有商品列表
@app.route("/api/<string:merchant_lineid>/product", methods=["GET"])
def get_products(merchant_lineid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = """
                SELECT 
                    gb.group_buying_number,
                    gb.merchant_lineid,
                    gb.purchase_quantity,
                    gb.launch_date,
                    gb.statement_date,
                    gb.arrival_date,
                    gb.due_days,
                    gb.inventory,
                    gb.income,
                    gb.cost,
                    p.product_id,
                    p.price,
                    p.product_describe,
                    p.supplier_name,
                    p.product_name,
                    p.product_picture
                FROM 
                    Group_buying_product AS gb
                INNER JOIN 
                    Product AS p ON gb.product_id = p.product_id
                WHERE 
                    gb.merchant_lineid = %s;
            """

    cursor.execute(query, (merchant_lineid,))
    products = cursor.fetchall()
    conn.close()

    data = []
    if products:
        for product in products:
            data.append(
                {
                    "group_buying_number" : product[0],
                    "merchant_lineid" : product[1],
                    "purchase_quantity" : product[2],
                    "launch_date" : product[3],
                    "statement_date" : product[4],
                    "arrival_date" : product[5],
                    "due_days" : product[6],
                    "inventory" : product[7],
                    "income" : product[8],
                    "cost" : product[9],
                    "product_id" : product[10],
                    "price" : product[11],
                    "product_describe" : product[12],
                    "supplier_name" : product[13],
                    "product_name" : product[14],
                    "product_picture" : product[15]
                }
            )
        return jsonify(data), 200

    return jsonify({"message": "Products not found"}), 404

# 獲取一筆團購訂單
@app.route("/api/<string:merchant_lineid>/product/<int:group_buying_number>", methods=["GET"])
def get_product(merchant_lineid, group_buying_number):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = """
                SELECT 
                    gb.group_buying_number,
                    gb.merchant_lineid,
                    gb.purchase_quantity,
                    gb.launch_date,
                    gb.statement_date,
                    gb.arrival_date,
                    gb.due_days,
                    gb.inventory,
                    gb.income,
                    gb.cost,
                    p.product_id,
                    p.price,
                    p.product_describe,
                    p.supplier_name,
                    p.product_name,
                    p.product_picture
                FROM 
                    Group_buying_product AS gb
                INNER JOIN 
                    Product AS p ON gb.product_id = p.product_id
                WHERE 
                    gb.merchant_lineid = %s
                AND
                    gb.group_buying_number = %s;
            """
    cursor.execute(query, (merchant_lineid, group_buying_number,))
    product = cursor.fetchone()
    conn.close()
    if product:
        product_dict = {
                            "group_buying_number" : product[0],
                            "merchant_lineid" : product[1],
                            "purchase_quantity" : product[2],
                            "launch_date" : product[3],
                            "statement_date" : product[4],
                            "arrival_date" : product[5],
                            "due_days" : product[6],
                            "inventory" : product[7],
                            "income" : product[8],
                            "cost" : product[9],
                            "product_id" : product[10],
                            "price" : product[11],
                            "product_describe" : product[12],
                            "supplier_name" : product[13],
                            "product_name" : product[14],
                            "product_picture" : product[15]
                        }
        return jsonify(product_dict), 200

    return jsonify({"message": "Product not found"}), 404
    
# 提交一筆訂單
@app.route("/api/<string:merchant_lineid>/order", methods=["POST"])
def create_order(merchant_lineid):
    data = request.json

    order_number = data.get('order_number')
    customer_lineid = data.get('customer_lineid')
    group_buy_num = data.get('group_buy_num')
    quantity = data.get('quantity')
    receive_status = data.get('receive_status')

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        query = "INSERT INTO `Order` VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (order_number, customer_lineid, group_buy_num, quantity, receive_status))
        conn.commit()

        return jsonify({'message': 'Order created successfully'}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    
    finally:
        conn.close()

# 查詢一筆訂單
@app.route("/api/<string:merchant_lineid>/order/<int:order_number>", methods=["GET"])
def get_order(merchant_lineid, order_number):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "SELECT * FROM `Order` WHERE order_number = %s"
    cursor.execute(query, (order_number,))
    order = cursor.fetchone()
    conn.close()

    if order:
        order_dict = {
            "order_number": order[0],
            "customer_lineid": order[1],
            "group_buy_num": order[2],
            "quantity": order[3],
            "receive_status" : order[4]
        }
        return jsonify(order_dict), 200
    
    return jsonify({'message':'Order not found'}), 404

# 查詢一名客戶所有清單
@app.route("/api/<string:merchant_lineid>/order/<string:customer_lineid>", methods=["GET"])
def get_all_orders(merchant_lineid, customer_lineid):

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "SELECT * FROM `Order` WHERE customer_lineid = %s"
    cursor.execute(query, (customer_lineid,))
    orders = cursor.fetchall()
    conn.close()

    data = []
    if orders:
        for order in orders:
            data.append(
                {
                    "order_number": order[0],
                    "customer_lineid": order[1],
                    "group_buy_num": order[2],
                    "quantity": order[3],
                    "receive_status" : order[4]
                }
            )
        return jsonify(data), 200

    return jsonify({'message' : 'Order not found'}), 404

# 查詢一名客戶歷史或代領清單
@app.route("/api/<string:merchant_lineid>/order/<string:customer_lineid>/<int:status>", methods=["GET"])
def get_orders(merchant_lineid, customer_lineid, status):
    status = True if status == 1 else False

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "SELECT * FROM `Order` WHERE customer_lineid = %s AND receive_status = %s"
    cursor.execute(query, (customer_lineid, status))
    orders = cursor.fetchall()
    conn.close()

    data = []
    if orders:
        for order in orders:
            data.append(
                {
                    "order_number": order[0],
                    "customer_lineid": order[1],
                    "group_buy_num": order[2],
                    "quantity": order[3],
                    "receive_status" : order[4]
                }
            )
        return jsonify(data), 200

    return jsonify({'message' : 'Order not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)