# app/resources.py
from flask import Blueprint, request
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.models import vacancies

bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(bp)

parser = reqparse.RequestParser()
parser.add_argument("title", type=str, required=True, help="Title is required")
parser.add_argument("location", type=str, required=True, help="Location is required")
parser.add_argument("salary", type=int, required=True, help="Salary is required")

class VacancyResource(Resource):
    def get(self, vacancy_id):
        vacancy = next((v for v in vacancies if v["id"] == vacancy_id), None)
        if vacancy:
            return vacancy
        else:
            return {"message": "Vacancy not found"}, 404

    def put(self, vacancy_id):
        args = parser.parse_args()
        vacancy = next((v for v in vacancies if v["id"] == vacancy_id), None)
        if vacancy:
            vacancy.update(args)
            return vacancy
        else:
            return {"message": "Vacancy not found"}, 404

    def delete(self, vacancy_id):
        global vacancies
        vacancies = [v for v in vacancies if v["id"] != vacancy_id]
        return {"message": "Vacancy deleted successfully"}

class VacancyListResource(Resource):
    def get(self):
        return vacancies

    def post(self):
        args = parser.parse_args()
        new_vacancy = {
            "id": len(vacancies) + 1,
            "title": args["title"],
            "location": args["location"],
            "salary": args["salary"],
        }
        vacancies.append(new_vacancy)
        return new_vacancy, 201

class SecureVacancyResource(Resource):
    @jwt_required()
    def put(self, vacancy_id):
        current_user = get_jwt_identity()
        args = parser.parse_args()
        vacancy = next((v for v in vacancies if v["id"] == vacancy_id), None)
        if vacancy:
            vacancy.update(args)
            return vacancy
        else:
            return {"message": "Vacancy not found"}, 404

    @jwt_required()
    def delete(self, vacancy_id):
        current_user = get_jwt_identity()
        global vacancies
        vacancies = [v for v in vacancies if v["id"] != vacancy_id]
        return {"message": "Vacancy deleted successfully"}

api.add_resource(VacancyListResource, "/vacancies")
api.add_resource(VacancyResource, "/vacancies/<int:vacancy_id>")
api.add_resource(SecureVacancyResource, "/secure/vacancies/<int:vacancy_id>")