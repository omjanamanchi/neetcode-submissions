from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    result = 0
    for i in range(len(nums)):
        result+=nums[i]
    return result

def get_min(nums: List[int]) -> int:
    new_min = 1e10
    for i in range(len(nums)):
        if nums[i] < new_min:
            new_min = nums[i]
    return new_min

def get_max(nums: List[int]) -> int:
    new_max = 1e-10
    for i in range(len(nums)):
        if nums[i] > new_max:
            new_max = nums[i]
    return new_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
