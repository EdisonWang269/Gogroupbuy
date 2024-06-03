from flask import Blueprint, jsonify, request
from ..database import execute_query

from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required

product_bp = Blueprint("product", __name__)


# 獲取商家的所有商品列表
@product_bp.route("/api/product", methods=["GET"])
@jwt_required()
def get_all_products_by_storeid():
    """
    獲取商家的所有商品列表
    ---
    tags:
      - Product
    security:
      - APIKeyHeader: []
    responses:
      200:
        description: Get all products by storeid successfully
        schema:
          type: object
          properties:
            statement_date:
              type: string
              example: 2021-06-01
            price:
              type: integer
              example: 100
            unit:
              type: string
              example: 件
            product_name:
              type: string
              example: 衣服
            product_picture:
              type: string
              example: shirt.jpg
        examples:
          application/json:
            statement_date: 2021-06-01
            price: 100
            unit: 件
            product_name: 衣服
            product_picture: shirt.jpg
      404:
        description: Fail to get all products by storeid
        schema:
          type: object
          properties:
            message:
              type: string
              example: Fail to get all products by storeid
    """
    identity = get_jwt_identity()
    store_id = identity.get("store_id")

    query = """
                SELECT 
                    GBP.statement_date,
                    GBP.group_buying_id,
                    P.price,
                    P.unit,
                    P.product_name,
                    P.product_picture, 
                    P.product_id,
                    P.product_describe
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
                    "statement_date": product[0],
                    "price": product[1],
                    "unit": product[2],
                    "product_name": product[3],
                    "product_picture": product[4],
                    "product_id": product[5],
                    "group_buying_id": product[6],
                    "product_describe": product[7],
                }
            )
        return jsonify(data), 200

    return jsonify({"message": "Fail to get all products by store_id"}), 404


# 以store_id獲取商家的所有團購商品列表
@product_bp.route("/api/product/groupbuying", methods=["GET"])
@jwt_required()
def get_all_groupbuying_products_by_storeid():
    """
    以store_id獲取商家的所有團購商品名稱列表
    ---
    tags:
      - Product
    security:
      - APIKeyHeader: []
    responses:
      200:
        description: Get all groupbuying products by storeid successfully
        schema:
          type: object
          properties:
            product_name:
              type: string
              example: 衣服
        examples:
          application/json:
            product_name: 衣服
      403:
        description: 權限不足
        schema:
          type: object
          properties:
            message:
              type: string
              example: 權限不足
        examples:
          application/json:
            message: 權限不足
      404:
        description: Fail to get all groupbuying products by storeid
        schema:
          type: object
          properties:
            message:
              type: string
              example: Fail to get all groupbuying products by store_id
    """
    identity = get_jwt_identity()
    store_id = identity.get("store_id")

    claims = get_jwt()
    role = claims["role"]
    if role != "merchant":
        return jsonify({"message": "權限不足"}), 403

    query = """
                SELECT 
                    p.product_name
                FROM 
                    Group_buying_product g
                JOIN 
                    Product p ON g.product_id = p.product_id
                WHERE 
                    p.store_id = %s;
            """
    products = execute_query(query, (store_id,), True)
    if products:
        data = []
        for product in products:
            data.append({"product_name": product[0]})
        return jsonify(data), 200
    return jsonify({"message": "Fail to get all groupbuying products by store_id"}), 404


# # 獲取一筆團購訂單
# @product_bp.route("/api/product/<int:group_buying_id>", methods=["GET"])
# @jwt_required()
# def get_product_by_group_buying_id(group_buying_id):
#     """
#     獲取一筆團購訂單
#     ---
#     tags:
#         - Product
#     security:
#       - APIKeyHeader: []
#     parameters:
#       - name: group_buying_id
#         in: path
#         type: integer
#         required: true
#         description: group_buying_id
#     responses:
#         200:
#             description: Get product by groupbuying id successfully
#         404:
#             description: Fail to get product by groupbuying id
#     """
#     identity = get_jwt_identity()
#     store_id = identity.get('store_id')

