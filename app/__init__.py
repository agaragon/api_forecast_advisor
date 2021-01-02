from flask import Flask, request
from flask_restful import Api, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func
from app.helpers.convert_from_date_string import convert_from_date_string
from app.helpers.city_id_validator import city_id_validator
from app.helpers.analysis_request_validator import analysis_request_validator
from app.webservice import get_city_forecast
from app.models.City import create_city_model, create_city_instance
from datetime import date

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
City = create_city_model(db)

response_api_fields = {
    'id': fields.Integer,
    'date': fields.String,
    'name': fields.String,
    'state': fields.String,
    'country': fields.String,
    'probability': fields.Float,
    'precipitation': fields.Float,
    'mintemp': fields.Float,
    'maxtemp': fields.Float,
}

response_analysis_fields = {
    'city': fields.String,
    'average_precipitation': fields.Float
}


@app.route('/city', methods=['GET'])
@marshal_with(response_api_fields)
def getCity():
    if not city_id_validator(request):
        return
    id = request.args['id']
    queryResult = City.query.filter_by(id=id, date=date.today()).first()
    if queryResult:
        return queryResult
    response = get_city_forecast(id)
    if 'error' in response:
        return
    city = create_city_instance(response, 0, City)
    db.session.add(city)
    db.session.commit()
    return city


@app.route('/analysis', methods=['GET'])
@marshal_with(response_analysis_fields)
def analysis():
    if not analysis_request_validator(request):
        return
    initial_date = convert_from_date_string(request.args['initial_date'])
    final_date = convert_from_date_string(request.args['final_date'])
    average_precipitation = db.session.query(
        func.avg(City.precipitation)
    ).filter(
        City.date >= initial_date, City.date <= final_date).scalar()
    hottest_city = City.query.filter(
        City.date >= initial_date, City.date <= final_date).order_by(
            desc(City.maxtemp)
    ).first()
    return {'city': hottest_city.name,
            'average_precipitation': average_precipitation}

