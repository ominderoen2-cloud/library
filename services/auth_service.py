from database.database import add_user, get_user
from database.database import get_user
from flask_jwt_extended import create_access_token
from models.user import User
import bcrypt


class AuthService:
    def hash_password(self ,password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)

    def register(self, data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"message": "missing fields"}, 400

        user = get_user(username)

        if user is not None:
            return {"message": "username already exists"}, 409
        hashed_password = self.hash_password(password.decode())
        
        add_user(username, hashed_password)

        return {"message": "successfully registered"}, 201
    def login(self , data ):
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return {"message": "missing fields"}, 400
        user = get_user(username)

        if user is None:
          return {"message": "Invalid credentials"}, 401

        stored_password = user["password"]

        if not bcrypt.checkpw(
            password.encode(),
            stored_password.encode()):
              return {"message": "Invalid credentials"}, 401

        token = create_access_token(identity=username)

        return {"access_token": token}, 200
        

        
    

    