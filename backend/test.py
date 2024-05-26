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
    
    query = 'INSERT INTO `Group_buying_product`(launch_date, statement_date, product_id) VALUES(%s, %s, %s);'
    result = execute_query(query, (launch_date, statement_date, product_id,))   
    
    if result:
         return jsonify({'message': 'group_buying_product created successfully'}), 200
    return jsonify({'error': 'Failed to create group_buying_product'}), 500      


#到貨時通知顧客：獲取一項團購商品的所有訂購者
@app.route("/api/<string:store_id>/Order/<int:group_buying_id>", methods = ["GET"])
def get_userid_by_group_buying_id(store_id, group_buying_id):
    query = '''SELECT `userid`
                FROM `Order` AS O,`Group_buying_product` AS G,`Product` AS P
                WHERE O.group_buying_id = G.group_buying_id
                AND G.product_id = P.product_id
                AND P.store_id = %s
                AND O.group_buying_id = %s;             
    '''
    userids = execute_query(query, (store_id, group_buying_id), True)
    data = []
    if userids:
        data.append(
            {
                "userids":userids,
            }
        )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get all userid by group_buying_id'}), 404  

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
    
#結單時管理者進貨（更新團購商品：到貨日期/領取截止日/inventory...） 
#前端畫面有缺：商品上架缺supplier_name，缺管理者進貨的頁面
#更改結單日期
#到貨時更新到貨日期
#到貨時開始計算停止領取日期
#增加現場購買客人

        
if __name__ == "__main__":
    app.run()