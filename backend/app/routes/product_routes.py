from flask import Blueprint, jsonify
from ..database import execute_query

product_bp = Blueprint('product', __name__)

@product_bp.route("/api/<string:merchant_lineid>/product", methods=["GET"])
def get_products(merchant_lineid):
    query = """
            SELECT 
                gb.group_buying_number,
                gb.merchant_lineid,
                gb.purchase_quantity,
                gb.launch_date,
                gb.statement_date,
                gb.arrival_date,
                gb.due_days,
                gb.inventory,
                gb.income,
                gb.cost,
                p.product_id,
                p.price,
                p.product_describe,
                p.supplier_name,
                p.product_name,
                p.product_picture
            FROM 
                Group_buying_product AS gb
            INNER JOIN 
                Product AS p ON gb.product_id = p.product_id;
            """
    products = execute_query(query, fetchall=True)

    data = []
    if products:
        for product in products:
            data.append(
                {
                    "group_buying_number" : product[0],
                    "merchant_lineid" : product[1],
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

    return jsonify({"message": "Products not found"}), 404

@product_bp.route("/api/<string:merchant_lineid>/product/<int:group_buying_number>", methods=["GET"])
def get_product(merchant_lineid, group_buying_number):
    query = """
            SELECT 
                gb.group_buying_number,
                gb.merchant_lineid,
                gb.purchase_quantity,
                gb.launch_date,
                gb.statement_date,
                gb.arrival_date,
                gb.due_days,
                gb.inventory,
                gb.income,
                gb.cost,
                p.product_id,
                p.price,
                p.product_describe,
                p.supplier_name,
                p.product_name,
                p.product_picture
            FROM 
                Group_buying_product AS gb
            INNER JOIN 
                Product AS p ON gb.product_id = p.product_id
            WHERE 
                gb.merchant_lineid = %s
            AND
                gb.group_buying_number = %s;
            """

    product = execute_query(query, (merchant_lineid, group_buying_number))

    if product:
        product_dict = {
            "group_buying_number" : product[0],
            "merchant_lineid" : product[1],
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

    return jsonify({"message": "Product not found"}), 404
