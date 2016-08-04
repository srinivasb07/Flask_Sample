from flask import  Flask,request,jsonify
from flask_restful import Resource, Api
from sqlalchemy.exc import SQLAlchemyError
from json import dumps
from app import app, db
from app.models import Users, UsersSchema

api = Api(app)
schema = UsersSchema(strict=True)
# Users

#List all Users and Create single User
class Create_List_Users(Resource):

    def get(self):
        all_users = Users.query.all()
        results = schema.dump(all_users, many=True)
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
            user = Users(raw_dict['email'], raw_dict['password'], raw_dict['name'], raw_dict['active'])
            user.add(user)
            # Should not return password hash
            query = Users.query.get(user.id)
            results = schema.dump(query)
            return results, 201

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 403
            return resp

#Get, Update or Delete single User
class Get_Update_DeleteUser(Resource):

    def get(self, id):
        user_query = Users.query.get_or_404(id)
        result = schema.dump(user_query)
        return result

    def put(self, id):
        user = Users.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        try:
            for key, value in raw_dict.items():
                setattr(user, key, value)

            user.update()
            return self.get(id)

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

    def delete(self, id):
        user = Users.query.get_or_404(id)
        try:
            delete = user.delete(user)
            response = make_response()
            response.status_code = 204
            return response

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp


api.add_resource(Create_List_Users, '/User')
api.add_resource(Get_Update_DeleteUser, '/User/<int:id>')