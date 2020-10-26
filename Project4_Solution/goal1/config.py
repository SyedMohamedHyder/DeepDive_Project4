#!/usr/bin/env python3

# All imports go here
import converter

# Files to be converted as an iterator
employment_file = "data/employment.csv"
personal_info_file = "data/personal_info.csv"
update_status_file = "data/update_status.csv"
vehicles_file = "data/vehicles.csv"

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
