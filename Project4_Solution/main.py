# All imports go here
import goal1
import goal2
import goal3
import goal4

# Combining all the iterators using the goal2 package.
combined_data = goal2.get_full_data(goal1.employment_file, goal1.personal_info_file,
                                    goal1.update_status_file, goal1.vehicles_file)

# All the unstale records of combined data
unstale_records = goal3.get_unstale_records(goal1.employment_file, goal1.personal_info_file,
                                            goal1.update_status_file, goal1.vehicles_file)

# Sorting the unstale records based on the vehicle_make
sorted_unstale_records =sorted(unstale_records, key=lambda record : record.vehicle_make)

# Getting gender wise records
male_records = goal4.get_gender_records(sorted_unstale_records, gender='Male')
female_records = goal4.get_gender_records(sorted_unstale_records, gender='Female')

# Getting the records grouped based on the vehicle make
male_groupped_records = goal4.group_record(male_records, key=lambda record : record.vehicle_make)
female_groupped_records = goal4.group_record(female_records, key=lambda record : record.vehicle_make)

# Getting the make, count as tuples for each gender
#male_make_count = goal4.no_of_members(male_groupped_records)
#female_make_count = goal4.no_of_members(female_groupped_records)

# Getting the largest make for each gender
print(goal4.get_largest_group(male_groupped_records))
print(goal4.get_largest_group(female_groupped_records))
