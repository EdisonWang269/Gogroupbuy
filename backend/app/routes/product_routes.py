from flask import Blueprint, jsonify
from ..database import execute_query

product_bp = Blueprint('product', __name__)

# 獲取商家的所有商品列表
@product_bp.route("/api/<string:en_store_name>/product", methods=["GET"])
def get_all_products_by_storename(en_store_name):
    query = """
                SELECT 
                    GBP.group_buying_id,
                    GBP.en_store_name,
                    GBP.purchase_quantity,
                    GBP.launch_date,
                    GBP.statement_date,
                    GBP.arrival_date,
                    GBP.due_days,
                    GBP.inventory,
                    GBP.income,
                    GBP.cost,
                    P.product_id,
                    P.price,
                    P.product_describe,
                    P.supplier_name,
                    P.product_name,
                    P.product_picture
                FROM 
                    Group_buying_product GBP
                INNER JOIN 
                    Product P ON GBP.product_id = P.product_id
                WHERE
                    GBP.en_store_name = %s;
            """
    
    products = execute_query(query, (en_store_name,), True)

    data = []
    if products:
        for product in products:
            data.append(
                {
                    "group_buying_id" : product[0],
                    "en_store_name" : product[1],
                    "purchase_quantity" : product[2],
                    "launch_date" : product[3],
                    "statement_date" : product[4],
                    "arrival_date" : product[5],
                    "due_days" : product[6],
                    "inventory" : product[7],
                    "income" : product[8],
                    "cost" : product[9],
                    "product_id" : product[10],
                    "price" : product[11],
                    "product_describe" : product[12],
                    "supplier_name" : product[13],
                    "product_name" : product[14],
                    "product_picture" : product[15]
                }
            )
        return jsonify(data), 200

    return jsonify({"message": "Fail to get all products by storename"}), 404

# 獲取一筆團購訂單
@product_bp.route("/api/<string:en_store_name>/product/<int:group_buying_id>", methods=["GET"])
def get_product_by_group_buying_id(en_store_name, group_buying_id):
    query = """
                SELECT 
                    GBP.group_buying_id,
                    GBP.en_store_name,
                    GBP.purchase_quantity,
                    GBP.launch_date,
                    GBP.statement_date,
                    GBP.arrival_date,
                    GBP.due_days,
                    GBP.inventory,
                    GBP.income,
                    GBP.cost,
                    P.product_id,
                    P.price,
                    P.product_describe,
                    P.supplier_name,
                    P.product_name,
                    P.product_picture
                FROM 
                    Group_buying_product GBP
                INNER JOIN 
                    Product P ON GBP.product_id = P.product_id
                WHERE
                    GBP.en_store_name = %s
                AND
                    GBP.group_buying_id = %s;
            """

    product = execute_query(query, (en_store_name, group_buying_id))

    if product:
        product_dict = {
                            "group_buying_id" : product[0],
                            "en_store_name" : product[1],
                            "purchase_quantity" : product[2],
                            "launch_date" : product[3],
                            "statement_date" : product[4],
                            "arrival_date" : product[5],
                            "due_days" : product[6],
                            "inventory" : product[7],
                            "income" : product[8],
                            "cost" : product[9],
                            "product_id" : product[10],
                            "price" : product[11],
                            "product_describe" : product[12],
                            "supplier_name" : product[13],
                            "product_name" : product[14],
                            "product_picture" : product[15]
                        }
        return jsonify(product_dict), 200

    return jsonify({"message": "Fail to get product by group buying id"}), 404
