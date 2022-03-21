# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives
# become positives.
# You can assume that all values are integers. Do not mutate the input array/list.
def invert(lst):
    res_list = []
    for i in lst:
        res_list.append(-i)
    return res_list
