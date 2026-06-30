from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    ans = -1
    for index, value in enumerate(nums):
        if value == 7:
            ans = index
            break
    return ans


def get_dist_between_sevens(nums: List[int]) -> int:
    first, second = 0,0
    count = 0
    for index, value in enumerate(nums):
        if value == 7 and count < 2:
            if count == 0:
                first = index
            elif count == 1:
                second = index
            count+=1
        if count >= 2:
            break
    return second - first


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
