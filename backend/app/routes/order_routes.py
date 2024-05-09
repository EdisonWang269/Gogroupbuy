from flask import Blueprint, request, jsonify
from ..database import execute_query

order_bp = Blueprint('order', __name__)

# 提交一筆訂單
@order_bp.route("/api/<string:en_store_name>/order", methods=["POST"])
def create_order(en_store_name):
    data = request.json
    order_id = data.get('order_id')
    userid = data.get('userid')
    group_buying_id = data.get('group_buying_id')
    quantity = data.get('quantity')

    query = "INSERT INTO `Order` (order_id, userid, group_buying_id, quantity) VALUES (%s, %s, %s, %s)"
    result = execute_query(query, (order_id, userid, group_buying_id, quantity))

    if result:
        return jsonify({'message': 'Order created successfully'}), 200

    return jsonify({'error': 'Failed to create order'}), 500

# 查詢一筆訂單
@order_bp.route("/api/<string:en_store_name>/order/<int:order_id>", methods=["GET"])
def get_order_by_order_id(en_store_name, order_id):
    query = "SELECT * FROM `Order` WHERE order_id = %s"
    order = execute_query(query, (order_id,))

    if order:
        order_dict = {
            "order_id": order[0],
            "userid": order[1],
            "group_buying_id": order[2],
            "quantity": order[3],
            "receive_status" : order[4]
        }
        return jsonify(order_dict), 200
    
    return jsonify({'message':'Fail to get all orders by orderid'}), 404

# 查詢一名客戶所有清單
@order_bp.route("/api/<string:en_store_name>/order/<string:userid>", methods=["GET"])
def get_all_orders_by_userid(en_store_name, userid):
    query = """
                SELECT `Order`.*
                FROM `Order`
                INNER JOIN Group_buying_product ON `Order`.group_buying_id = Group_buying_product.group_buying_id
                WHERE `Order`.userid = %s
                AND Group_buying_product.en_store_name = %s;
            """
    orders = execute_query(query, (userid, en_store_name), True)
    
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

@order_bp.route("/api/<string:en_store_name>/order/<string:userid>/<int:status>", methods=["GET"])
def get_all_orders_by_userid_and_status(en_store_name, userid, status):
    status = True if status == 1 else False

    # query = "SELECT * FROM `Order` WHERE userid = %s AND receive_status = %s"
    query = """
                SELECT `Order`.*
                FROM `Order`
                INNER JOIN Group_buying_product ON `Order`.group_buying_id = Group_buying_product.group_buying_id
                WHERE `Order`.userid = %s
                AND Group_buying_product.en_store_name = %s
                AND receive_status = %s;
            """
    orders = execute_query(query, (userid, en_store_name, status), True)

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