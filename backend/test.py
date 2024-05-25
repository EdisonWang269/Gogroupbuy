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
@app.route("/api/<string:store_id>/product", methods=["POST"])
def create_product(store_id):
    data = request.json
    price = data.get('price')
    unit = data.get('unit')
    product_describe = data.get('product_describe')
    supplier_name = data.get('supplier_name')
    product_name = data.get('product_name')
    product_picture = data.get('product_picture')
    
    
    query = """INSERT INTO `PRODUCT` (store_id, price, product_describe, supplier_name, product_name, product_picture)
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

#獲取一項團購商品的所有訂購者
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

#取得user的歷史訂單
@app.route(/api/<string:store_id>/,methods = ["GET"] )



#結單時管理者下單（更新團購商品：到貨日期/領取截止日/inventory...）
#到貨時更新到貨日期
#到貨時開始計算停止領取日期


        
if __name__ == "__main__":
    app.run()