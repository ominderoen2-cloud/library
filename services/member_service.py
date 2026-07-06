from validators.validators import validate_member_data
from database.database import (
    add_member,
    get_all_members,
    update_member_data,
    delete_member,
    connect_db
)

class MemberService:

    def create_member(self, data):
        clean_data, error, status = validate_member_data(data)
        if error:
            return error, status

        success = add_member(
            clean_data["member_id"],
            clean_data["name"]
        )

        if not success:
            return {"message": "member not registered"}, 409

        return {"message": "member successfully registered"}, 201

    def list_members(self):
        return get_all_members(), 200

    def remove_member(self, member_id):
        success = delete_member(member_id)

        if not success:
            return {"message": "user not found"}, 404

        return {"message": "successfully deleted"}, 200

    def update_member(self, data, member_id):
        clean_data, error, status = validate_member_data(
            data,
            require_id=False
        )

        if error:
            return error, status

        success = update_member_data(
            clean_data["name"],
            member_id
        )

        if not success:
            return {"message": "member not updated"}, 400

        return {"message": "member successfully updated"}, 200

    def get_by_member_id(self, member_id):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT member_id, name FROM members WHERE member_id = %s",
            (member_id,)
        )

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return {"message": "member not found"}, 404

        return {
            "member_id": row[0],
            "name": row[1]
        }, 200
