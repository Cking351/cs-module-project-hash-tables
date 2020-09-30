# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# """"
# loop through an array with multiple sub arrays
# find the smallest value in every sub array
# add the values together and return it
#
# """"

# def add_smallest_values(arr):
#     count = 0
#     for element in arr:
#         element.sort()
#         smallest_nums = element[0]
#         count += smallest_nums
#     print(count)

def add_smallest_values(arr):
    total = 0
    for element in arr:
        total += min(element)
    return total


# This would have been the better way to do it.

test = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

print(add_smallest_values(test))