#     query = """
#                 SELECT
#                     GBP.group_buying_id,
#                     GBP.purchase_quantity,
#                     GBP.launch_date,
#                     GBP.statement_date,
#                     GBP.arrival_date,
#                     GBP.due_days,
#                     GBP.inventory,
#                     GBP.income,
#                     GBP.cost,
#                     P.product_id,
#                     P.store_id,
#                     P.price,
#                     p.unit,
#                     P.product_describe,
#                     P.supplier_name,
#                     P.product_name,
#                     P.product_picture
#                 FROM
#                     Group_buying_product GBP
#                 INNER JOIN
#                     Product P ON GBP.product_id = P.product_id
#                 WHERE
#                     P.store_id = %s
#                 AND
#                     GBP.group_buying_id = %s;
#             """

#     product = execute_query(query, (store_id, group_buying_id))

#     if product:
#         product_dict =  {
#                     "group_buying_id": product[0],
#                     "purchase_quantity": product[1],
#                     "launch_date": product[2],
#                     "statement_date": product[3],
#                     "arrival_date": product[4],
#                     "due_days": product[5],
#                     "inventory": product[6],
#                     "income": product[7],
#                     "cost": product[8],
#                     "product_id": product[9],
#                     "store_id": product[10],
#                     "price": product[11],
#                     "unit": product[12],
#                     "product_describe": product[13],
#                     "supplier_name": product[14],
#                     "product_name": product[15],
#                     "product_picture": product[16]
#                 }
#         return jsonify(product_dict), 200

#     return jsonify({"message": "Fail to get product by groupbuying id"}), 404


