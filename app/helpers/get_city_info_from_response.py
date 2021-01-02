def get_city_info_from_response(response, day):
    city_info = {}
    city_info['id'] = response['id']
    city_info['name'] = response['name']
    city_info['state'] = response['state']
    city_info['country'] = response['country']
    data = response['data'][day]
    city_info['date'] = data['date']
    city_info['probability'] = data['rain']['probability']
    city_info['precipitation'] = data['rain']['precipitation']
    city_info['min_temp'] = data['temperature']['min']
    city_info['max_temp'] = data['temperature']['max']
    return city_info
