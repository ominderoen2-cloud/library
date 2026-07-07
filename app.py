from database.database import create_member_table , create_books_table , create_borrow_books_table , create_users_table
from routes.routes import member_bp
import os
from flask import Flask
from flask_jwt_extended import JWTManager
app = Flask(__name__)
app.register_blueprint(member_bp)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)
@app.route("/")
def home():
    return {"status":"api running"}
create_member_table()
create_borrow_books_table()
create_books_table()
create_users_table()
port = int(os.getenv("PORT", 67))

app.run(
    host="0.0.0.0",
    port=port,
    debug=True
)

#library/app.py