# 新增一項商品
@product_bp.route("/api/product", methods=["POST"])
@jwt_required()
def create_product():
    """
    新增一項商品
    ---
    tags:
      - Product
    security:
      - APIKeyHeader: []
    parameters:
      - name: body
        in: body
        schema:
          type: object
          required:
            - price
            - unit
            - product_describe
            - supplier_name
            - product_name
            - product_picture
          properties:
            price:
              type: integer
              description: 商品價格
              example: 100
            unit:
              type: string
              description: 商品單位
              example: 件
            product_describe:
              type: string
              description: 商品描述
              example: 這是一個好商品
            supplier_name:
              type: string
              description: 供應商名稱
              example: AAA供應商
            product_name:
              type: string
              description: 商品名稱
              example: 衣服
            product_picture:
              type: string
              description: 商品圖片
              example: shirt.jpg
    responses:
        201:
            description: Pruduct created successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Product created successfully
            examples:
              application/json:
                message: Product created successfully
        403:
            description: 權限不足
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: 權限不足
            examples:
              application/json:
                message: 權限不足
        500:
            description: Failed to create product
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Failed to create product
            examples:
              application/json:
                error: Failed to create product
    """
    data = request.json
    price = data.get("price")
    unit = data.get("unit")
    product_describe = data.get("product_describe")
    supplier_name = data.get("supplier_name")
    product_name = data.get("product_name")
    product_picture = data.get("product_picture")

    identity = get_jwt_identity()
    store_id = identity.get("store_id")

    claims = get_jwt()
    role = claims["role"]

    if role != "merchant":
        return jsonify({"message": "權限不足"}), 403

    query = """
                INSERT INTO `PRODUCT` (store_id, price, unit, product_describe, supplier_name, product_name, product_picture)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
    result = execute_query(
        query,
        (
            store_id,
            price,
            unit,
            product_describe,
            supplier_name,
            product_name,
            product_picture,
        ),
    )

    if result:
        return jsonify({"message": "Pruduct created successfully"}), 201

    return jsonify({"error": "Failed to create product"}), 500


# 新增一項團購商品
@product_bp.route("/api/product/ontheshelves", methods=["POST"])
@jwt_required()
def create_group_buying_product():
    """
    新增一項團購商品
    ---
    tags:
      - Product
    security:
      - APIKeyHeader: []
    parameters:
      - name: body
        in: body
        schema:
          type: object
          required:
            - launch_date
            - statement_date
            - product_id
          properties:
            launch_date:
              type: string
              format: date
              description: 上架日期
              example: 2021-06-01
            statement_date:
              type: string
              format: date
              description: 截止日期
              example: 2021-06-10
            product_id:
              type: integer
              description: product_id
              example: 1
    responses:
        201:
            description: Product created successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: group_buying_product created successfully
            examples:
              application/json:
                message: group_buying_product created successfully
        403:
            description: 權限不足
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: 權限不足
            examples:
              application/json:
                message: 權限不足
        404:
            description: this product not in this store
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: this product not in this store
            examples:
              application/json:
                error: this product not in this store
        500:
            description: Failed to create product
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Failed to create group_buying_product
            examples:
              application/json:
                error: Failed to create group_buying_product
    """
    data = request.json
    launch_date = data.get("launch_date")
    statement_date = data.get("statement_date")
    product_id = data.get("product_id")

    identity = get_jwt_identity()
    store_id = identity.get("store_id")

    claims = get_jwt()
    role = claims["role"]

    if role != "merchant":
        return jsonify({"message": "權限不足"}), 403

    query = "SELECT store_id FROM Product WHERE product_id = %s"
    sid = execute_query(query, (product_id,))
    if sid[0] == store_id:
        query = "INSERT INTO `Group_buying_product`(launch_date, statement_date, product_id) VALUES(%s, %s, %s);"
        result = execute_query(
            query,
            (
                launch_date,
                statement_date,
                product_id,
            ),
        )
        if result:
            return (
                jsonify({"message": "group_buying_product created successfully"}),
                201,
            )
        return jsonify({"error": "Failed to create group_buying_product"}), 500

    return jsonify({"error": "this product not in this store"}), 404


# 結單時管理者進貨，更新團購商品：inventory/purchase_quantity/cost
@product_bp.route("/api/product/<int:group_buying_id>", methods=["PUT"])
@jwt_required()
def update_purchase_quantity(group_buying_id):
    """
    結單時管理者進貨，更新團購商品：inventory/purchase_quantity/cost
    ---
    tags:
      - Product
    security:
      - APIKeyHeader: []
    parameters:
          - name: group_buying_id
            in: path
            type: integer
            required: true
            description: group_buying_id
            default: 1
          - name: body
            in: body
            schema:
                type: object
                required:
                    - purchase_quantity
                    - cost
                properties:
                    purchase_quantity:
                      type: integer
                      description: 進貨數量
                      example: 100
                    cost:
                      type: integer
                      description: 進貨成本
                      example: 2500
    responses:
        200:
            description: group_buying_product purchase_quantity updated successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: group_buying_product purchase_quantity updated successfully
            examples:
              application/json:
                message: group_buying_product purchase_quantity updated successfully
        403:
            description: 權限不足
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: 權限不足
            examples:
              application/json:
                message: 權限不足
        500:
            description: Failed to update group_buying_product purchase_quantity
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Failed to update group_buying_product purchase_quantity
            examples:
              application/json:
                error: Failed to update group_buying_product purchase_quantity
    """
    data = request.json
    purchase_quantity = data.get("purchase_quantity")
    cost = data.get("cost")

    claims = get_jwt()
    role = claims["role"]

    if role != "merchant":
        return jsonify({"message": "權限不足"}), 403

    query = """
                UPDATE `Group_buying_product`
                SET purchase_quantity = %s, cost = %s, inventory = %s
                WHERE group_buying_id = %s
            """
    result = execute_query(
        query,
        (
            purchase_quantity,
            cost,
            purchase_quantity,
            group_buying_id,
        ),
    )
    if result:
        return (
            jsonify(
                {
                    "message": "group_buying_product purchase_quantity updated successfully"
                }
            ),
            200,
        )
    return (
        jsonify({"error": "Failed to update group_buying_product purchase_quantityt"}),
        500,
    )


# 到貨時(更新團購商品：到貨日期arrival_date/領取截止日due_days)
@product_bp.route("/api/product/arrival/<int:group_buying_id>", methods=["PUT"])
@jwt_required()
def update_arrival_date(group_buying_id):
    """
    到貨時(更新團購商品：到貨日期arrival_date/領取截止日due_days)
    ---
    tags:
      - Product
    security:
      - APIKeyHeader: []
    parameters:
          - name: group_buying_id
            in: path
            type: integer
            required: true
            description: group_buying_id
            default: 1
          - name: body
            in: body
            schema:
                type: object
                required:
                    - arrival_date
                    - due_days
                properties:
                    arrival_date:
                      type: string
                      format: date
                      description: 到貨日期
                      example: 2021-06-01
                    due_days:
                      type: integer
                      description: 領取時限(幾天)
                      example: 7
    responses:
        200:
            description: arrival_date updated successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: arrival_date updated successfully
            examples:
              application/json:
                message: arrival_date updated successfully
        403:
            description: 權限不足
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: 權限不足
            examples:
              application/json:
                message: 權限不足
        500:
            description: Failed to update arrival_date
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Failed to update arrival_date
            examples:
              application/json:
                error: Failed to update arrival_date
    """
    data = request.json
    arrival_date = data.get("arrival_date")
    due_days = data.get("due_days")

    claims = get_jwt()
    role = claims["role"]

    if role != "merchant":
        return jsonify({"message": "權限不足"}), 403

    query = """
                UPDATE `Group_buying_product`
                SET arrival_date = %s, due_days = %s
                WHERE group_buying_id = %s
            """

    result = execute_query(query, (arrival_date, due_days, group_buying_id))
    if result:
        return jsonify({"message": "arrival_date updated successfully"}), 200
    return jsonify({"error": "Failed to update arrival_date"}), 500


# 增加現場購買客人（更新團購商品庫存量）
@product_bp.route(
    "/api/product/instore_shopping/<int:group_buying_id>", methods=["PUT"]
)
@jwt_required()
def update_inventory(group_buying_id):
    """
    增加現場購買客人（更新團購商品庫存量）
    ---
    tags:
      - Product
    security:
      - APIKeyHeader: []
    parameters:
          - name: group_buying_id
            in: path
            type: integer
            required: true
            description: group_buying_id
            default: 1
          - name: body
            in: body
            schema:
                type: object
                required:
                    - instore_purchase_quantity
                properties:
                    instore_purchase_quantity:
                      type: integer
                      description: 現場購買數量
                      example: 3
    responses:
        200:
            description: inventory updated successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: inventory updated successfully
            examples:
              application/json:
                message: inventory updated successfully
        403:
            description: 權限不足
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: 權限不足
            examples:
              application/json:
                message: 權限不足
        500:
            description: Failed to update inventory
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Failed to update inventory
            examples:
              application/json:
                error: Failed to update inventory
    """
    data = request.json
    instore_purchase_quantity = data.get("instore_purchase_quantity")

    claims = get_jwt()
    role = claims["role"]
    if role != "merchant":
        return jsonify({"message": "權限不足"}), 403

    query = """SELECT inventory FROM Group_buying_product WHERE group_buying_id = %s"""
    inventory = execute_query(query, (group_buying_id,))
    if inventory[0] - instore_purchase_quantity < 0:
        return jsonify({"error": "inventory can not be negative"}), 500

    query = """UPDATE Group_buying_product
                SET inventory = inventory - %s
                WHERE group_buying_id = %s"""
    result = execute_query(query, (instore_purchase_quantity, group_buying_id))

    if result:
        return jsonify({"message": "inventory updated successfully"}), 200
    return jsonify({"error": "Failed to update inventory"}), 500


# 下架商品時(更新團購商品：income)
@product_bp.route("/api/product/income/<int:group_buying_id>", methods=["PUT"])
@jwt_required()
def calculate_income(group_buying_id):
    """
    下架商品時(更新團購商品：income)
    ---
    tags:
      - Product
    security:
      - APIKeyHeader: []
    parameters:
          - name: group_buying_id
            in: path
            type: integer
            required: true
            description: group_buying_id
            default: 1
    responses:
        200:
            description: income updated successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: income updated successfully
            examples:
              application/json:
                message: income updated successfully
        403:
            description: 權限不足
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: 權限不足
            examples:
              application/json:
                message: 權限不足
        500:
            description: Failed to update income
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: Failed to update income
            examples:
              application/json:
                error: Failed to update income
    """
    claims = get_jwt()
    role = claims["role"]
    if role != "merchant":
        return jsonify({"message": "權限不足"}), 403

    query = """with get_income (income) as
                (SELECT (g.purchase_quantity - g.inventory) * p.price
		        FROM Group_buying_product AS g, Product AS p
		        WHERE g.product_id = p.product_id
		        AND g.group_buying_id = %s)
          
            UPDATE Group_buying_product
            SET income = (select income from get_income)
            WHERE group_buying_id = %s"""
    result = execute_query(query, (group_buying_id, group_buying_id))

    if result:
        return jsonify({"message": "income updated successfully"}), 200
    return jsonify({"error": "Failed to update income"}), 500
