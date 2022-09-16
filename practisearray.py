def test_duplicate(array_nums):

    nums_set = set(array_nums)

    return len(array_nums) != len(nums_set)

print(test_duplicate([2,3,4,5,7,9]))
print(test_duplicate([2,3,4,5,7,9,9]))
print(test_duplicate([2,2,3,3,4,4,5,5,7,7,9]))