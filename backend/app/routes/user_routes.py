from flask import Blueprint, request, jsonify
from ..database import execute_query

from flask_jwt_extended import create_access_token, get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

user_bp = Blueprint('user', __name__)

def check_role(store_id, userid):
    query = "SELECT * FROM Group_buying_merchant WHERE store_id = %s AND merchant_userid = %s;"
    merchant_info = execute_query(query, (store_id, userid))
    # 已註冊商家
    if merchant_info:
        data = {
                "role" : "merchant",
                "info" : merchant_info
            }
        return data

    query = "SELECT * FROM Customer WHERE store_id = %s AND userid = %s;"
    customer_info = execute_query(query, (store_id, userid))
    # 已註冊消費者
    if customer_info:
        data = {
                "role" : "customer",
                "info" : customer_info
            }
        return data

    # 未註冊
    return {}

# 登入時呼叫授予身份，並更新user_name
@user_bp.route("/api/<string:store_id>/user", methods=["POST"])
def login_check(store_id):
    data = request.json
    userid = data.get('userid')
    user_name = data.get('user_name')

    role_info = check_role(store_id, userid)
    if role_info:
        if role_info["role"] == "merchant":
            identity = {"store_id": store_id, "userid": userid}
            additional_claims = {"role": "merchant"}
            access_token = create_access_token(identity=identity, additional_claims=additional_claims)
            return jsonify(access_token=access_token)

 
        elif role_info["role"] == "customer":

            # 更新user_name
            if role_info["info"][2] != user_name:
                query = "UPDATE Customer SET user_name = %s WHERE userid = %s AND store_id = %s"
                result = execute_query(query, (user_name, userid, store_id))
                if result:
                    print("secc update user_name")
                else:
                    print("fail to update user_name")

            identity = {"store_id": store_id, "userid": userid}
            additional_claims = {"role": "customer"}
            access_token = create_access_token(identity=identity, additional_claims=additional_claims)
            return jsonify(access_token=access_token)

    else:
        query = "INSERT INTO Customer (userid, store_id, user_name) VALUES(%s, %s, %s);"
        result = execute_query(query, (userid, store_id, user_name))
        if result:
            identity = {"store_id": store_id, "userid": userid}
            additional_claims = {"role": "customer"}
            access_token = create_access_token(identity=identity, additional_claims=additional_claims)
            return jsonify(access_token=access_token, message="Successfully enrolled")
        
        return jsonify({"message": "Enroll failed"}), 404

# 更改用戶電話
@user_bp.route("/api/<string:store_id>/user", methods=["PUT"])
@jwt_required()
def update_user_info(store_id):
    data = request.json
    userid = data.get('userid')
    phone = data.get('phone')

    role_info = check_role(store_id, userid)
    if not role_info:
        return jsonify({"message": "User not found"}), 404
    
    if role_info["role"] == "merchant":
        return jsonify({"message": "Merchant don't have phone"}), 404

    query = "UPDATE Customer SET phone = %s WHERE userid = %s AND store_id = %s"
    result = execute_query(query, (phone, userid, store_id))
    if result:
        return jsonify({"message": "Update user info successfully"}), 200
    
    return jsonify({"message": "Fail to update user info"}), 200

# 修改用戶blacklist
@user_bp.route("/api/<string:store_id>/user/<string:operation>", methods=["PUT"])
@jwt_required()
def update_user_blacklist(store_id, operation):
    data = request.json
    userid = data.get('userid')

    claims = get_jwt()
    role = claims['role']
    if role != 'merchant':
        return jsonify({"message":"權限不足"}), 400


    role_info = check_role(store_id, userid)
    if not role_info:
        return jsonify({"message": "User not found"}), 404
    
    if role_info["role"] == "merchant":
        return jsonify({"message": "Merchant don't have blacklist"}), 404
    
    blacklist = role_info["info"][4]
    if operation == "0":
        blacklist = 0
    elif operation == "1":
        blacklist += 1
    elif operation == "-1":
        blacklist -= 1
    else:
        return jsonify({"message": "Invalid operation"}), 404

    query = "UPDATE Customer SET blacklist = %s WHERE userid = %s AND store_id = %s"
    result = execute_query(query, (blacklist, userid, store_id))
    if result:
        return jsonify({"message": "Update user blacklist successfully"}), 200
    
    return jsonify({"message": "Fail to update user blacklist"}), 200