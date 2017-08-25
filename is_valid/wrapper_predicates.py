import json


def is_transformed(transform, predicate, *args, exceptions=[
    Exception
], msg='data can\'t be transformed', **kwargs):
    def is_valid(data, explain=False):
        try:
            data = transform(data, *args, **kwargs)
        except Exception as e:
            if not any(isinstance(e, exc) for exc in exceptions):
                raise e
            return (False, msg) if explain else False
        return predicate(data, explain=explain)
    return is_valid


def is_json(predicate, *args, **kwargs):
    return is_transformed(json.loads, predicate, *args, exceptions=[
        json.JSONDecodeError
    ], msg='data is not valid json', **kwargs)
