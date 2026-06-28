from database.database import create_member_table , create_books_table , create_borrow_books_table
from routes.routes import member_bp
from flask import Flask
app = Flask(__name__)
app.register_blueprint(member_bp)
@app.route("/")
def home():
    return {"status":"api running"}
create_member_table()
create_borrow_books_table()
create_books_table()
if "__main__" == __name__:
    app.run(host ="0.0.0.0" , port = 67 , debug = True)
#library/app.py