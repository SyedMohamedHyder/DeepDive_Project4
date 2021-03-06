# All imports go here
import goal1.utils as utils

# Converts a csv file to an iterator which returns each line as a namedtuple.
def convert_to_iterator(filename):
    headers = utils.get_header(filename)
    data_tuple = utils.create_namedtuple(filename, headers)
    for data in utils.parse_data(filename):
        cleaned_data = utils.convert_datatype(zip(data, headers))
        yield data_tuple(*cleaned_data)

# Things to be exported

__all__ = ['convert_to_iterator']