# All imports go here
import itertools

def group_record(data, *, key):
    yield from itertools.groupby(data, key=key)

__all__ = ['group_record']