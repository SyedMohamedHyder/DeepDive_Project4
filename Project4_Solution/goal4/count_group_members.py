# All imports go here
import itertools

# Yields the key and number of members in the corresponding gruop as a tuple
def no_of_members(groups):
    for key, group in groups:
        yield (key, sum(1 for _ in group))

def get_largest_group(groups):
    member_count = no_of_members(groups)
    sorted_members = sorted(member_count, key=lambda group : group[1], reverse=True)
    largest_count = sorted_members[0][1]
    return [(key, count) for key, count in sorted_members if count==largest_count]

__all__ = ['no_of_members', 'get_largest_group']