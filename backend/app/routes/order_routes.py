import datetime
from flask import Blueprint, request, jsonify
from ..database import execute_query
from ..sendmess import send_message

from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required

order_bp = Blueprint('order', __name__)

# 提交一筆訂單
@order_bp.route("/api/order", methods=["POST"])
@jwt_required()
def create_order():
    """
    提交一筆訂單
    ---
    tags:
      - Order
    security:
      - APIKeyHeader: []
    parameters:
      - name: body
        in: body
        schema:
          type: object
          required:
            - group_buying_id
            - quantity
          properties:
            group_buying_id:
              type: integer
              description: group_buying_id
              default: 1
            quantity:
              type: integer
              description: 購買數量
              default: 3
    responses:
      201:
        description: Order created successfully
        example: {'message': 'Order created successfully'}
      500:
        description: Failed to create order
        example: {'error': 'Failed to create order'}
    """
    data = request.json
    group_buying_id = data.get('group_buying_id')
    quantity = data.get('quantity')

    identity = get_jwt_identity()
    userid = identity.get('userid')

    query = "INSERT INTO `Order` (userid, group_buying_id, quantity) VALUES (%s, %s, %s)"
    result = execute_query(query, (userid, group_buying_id, quantity))

    if result:
        return jsonify({'message': 'Order created successfully'}), 201

    return jsonify({'error': 'Failed to create order'}), 500

# 查詢一筆訂單
@order_bp.route("/api/order/<int:order_id>", methods=["GET"])
@jwt_required()
def get_order_by_order_id(order_id):
    """
    用order_id查詢一筆訂單
    ---
    tags:
      - Order
    security:
      - APIKeyHeader: []
    parameters:
      - name: order_id
        in: path
        type: integer
        required: true
        description: Order ID
        default: 1
    responses:
      200:
        description: Order details
      404:
        description: Fail to get order by orderid
    """
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

# 用userid查詢一名客戶所有清單
@order_bp.route("/api/order/<string:userid>", methods=["GET"])
@jwt_required()
def get_all_orders_by_userid(userid):
    """
    用userid查詢一名客戶所有清單
    ---
    tags:
      - Order
    security:
      - APIKeyHeader: []
    parameters:
      - name: userid
        in: path
        type: string
        required: true
        description: userid
    responses:
      200:
        description: User's orders
      404:
        description: Fail to get all orders by userid
    """
    identity = get_jwt_identity()
    store_id = identity.get('store_id')

    query = """
                SELECT 
                    p.product_name, 
                    gbp.arrival_date, 
                    gbp.due_days, 
                    o.receive_status,
                    p.product_picture
                FROM 
                    `Order` o
                JOIN 
                    Group_buying_product gbp ON o.group_buying_id = gbp.group_buying_id
                JOIN 
                    Product p ON gbp.product_id = p.product_id
                JOIN 
                    Customer c ON o.userid = c.userid AND c.store_id = p.store_id
                WHERE 
                    p.store_id = %s AND 
                    c.userid = %s;
            """ 
    orders = execute_query(query, (store_id, userid), True)
    
    data = []
    if orders:
        for order in orders:
            arrival_date = order[1]
            due_days = order[2]
            due_date = arrival_date + datetime.timedelta(days=due_days)
            data.append(
            {
                "product_name": order[0],
                "due_date": due_date,
                "receive_status": order[3],
                "product_picture": order[4]
            }
            )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get all orders by userid'}), 404


