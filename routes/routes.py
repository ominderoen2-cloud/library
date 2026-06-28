from flask import Blueprint , request, jsonify
from services.services import create_member , list_members , update_member , remove_member , get_by_member_id, create_book, get_all_books , get_one_book , borrow_book , return_book,check_book_status, remove_book
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
    response , statius = get_by_member_id(member_id)
    return jsonify(response) , statius
@member_bp.route("/book" , methods = ["POST"])
def create_book_route():
    response , status = create_book(request.json)
    return jsonify(response), status
                 
@member_bp.route("/book/<book_id>" , methods = ["GET"])
def one_book(book_id):
    response , status = get_one_book(book_id)
    return jsonify(response) , status
@member_bp.route("/book" , methods = ["GET"])
def list_books():
    response , status = get_all_books()
    return jsonify(response) , status
@member_bp.route("/borrow" , methods = ["POST"])
def borrow_book_route():
    response , status = borrow_book(request.json)
    return jsonify(response) , status
@member_bp.route("/borrow/<borrow_id>/return" , methods = ["POST"])
def return_book_route(borrow_id):
    response , status = return_book(request.json, borrow_id)
    return jsonify(response) , status
@member_bp.route("/borrow/<book_id>" , methods = ["GET"] )
def book_status(book_id):
    response , status = check_book_status(book_id)
    return jsonify(response) , status
@member_bp.route("/book/<book_id>" , methods = ["DELETE"])
def delete_book_route(book_id):
    response , status = remove_book(book_id)
    return jsonify(response) , status
#library/routes/routes.py
