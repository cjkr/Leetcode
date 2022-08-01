# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    # METHOD 1
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # METHOD 2
    check_dict = {}

    for i, n in enumerate(nums):
        if n in check_dict:
            return [i, check_dict[n]]
        else:
            check_dict[target - n] = i


print(twoSum(nums, target))
