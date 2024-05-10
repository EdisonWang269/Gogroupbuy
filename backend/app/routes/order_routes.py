from flask import Blueprint, request, jsonify
from ..database import execute_query

order_bp = Blueprint('order', __name__)

# 提交一筆訂單
@order_bp.route("/api/<string:store_id>/order", methods=["POST"])
def create_order(store_id):
    data = request.json
    userid = data.get('userid')
    group_buying_id = data.get('group_buying_id')
    quantity = data.get('quantity')

    query = "INSERT INTO `Order` (userid, group_buying_id, quantity) VALUES (%s, %s, %s)"
    result = execute_query(query, (userid, group_buying_id, quantity))

    if result:
        return jsonify({'message': 'Order created successfully'}), 200

    return jsonify({'error': 'Failed to create order'}), 500

# 查詢一筆訂單
@order_bp.route("/api/<string:store_id>/order/<int:order_id>", methods=["GET"])
def get_order_by_order_id(store_id, order_id):
    query = """
                SELECT `Order`.*
                FROM `Order`
                INNER JOIN Group_buying_product ON `Order`.group_buying_id = Group_buying_product.group_buying_id
                INNER JOIN Product ON Group_buying_product.product_id = Product.product_id
                WHERE `Order`.order_id = %s AND Product.store_id = %s;
            """
    order = execute_query(query, (order_id, store_id))

    if order:
        order_dict = {
            "order_id": order[0],
            "userid": order[1],
            "group_buying_id": order[2],
            "quantity": order[3],
            "receive_status" : order[4]
        }
        return jsonify(order_dict), 200
    
    return jsonify({'message':'Fail to get order by orderid'}), 404

# 查詢一名客戶所有清單
@order_bp.route("/api/<string:store_id>/order/<string:userid>", methods=["GET"])
def get_all_orders_by_userid(store_id, userid):
    query = """
                SELECT `Order`.*
                FROM `Order`
                INNER JOIN Group_buying_product ON `Order`.group_buying_id = Group_buying_product.group_buying_id
                INNER JOIN Product ON Group_buying_product.product_id = Product.product_id
                WHERE `Order`.userid = %s
                AND Product.store_id = %s;
            """
    orders = execute_query(query, (userid, store_id), True)
    
    data = []
    if orders:
        for order in orders:
            data.append(
                {
                    "order_id": order[0],
                    "userid": order[1],
                    "group_buying_id": order[2],
                    "quantity": order[3],
                    "receive_status" : order[4]
                }
            )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get all orders by userid'}), 404

@order_bp.route("/api/<string:store_id>/order/<string:userid>/<int:status>", methods=["GET"])
def get_all_orders_by_userid_and_status(store_id, userid, status):
    if status == 0:
        status = False
    elif status == 1:
        status = True
    else:
        return jsonify({'message' : 'Invalid status'}), 404
    
    query = """
                SELECT `Order`.*
                FROM `Order`
                INNER JOIN Group_buying_product ON `Order`.group_buying_id = Group_buying_product.group_buying_id
                INNER JOIN Product ON Group_buying_product.product_id = Product.product_id
                WHERE `Order`.userid = %s
                AND Product.store_id = %s
                AND receive_status = %s;
            """
    orders = execute_query(query, (userid, store_id, status), True)

    data = []
    if orders:
        for order in orders:
            data.append(
                {
                    "order_id": order[0],
                    "userid": order[1],
                    "group_buying_id": order[2],
                    "quantity": order[3],
                    "receive_status" : order[4]
                }
            )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get all orders by userid and status'}), 404