# 用手機查詢一名客戶所有清單
@order_bp.route("/api/order/phone/<string:phone>", methods=["GET"])
@jwt_required()
def get_all_orders_by_phone(phone):
    """
    用手機查詢一名客戶所有訂單
    ---
    tags:
      - Order
    security:
      - APIKeyHeader: []
    parameters:
      - name: phone
        in: path
        type: string
        required: true
        description: 手機號碼
    responses:
      200:
        description: User's orders
      404:
        description: Fail to get all orders by phone
    """
    identity = get_jwt_identity()
    store_id = identity.get('store_id')

    query = """
                SELECT 
                    c.user_name, 
                    p.product_name, 
                    gbp.purchase_quantity, 
                    c.phone, 
                    o.receive_status, 
                    DATE(gbp.arrival_date) AS arrival_date, 
                    gbp.due_days
                FROM 
                    Customer c
                JOIN 
                    `Order` o ON c.userid = o.userid
                JOIN 
                    Group_buying_product gbp ON o.group_buying_id = gbp.group_buying_id
                JOIN 
                    Product p ON gbp.product_id = p.product_id
                WHERE c.phone = %s
                AND p.store_id = %s;
            """
    orders = execute_query(query, (phone, store_id), True)
    
    data = []
    if orders:
        for order in orders:
            arrival_date = order[5]
            due_days = order[6]
            due_date = arrival_date + datetime.timedelta(days=due_days)
            data.append(
            {
                "user_name": order[0],
                "product_name": order[1],
                "purchase_quantity": order[2],
                "phone": order[3],
                "receive_status": order[4],
                "due_date": due_date
            }
            )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get all orders by phone'}), 404

# 從商品名稱獲取一項團購商品的所有訂購者的訂單資料
@order_bp.route("/api/order/productname/<string:product_name>", methods = ["GET"])
def get_userinfo_by_product_name(product_name):
    """
    從商品名稱獲取一項團購商品的所有訂購者
    ---
    tags:
      - Order
    security:
      - APIKeyHeader: []
    parameters:
      - name: product_name
        in: path
        type: string
        required: true
        description: 產品名稱
    responses:
      200:
        description: User's orders
      404:
        description: Fail to get all orders by product_name
    """
    identity = get_jwt_identity()
    store_id = identity.get('store_id')

    query = '''SELECT c.user_name, o.quantity, g.arrival_date, g.due_days, c.phone, o.receive_status
                FROM `Order` AS o,`Group_buying_product` AS g,`Product` AS p, `Customer` AS c
                WHERE o.group_buying_id = g.group_buying_id
                AND g.product_id = p.product_id
                AND c.userid = o.userid
                AND p.store_id = %s
                AND p.product_name = %s;             
    '''
    orders = execute_query(query, (store_id, product_name), True)
    data = []
    if orders:
        for order in orders:
            data.append(
                {
                  "user_name" : order[0],
                  "quantity" : order[1],
                  "due_date" : order[2] + datetime.timedelta(days=order[3]),
                  "phone" : order[4],
                  "receive_status" : order[5]
                }
             )
        return jsonify(data), 200

    return jsonify({'message' : 'Fail to get all userinfo by product_name'}), 404

#到貨時通知顧客：獲取一項團購商品的所有訂購者
@order_bp.route("/api/order/notify/<int:group_buying_id>", methods = ["GET"])
@jwt_required()
def get_userid_by_group_buying_id(group_buying_id):
    """
    一鍵通知該團購所有未取貨的顧客
    ---
    tags:
      - Order
    security:
      - APIKeyHeader: []
    parameters:
      - name: group_buying_id
        in: path
        type: integer
        required: true
        description: group_buying_id
    responses:
      200:
        description: Send message successfully
      403:
        description: 權限不足
      404:
        description: Fail to get all userid by group_buying_id
    """
    claims = get_jwt()
    role = claims['role']

    if role != 'merchant':
        return jsonify({"message":"權限不足"}), 403
    
    query = """
                SELECT O.userid, P.product_name, P.price, O.quantity, DATE(GBP.arrival_date) AS arrival_date, GBP.due_days
                FROM `Order` O
                JOIN Group_buying_product GBP ON O.group_buying_id = GBP.group_buying_id
                JOIN Product P ON GBP.product_id = P.product_id
                WHERE O.group_buying_id = %s 
                AND O.receive_status = FALSE;

            """
    results = execute_query(query, (group_buying_id,), True)

    if not results:
        return jsonify({'message' : 'Fail to get all userid by group_buying_id'}), 404

    for result in results:
        userid = result[0]
        product_name = result[1]
        price = result[2]
        quantity = result[3]
        arrival_date = result[4]
        due_days = result[5]
        due_date = arrival_date + datetime.timedelta(days=due_days)
        message = f'您訂購的{product_name}已到貨，請備妥${price*quantity}，於{due_date}前來店內取貨，謝謝。'

        send_message(userid, message)
    
    return jsonify({'message' : 'Send message successfully'}), 200