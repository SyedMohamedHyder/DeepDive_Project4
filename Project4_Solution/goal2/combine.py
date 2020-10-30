# All imports go here
import goal1
from collections import namedtuple

# Generator function which yields the combined data of all the files in a single namedtuple
def get_full_data(*files):
    file_iters = (goal1.convert_to_iterator(file) for file in files)
    zipped_iters = zip(*file_iters)
    first_data_row = next(zipped_iters)
    first_data_row_dict = { key:value for data in first_data_row for key, value in data._asdict().items()}
    fields = first_data_row_dict.keys()
    Full_data = namedtuple('Full_Data', fields)
    yield Full_data(**first_data_row_dict)
    for data_row in zipped_iters:
        yield Full_data(**{key:value for data in first_data_row for key, value in data._asdict().items()})

# Uncomment the below stuff to see how the sample data looks like.
print(next(get_full_data(goal1.employment_file,
                         goal1.personal_info_file,
                         goal1.update_status_file,
                         goal1.vehicles_file)))

# Things to be exported
__all__ = ['get_full_data']