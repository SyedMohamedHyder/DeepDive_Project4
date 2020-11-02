# All imports go here


def get_gender_records(data, *, gender):
    yield from filter(lambda datum : datum.gender == gender, data)


# Things to be exported
__all__ = ['get_gender_records']