from flask import Blueprint, request, jsonify
from ..database import execute_query
from ..sendmess import send_message

from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required

order_bp = Blueprint('order', __name__)

# 提交一筆訂單
@order_bp.route("/api/order", methods=["POST"])
@jwt_required()
def create_order():
    data = request.json
    group_buying_id = data.get('group_buying_id')
    quantity = data.get('quantity')

    identity = get_jwt_identity()
    userid = identity.get('userid')

    query = "INSERT INTO `Order` (userid, group_buying_id, quantity) VALUES (%s, %s, %s)"
    result = execute_query(query, (userid, group_buying_id, quantity))

    if result:
        return jsonify({'message': 'Order created successfully'}), 200

    return jsonify({'error': 'Failed to create order'}), 500

# 查詢一筆訂單
@order_bp.route("/api/order/<int:order_id>", methods=["GET"])
@jwt_required()
def get_order_by_order_id(order_id):
    identity = get_jwt_identity()
    store_id = identity.get('store_id')

    query = """
                SELECT 
                `Order`.order_id,
                `Order`.userid,
                `Order`.group_buying_id,
                `Order`.quantity,
                `Order`.receive_status,
                Product.product_id, 
                Product.store_id, 
                Product.price, 
                Product.unit, 
                Product.product_describe, 
                Product.supplier_name, 
                Product.product_name,
                Product.product_picture,
                Group_buying_product.purchase_quantity,
                Group_buying_product.launch_date,
                Group_buying_product.statement_date,
                Group_buying_product.arrival_date,
                Group_buying_product.due_days,
                Group_buying_product.inventory,
                Group_buying_product.income,
                Group_buying_product.cost

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
            "receive_status": order[4],
            "product_id": order[5],
            "store_id": order[6],
            "price": order[7],
            "unit": order[8],
            "product_describe": order[9],
            "supplier_name": order[10],
            "product_name": order[11],
            "product_picture": order[12],
            "purchase_quantity": order[13],
            "launch_date": order[14],
            "statement_date": order[15],
            "arrival_date": order[16],
            "due_days": order[17],
            "inventory": order[18],
            "income": order[19],
            "cost": order[20]
        }
        return jsonify(order_dict), 200
    
    return jsonify({'message':'Fail to get order by orderid'}), 404

# 查詢一名客戶所有清單
@order_bp.route("/api/order/<string:userid>", methods=["GET"])
@jwt_required()
def get_all_orders_by_userid(userid):
    identity = get_jwt_identity()
    store_id = identity.get('store_id')

    query = """
                SELECT 
                `Order`.order_id,
                `Order`.userid,
                `Order`.group_buying_id,
                `Order`.quantity,
                `Order`.receive_status,
                Product.product_id, 
                Product.store_id, 
                Product.price, 
                Product.unit, 
                Product.product_describe, 
                Product.supplier_name, 
                Product.product_name,
                Product.product_picture,
                Group_buying_product.purchase_quantity,
                Group_buying_product.launch_date,
                Group_buying_product.statement_date,
                Group_buying_product.arrival_date,
                Group_buying_product.due_days,
                Group_buying_product.inventory,
                Group_buying_product.income,
                Group_buying_product.cost
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
                "receive_status": order[4],
                "product_id": order[5],
                "store_id": order[6],
                "price": order[7],
                "unit": order[8],
                "product_describe": order[9],
                "supplier_name": order[10],
                "product_name": order[11],
                "product_picture": order[12],
                "purchase_quantity": order[13],
                "launch_date": order[14],
                "statement_date": order[15],
                "arrival_date": order[16],
                "due_days": order[17],
                "inventory": order[18],
                "income": order[19],
                "cost": order[20]
            }
            )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get all orders by userid'}), 404

@order_bp.route("/api/<string:userid>/<int:status>", methods=["GET"])
@jwt_required()
def get_all_orders_by_userid_and_status(userid, status):
    if status == 0:
        status = False
    elif status == 1:
        status = True
    else:
        return jsonify({'message' : 'Invalid status'}), 404
    
    identity = get_jwt_identity()
    store_id = identity.get('store_id')
    
    query = """
                SELECT 
                `Order`.order_id,
                `Order`.userid,
                `Order`.group_buying_id,
                `Order`.quantity,
                `Order`.receive_status,
                Product.product_id, 
                Product.store_id, 
                Product.price, 
                Product.unit, 
                Product.product_describe, 
                Product.supplier_name, 
                Product.product_name,
                Product.product_picture,
                Group_buying_product.purchase_quantity,
                Group_buying_product.launch_date,
                Group_buying_product.statement_date,
                Group_buying_product.arrival_date,
                Group_buying_product.due_days,
                Group_buying_product.inventory,
                Group_buying_product.income,
                Group_buying_product.cost
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
                    "receive_status": order[4],
                    "product_id": order[5],
                    "store_id": order[6],
                    "price": order[7],
                    "unit": order[8],
                    "product_describe": order[9],
                    "supplier_name": order[10],
                    "product_name": order[11],
                    "product_picture": order[12],
                    "purchase_quantity": order[13],
                    "launch_date": order[14],
                    "statement_date": order[15],
                    "arrival_date": order[16],
                    "due_days": order[17],
                    "inventory": order[18],
                    "income": order[19],
                    "cost": order[20]
                }
            )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get all orders by userid and status'}), 404

#到貨時通知顧客：獲取一項團購商品的所有訂購者
@order_bp.route("/api/order/<int:group_buying_id>", methods = ["GET"])
@jwt_required()
def get_userid_by_group_buying_id(group_buying_id):
    claims = get_jwt()
    role = claims['role']

    if role != 'merchant':
        return jsonify({"message":"權限不足"}), 400
    
    query = """
                SELECT userid
                FROM `Order`
                WHERE group_buying_id = %s 
                AND receive_status = FALSE;
            """
    userids = execute_query(query, (group_buying_id,), True)

    if not userids:
        return jsonify({'message' : 'Fail to get all userid by group_buying_id'}), 404 

    message = '您訂購的商品已送達，請盡快取貨。'
    
    for userid in userids:
        send_message(userid, message)
    
    return jsonify({'message' : 'Send message successfully'}), 200