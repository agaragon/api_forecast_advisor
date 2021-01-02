def city_id_validator(request):
    try:
        id = request.args['id']
    except KeyError:
        return
    try:
        id = int(id)
        return True
    except ValueError:
        return
