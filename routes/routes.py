from flask import Blueprint , request, jsonify
from services.services import create_member , list_members , update_member , remove_member , get_by_id , search_by_name
member_bp = Blueprint("member_bp" , __name__)
@member_bp.route("/member", methods = ["POST"])
def create():
    response , status = create_member(request.json)
    return jsonify(response) , status
@member_bp.route("/member" , methods = ["GET"])
def list_all():
    response , status = list_members()
    return jsonify(response) , status
@member_bp.route("/member/<member_id>" , methods = ["DELETE"])
def delete(member_id):
    response , status = remove_member(member_id)
    return jsonify(response) , status
@member_bp.route("/member/<member_id>" , methods = ["PUT"])
def update(member_id):
    response , status = update_member(request.json , member_id)
    return jsonify(response) , status
@member_bp.route("/member/<member_id>" , methods = ["GET"])
def search_by_id(member_id):
    response , statius = get_by_id(member_id)
    return jsonify(response) , statius
@member_bp.status("/member/<name>" , methods = ["GET"])
def get_by_name(name):
    response , status = jsonify(response)
    return jsonify(response) , status
