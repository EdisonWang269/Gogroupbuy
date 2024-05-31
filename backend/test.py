from flask import Flask, request, jsonify

import mysql.connector
import base64
import datetime
import numpy as np


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
    result = execute_query(query, ('2',))
    
    return 'server ok'

#測試加入照片 要把product_picture的資料型態改成longblob
@app.route("/api/product", methods=["POST"])
def add_pic_test():
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo uploaded'}), 400
    
    product_picture_file = request.files['photo'] #取得圖片檔案
    product_picture_binary = base64.b64encode(product_picture_file.read()) #把圖片轉成二進位
    
    query = "INSERT INTO `PRODUCT`(store_id, product_picture) VALUES('store001', %s)"
    result = execute_query(query,(product_picture_binary,))
    if result:
        return jsonify({'message': 'Pruduct created successfully'}), 200
    return jsonify({'error': 'Failed to create product'}), 500
    
#新增一項商品
@app.route("/api/<string:store_id>/product", methods=["POST"])
def create_product(store_id):
    data = request.json     
    price = data.get('price')
    unit = data.get('unit')
    product_describe = data.get('product_describe')
    supplier_name = data.get('supplier_name')
    product_name = data.get('product_name')
    product_picture = data.get('product_picture')

    query = """INSERT INTO `PRODUCT` (store_id, price, unit, product_describe, supplier_name, product_name, product_picture)
                VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    result = execute_query(query,(store_id, price, unit, product_describe, supplier_name, product_name, product_picture))
    
    if result:
        return jsonify({'message': 'Pruduct created successfully'}), 200
    return jsonify({'error': 'Failed to create product'}), 500
    
    
#新增一項團購商品
@app.route("/api/<string:store_id>/product/ontheshelves", methods = ["POST"])
def create_group_buying_product(store_id):
    data = request.json
    launch_date = data.get('launch_date')
    statement_date = data.get('statement_date')
    product_id = data.get('product_id')
    
    query = 'SELECT store_id FROM Product WHERE product_id = %s'
    sid = execute_query(query, (product_id,))
    if sid[0] == store_id:
        query = 'INSERT INTO `Group_buying_product`(launch_date, statement_date, product_id) VALUES(%s, %s, %s);'
        result = execute_query(query, (launch_date, statement_date, product_id,))
        if result:
            return jsonify({'message': 'group_buying_product created successfully'}), 200
        return jsonify({'error': 'Failed to create group_buying_product'}), 500
    
    return jsonify({'error': 'this product not in this store'}), 500

 #結單時管理者進貨，更新團購商品：inventory/purchase_quantity/cost
@app.route("/api/<string:store_id>/product/<int:group_buying_id>/check", methods = ['POST'])
def update_purchase_quantity(store_id, group_buying_id):
    data = request.json
    purchase_quantity = data.get('purchase_quantity')
    cost = data.get('cost')
      
    query = '''UPDATE `Group_buying_product`
                SET purchase_quantity = %s, cost = %s, inventory = %s
                WHERE group_buying_id = %s'''
    result = execute_query(query,(purchase_quantity,cost,purchase_quantity,group_buying_id, ))
    if result:
        return jsonify({'message': 'group_buying_product purchase_quantity updated successfully'}), 200
    return jsonify({'error': 'Failed to update group_buying_produc purchase_quantityt'}), 500     
    
#到貨時(更新團購商品：到貨日期arrival_date/領取截止日due_days)
@app.route("/api/<string:store_id>/product/<int:group_buying_id>/arrival", methods = ['POST'])
def update_arrival_date(store_id, group_buying_id):
    data = request.json
    arrival_date = data.get('arrival_date')
    due_days = data.get('due_days')
    
    query = '''UPDATE `Group_buying_product`
                SET arrival_date = %s, due_days = %s
                WHERE group_buying_id = %s'''
    result = execute_query(query, (arrival_date, due_days, group_buying_id))
    if result:
         return jsonify({'message': 'arrival_date updated successfully'}), 200
    return jsonify({'error': 'Failed to update arrival_date'}), 500                      

#到貨時通知顧客/搜尋：從商品名稱獲取一項團購商品的所有訂購者的訂單資料
# （回傳user_name/訂貨數量/領取期限/手機號碼/訂單狀態)
@app.route("/api/<string:store_id>/Order/<string:product_name>", methods = ["GET"])
def get_userinfo_by_product_name(store_id, product_name):
    query = '''SELECT c.user_name, o.quantity, g.arrival_date, g.due_days, c.phone, o.receive_status
                FROM `Order` AS o,`Group_buying_product` AS g,`Product` AS p, `Customer` AS c
                WHERE o.group_buying_id = g.group_buying_id
                AND g.product_id = p.product_id
                AND c.userid = o.userid
                AND p.store_id = %s
                AND p.product_name = %s;             
    '''
    users = execute_query(query, (store_id, product_name), True)
    data = []
    if users:
        for user in users:
            data.append(
                {
                  "user_name" : user[0],
                  "quantity" : user[1],
                  "領取期限" : user[2] + datetime.timedelta(days=user[3]),
                  "phone" : user[4],
                  "receive_status" : user[5]
                }
             )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get all userinfo by product_name'}), 404  

#取得user的歷史訂單 回傳productid,productname,到貨時間,可領取天數,訂單狀態,圖片
@app.route("/api/<string:store_id>/Order/<string:userid>/",methods = ["GET"] )
def get_user_all_order_by_userid(store_id, userid):
    query = '''SELECT P.product_id, product_name, arrival_date, due_days, receive_status, product_picture
                FROM `Order` AS O, Group_buying_product AS G, Product AS P
                WHERE O.group_buying_id = G.group_buying_id
                AND G.product_id = P.product_id
                AND P.store_id = %s
                AND O.userid = %s'''
    orders = execute_query(query,(store_id, userid), True)
    data = []
    if orders:
        for order in orders:
            data.append(
                {
                    "product_id": order[0],
                    "product_name": order[1],
                    "領取期限":order[2] + datetime.timedelta(days=order[3]),
                    "receive_status" : order[4],
                    "product_picture" : order[5]
                }
            )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get user all order by userid'}), 404 
    


#更改結單日期

#增加現場購買客人
#下架商品時(更新團購商品：income)
        
if __name__ == "__main__":
    app.run()