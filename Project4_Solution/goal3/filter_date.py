# All imports go here
import goal1
import goal2
from datetime import datetime

# Generator factory which returns all the unstale records of files as an iterator.
def get_unstale_records(*files, last_stale_date=datetime(2017, 3, 1)):
    combined_data = goal2.get_full_data(*files)
    yield from filter(lambda data : data.last_updated >= last_stale_date, combined_data)

# Uncomment the following to see the output.
# records = get_unstale_records(goal1.employment_file,
#                              goal1.personal_info_file,
#                              goal1.update_status_file,
#                              goal1.vehicles_file)

# print(sum(1 for _ in records))

# Things to be exported

__all__ = ['get_unstale_records']
