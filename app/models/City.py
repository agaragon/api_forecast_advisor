from app.helpers.get_city_info_from_response import get_city_info_from_response
from app.helpers.convert_from_date_string import convert_from_date_string

def create_city_model(db):
    class City(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        date = db.Column(db.Date, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        state = db.Column(db.String(100), nullable=False)
        country = db.Column(db.String(100), nullable=False)
        probability = db.Column(db.Float, nullable=False)
        precipitation = db.Column(db.Float, nullable=False)
        mintemp = db.Column(db.Float, nullable=False)
        maxtemp = db.Column(db.Float, nullable=False)
    db.create_all()
    return City


def create_city_instance(response, i, City):
    cityInfo = get_city_info_from_response(response, i)
    consultDate = convert_from_date_string(cityInfo['date'])
    city = City(id=cityInfo['id'],
                date=consultDate,
                name=cityInfo['name'],
                state=cityInfo['state'],
                country=cityInfo['country'],
                probability=cityInfo['probability'],
                precipitation=cityInfo['precipitation'],
                mintemp=cityInfo['min_temp'],
                maxtemp=cityInfo['max_temp'])
    return city
