# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
# Given:
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
unique_list = list(set(sample_list))
result_tuple = tuple(unique_list)
min_number = min(result_tuple)
max_number = max(result_tuple)

print(unique_list)
print(result_tuple)
print(min_number)
print(max_number)

# Expected output:

# [87, 45, 41, 65, 94, 99]