from flask import Flask, request, jsonify

import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
  'user': 'root',
  'password': 'kate1208',
  'host': '127.0.0.1',
  'database': 'Groupbuy',
}

def get_database_connection():
    return mysql.connector.connect(**DB_CONFIG)

def execute_query(query, params=None, fetchall=False):
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)

        if query.strip().upper().startswith('SELECT'):
            if fetchall:
                return cursor.fetchall()
            else:
                return cursor.fetchone()
            
        else:
            conn.commit()
            return True

    except Exception as e:
        print(str(e))
        conn.rollback()
        return None
    
    finally:
        cursor.close()
        conn.close()
      
@app.route('/')
def home():
    query = '''INSERT INTO Test
            VALUES (%s);'''
    result = execute_query(query, ('1',))
    
    return 'server ok'

#新增一項商品
@app.route("/api/product", methods=["POST"])
def create_product():
    data = request.json
    store_id = data.get('store_id')
    price = data.get('price')
    product_describe = data.get('product_describe')
    supplier_name = data.get('supplier_name')
    product_name = data.get('product_name')
    product_picture = data.get('product_picture')
    
    query = """INSERT INTO `PRODUCT` (store_id, price, product_describe, supplier_name, product_name, product_picture)
                VALUES (%s, %s, %s, %s, %s, %s)"""
    result = execute_query(query,(store_id, price, product_describe, supplier_name, product_name, product_picture))
    
    if result:
        return jsonify({'message': 'Pruduct created successfully'}), 200
    return jsonify({'error': 'Failed to create product'}), 500
    
#新增一項團購商品
@app.route("/api/<string:store_id>/product", methods = ["POST"])
def create_group_buying_product():
    data = request.json
    purchase_quantity = data.get('purchase_quantity')
    launch_date = data.get('launch_date')
    statement_date = data.get('statement_date')
    arrival_date = data.get('arrival_date')
    due_days= data.get('due_days')
    inventory = data.get('inventory')
    arrival_date = data.get('arrival_date')
    income = data.get('income')
    cost = data.get('cost')
    product_id = data.get('product_id')
    
    query = '''INSERT INTO `Group_buying_product`(purchase_quantity, launch_date, statement_date, arrival_date,
                 due_days, inventory, arrival_date, income, cost, product_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s))'''
    result = execute_query(query, (purchase_quantity, launch_date, statement_date, arrival_date,
                 due_days, inventory, arrival_date, income, cost, product_id))   
    
    if result:
         return jsonify({'message': 'group_buying_product created successfully'}), 200
    return jsonify({'error': 'Failed to create group_buying_product'}), 500      

#獲取一項團購商品的所有訂購者


#到貨時更新到貨日期
#到貨時開始計算停止領取日期


        
if __name__ == "__main__":
    app.run()