#!/usr/bin/env python3

# All imports go here
import csv
import os
from datetime import datetime
from collections import namedtuple

# Returns the first line (header) of a csv file as a list of strings.
def get_header(filename, *, delimiter=',', quotechar='"'):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter, quotechar=quotechar)
        return next(reader)

# Creates a namedtuple by making the filenameas name of the namedtuple class.
def create_namedtuple(filename, fields, *, to_be_replaced='.csv', replace_with=''):
    name = os.path.splitext(os.path.split(filename)[1])[0]
    return namedtuple(name, fields)

# Generator factory which yields the data lines by skipping line1.
def parse_data(filename, *, delimiter=',', quotechar='"'):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter, quotechar=quotechar)
        next(reader)
        yield from reader

# Converts data to the corresponding datatype.
def convert_datatype(zipped_data):
    make_date = lambda date, date_format='%Y-%m-%dT%H:%M:%SZ' : datetime.strptime(date, date_format)
    datatype_map = {
        'last_updated' : make_date,
        'created' : make_date,
        'model_year' : int
    }
    return (datatype_map.get(datatype, str)(data) for data, datatype in zipped_data)
