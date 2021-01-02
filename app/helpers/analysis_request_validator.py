from app.helpers.convert_from_date_string import convert_from_date_string

def analysis_request_validator(request):
    try:
        convert_from_date_string(request.args['initial_date'])
        convert_from_date_string(request.args['final_date'])
        return True
    except KeyError:
        return
    except ValueError:
        return
