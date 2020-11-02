# All imports go here
import os
import goal1.converter as converter

# Base directory of this module
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Files to be converted as an iterator
employment_file = os.path.join(base_dir, 'data', 'employment.csv')
personal_info_file = os.path.join(base_dir, 'data', 'personal_info.csv')
update_status_file = os.path.join(base_dir, 'data', 'update_status.csv')
vehicles_file = os.path.join(base_dir, 'data', 'vehicles.csv')

# Iterator of all the files.
employment_iterator = converter.convert_to_iterator(employment_file)
personal_info_iterator = converter.convert_to_iterator(personal_info_file)
update_status_iterator = converter.convert_to_iterator(update_status_file)
vehicles_iterator = converter.convert_to_iterator(vehicles_file)

# Checking the length of every iterator.
#print(sum(1 for _ in employment_iterator))
#print(sum(1 for _ in personal_info_iterator))
#print(sum(1 for _ in update_status_iterator))
#print(sum(1 for _ in vehicles_iterator))

# Things to be exported
__all__ = ['employment_file',
           'personal_info_file',
           'update_status_file',
           'vehicles_file',
           'employment_iterator',
           'personal_info_iterator',
           'update_status_iterator',
           'vehicles_iterator']