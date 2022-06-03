"1. Two Sum"

class Solution:
    "Contains functions needed to compute the result."

    def twoSum(self, nums, target):
        "Returns indices of the two numbers such that they add up to target."
        history = {}
        for index in range(len(nums)):
            check = target - int(nums[index])
            if check in history:
                return [history[check], index]
            history[int(nums[index])] = index
