from json import loads


def validate_json(*args_dec):
    def true_decorator(decorated_fun):
        def check_json(str_json):
            dict_json = loads(str_json)

            for key in dict_json.keys():
                if key not in args_dec:
                    raise ValueError
            return decorated_fun(str_json)

        return check_json

    return true_decorator


@validate_json('first_name', 'last_name')
def process_json(json_data):
    return len(json_data)


result = process_json('{"first_name": "James", "last_name": "Bond"}')
assert result == 44

process_json('{"first_name": "James", "age": 45}')
# ValueError

process_json('{"first_name": "James", "last_name": "Bond", "age": 45}')
# ValueError
