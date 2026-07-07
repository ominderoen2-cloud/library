from database.database import create_member_table , create_books_table , create_borrow_books_table , users , create_users_table
from routes.routes import member_bp
from models.user import User
import os
from flask import Flask
from flask_jwt_extended import JWTManager
app = Flask(__name__)
app.register_blueprint(member_bp)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)
users.append(
    User(
        username="roen",
        password="1234"
    )
)
@app.route("/")
def home():
    return {"status":"api running"}
create_member_table()
create_borrow_books_table()
create_books_table()
create_users_table()
if "__main__" == __name__:
    app.run(host ="0.0.0.0" , port = 67 , debug = True)

#library/app.py