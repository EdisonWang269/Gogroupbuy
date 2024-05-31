from flask import Blueprint, jsonify, request
from ..database import execute_query

from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required

product_bp = Blueprint('product', __name__)

# 獲取商家的所有商品列表
@product_bp.route("/api/product", methods=["GET"])
@jwt_required()
def get_all_products_by_storename():
    identity = get_jwt_identity()
    store_id = identity.get('store_id')

    query = """
                SELECT 
                    GBP.group_buying_id,
                    GBP.purchase_quantity,
                    GBP.launch_date,
                    GBP.statement_date,
                    GBP.arrival_date,
                    GBP.due_days,
                    GBP.inventory,
                    GBP.income,
                    GBP.cost,
                    P.product_id,
                    P.store_id,
                    P.price,
                    P.unit,
                    P.product_describe,
                    P.supplier_name,
                    P.product_name,
                    P.product_picture
                FROM 
                    Group_buying_product GBP
                INNER JOIN 
                    Product P ON GBP.product_id = P.product_id
                WHERE
                    P.store_id = %s;
            """
    
    products = execute_query(query, (store_id,), True)

    data = []
    if products:
        for product in products:
            data.append(
                {
                    "group_buying_id": product[0],
                    "purchase_quantity": product[1],
                    "launch_date": product[2],
                    "statement_date": product[3],
                    "arrival_date": product[4],
                    "due_days": product[5],
                    "inventory": product[6],
                    "income": product[7],
                    "cost": product[8],
                    "product_id": product[9],
                    "store_id": product[10],
                    "price": product[11],
                    "unit": product[12],
                    "product_describe": product[13],
                    "supplier_name": product[14],
                    "product_name": product[15],
                    "product_picture": product[16]
                }
            )
        return jsonify(data), 200

    return jsonify({"message": "Fail to get all products by storename"}), 404

# 獲取一筆團購訂單
@product_bp.route("/api/product/<int:group_buying_id>", methods=["GET"])
@jwt_required()
def get_product_by_group_buying_id(group_buying_id):
    identity = get_jwt_identity()
    store_id = identity.get('store_id')

    query = """
                SELECT 
                    GBP.group_buying_id,
                    GBP.purchase_quantity,
                    GBP.launch_date,
                    GBP.statement_date,
                    GBP.arrival_date,
                    GBP.due_days,
                    GBP.inventory,
                    GBP.income,
                    GBP.cost,
                    P.product_id,
                    P.store_id,
                    P.price,
                    p.unit,
                    P.product_describe,
                    P.supplier_name,
                    P.product_name,
                    P.product_picture
                FROM 
                    Group_buying_product GBP
                INNER JOIN 
                    Product P ON GBP.product_id = P.product_id
                WHERE
                    P.store_id = %s
                AND
                    GBP.group_buying_id = %s;
            """

    product = execute_query(query, (store_id, group_buying_id))

    if product:
        product_dict =  {
                    "group_buying_id": product[0],
                    "purchase_quantity": product[1],
                    "launch_date": product[2],
                    "statement_date": product[3],
                    "arrival_date": product[4],
                    "due_days": product[5],
                    "inventory": product[6],
                    "income": product[7],
                    "cost": product[8],
                    "product_id": product[9],
                    "store_id": product[10],
                    "price": product[11],
                    "unit": product[12],
                    "product_describe": product[13],
                    "supplier_name": product[14],
                    "product_name": product[15],
                    "product_picture": product[16]
                }
        return jsonify(product_dict), 200

    return jsonify({"message": "Fail to get product by groupbuying id"}), 404
    
#新增一項商品
@product_bp.route("/api/product", methods=["POST"])
@jwt_required()
def create_product():
    data = request.json     
    price = data.get('price')
    unit = data.get('unit')
    product_describe = data.get('product_describe')
    supplier_name = data.get('supplier_name')
    product_name = data.get('product_name')
    product_picture = data.get('product_picture')

    identity = get_jwt_identity()
    store_id = identity.get('store_id')

    claims = get_jwt()
    role = claims['role']

    if role != 'merchant':
        return jsonify({"message":"權限不足"}), 400

    query = """
                INSERT INTO `PRODUCT` (store_id, price, unit, product_describe, supplier_name, product_name, product_picture)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
    result = execute_query(query,(store_id, price, unit, product_describe, supplier_name, product_name, product_picture))
    
    if result:
        return jsonify({'message': 'Pruduct created successfully'}), 200
    
    return jsonify({'error': 'Failed to create product'}), 500

