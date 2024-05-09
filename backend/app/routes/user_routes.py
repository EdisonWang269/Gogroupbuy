from flask import Blueprint, request, jsonify
from ..database import execute_query

user_bp = Blueprint('user', __name__)

@user_bp.route("/api/<string:company_id>/user", methods=["POST"])
def create_user(company_id):
    data = request.json
    line_id = data.get('customer_lineid')
    phone = int(data.get('phone'))

    try:
        query = "INSERT INTO Customer (customer_lineid, phone) VALUES (%s, %s)"
        execute_query(query, (line_id, phone))
        return jsonify({'message': 'New user created successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route("/api/<string:company_id>/user/<string:customer_id>", methods=["GET"])
def get_user(company_id, customer_id):
    try:
        query = "SELECT * FROM customer WHERE customer_lineid = %s"
        user_data = execute_query(query, (customer_id,))
        if user_data:
            user_dict = {
                "customer_id": user_data[0],
                "customer_name": user_data[1],
            }
            return jsonify(user_dict)
        return "User not found", 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route("/api/<string:company_id>/user", methods=["GET"])
def get_users(company_id):
    try:
        query = "SELECT * FROM customer"
        user_datas = execute_query(query, fetchall=True)
        data = []
        if user_datas:
            for user_data in user_datas:
                data.append(
                    {
                        "customer_id": user_data[0],
                        "customer_name": user_data[1],
                    }
                )
            return jsonify(data), 200
        return "User not found", 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
