from flask import Blueprint , request, jsonify
from services.services import create_member , list_members , update_member , remove_member , get_by_member_id, create_book, get_all_books , get_one_book , borrow_book , return_book,check_book_status, remove_book
from services.member_service import MemberService
from services.book_service import BookService
from services.borrow_service import Borrowbookservice
from services.return_services import Returnbookservice
from services.auth_service import AuthService 
from flask_jwt_extended import jwt_required
book_service = BookService()
member_service = MemberService()
borrow_service = Borrowbookservice()
return_service = Returnbookservice()
member_bp = Blueprint("member_bp" , __name__)
auth_service = AuthService()

@member_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    response, status = auth_service.login(data)

    return response, status
@member_bp.route("/register", methods=["POST"])
def register():
    response , status = auth_service.register(request.json)
    return jsonify(response) , status
@member_bp.route("/member", methods = ["POST"])
def create():
    response , status = member_service.create_member(request.json)
    return jsonify(response) , status
@member_bp.route("/member" , methods = ["GET"])
@jwt_required()
def list_all():
    response , status = member_service.list_members()
    return jsonify(response) , status
@member_bp.route("/member/<member_id>" , methods = ["DELETE"])
def delete(member_id):
    response , status = member_service.remove_member(member_id)
    return jsonify(response) , status
@member_bp.route("/member/<member_id>" , methods = ["PUT"])
def update(member_id):
    response , status = member_service.update_member(request.json , member_id)
    return jsonify(response) , status
@member_bp.route("/member/<member_id>" , methods = ["GET"])
def search_by_id(member_id):
    response , statius = member_service.get_by_member_id(member_id)
    return jsonify(response) , statius
@member_bp.route("/book" , methods = ["POST"])
def create_book_route():
    response , status = book_service.create_book(request.json)
    return jsonify(response), status
                 
@member_bp.route("/book/<book_id>" , methods = ["GET"])
def one_book(book_id):
    response , status = book_service.get_one_book(book_id)
    return jsonify(response) , status
@member_bp.route("/book" , methods = ["GET"])
def list_books():
    response , status = book_service.get_all_books()
    return jsonify(response) , status
@member_bp.route("/borrow" , methods = ["POST"])
def borrow_book_route():
    response , status = borrow_service.borrow_book(request.json)
    return jsonify(response) , status
@member_bp.route("/borrow/<borrow_id>/return" , methods = ["POST"])
def return_book_route(borrow_id):
    response , status = return_service.return_book(request.json, borrow_id)
    return jsonify(response) , status
@member_bp.route("/borrow/<book_id>" , methods = ["GET"] )
def book_status(book_id):
    response , status = book_service.check_book_status(book_id)
    return jsonify(response) , status
@member_bp.route("/book/<book_id>" , methods = ["DELETE"])
def delete_book_route(book_id):
    response , status = book_service.remove_book(book_id)
    return jsonify(response) , status
#library/routes/routes.py
