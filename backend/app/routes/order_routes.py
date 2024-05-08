from flask import Blueprint, request, jsonify
from ..database import execute_query

order_bp = Blueprint('order', __name__)

@order_bp.route("/api/<string:merchant_lineid>/order", methods=["POST"])
def create_order(merchant_lineid):
    data = request.json
    order_number = data.get('order_number')
    customer_lineid = data.get('customer_lineid')
    group_buy_num = data.get('group_buy_num')
    quantity = data.get('quantity')
    receive_status = data.get('receive_status')

    query = "INSERT INTO `Order` VALUES (%s, %s, %s, %s, %s)"
    result = execute_query(query, (order_number, customer_lineid, group_buy_num, quantity, receive_status))

    if result:
        return jsonify({'message': 'Order created successfully'}), 200
    else:
        return jsonify({'error': 'Failed to create order'}), 500

@order_bp.route("/api/<string:merchant_lineid>/order/<int:order_number>", methods=["GET"])
def get_order(merchant_lineid, order_number):
    query = "SELECT * FROM `Order` WHERE order_number = %s"
    order = execute_query(query, (order_number,))

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

@order_bp.route("/api/<string:merchant_lineid>/order/<string:customer_lineid>", methods=["GET"])
def get_all_orders(merchant_lineid, customer_lineid):
    query = "SELECT * FROM `Order` WHERE customer_lineid = %s"
    orders = execute_query(query, (customer_lineid,), True)
    
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

@order_bp.route("/api/<string:merchant_lineid>/order/<string:customer_lineid>/<int:status>", methods=["GET"])
def get_orders(merchant_lineid, customer_lineid, status):
    status = True if status == 1 else False

    query = "SELECT * FROM `Order` WHERE customer_lineid = %s AND receive_status = %s"
    orders = execute_query(query, (customer_lineid, status), True)

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