# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Constraints:

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

# Test Cases:
 
    # Example 1:

    # Input: 
    #     nums = [2,7,11,15], target = 9
    # Output: 
    #     [0,1]

    # Example 2:

    # Input: 
    #     nums = [3,2,4], target = 6
    # Output: 
    #     [1,2]

    # Example 3:

    # Input: 
    #     nums = [3,3], target = 6
    # Output: 
    #     [0,1]

def twoSum(nums, target):
    if len(nums) >= 2 and len(nums) <= 10^4:
        target_sum_indices = []
        for i in range(len(nums) - 1):
            pair_sum = nums[i] + nums[i + 1]
            if pair_sum == target:
                target_sum_indices.append([i, i+1])
        return target_sum_indices.pop(0)
                
    # Solution Runtime: O(n)

# ---------------------------------

# Alternate Solution:

def twoSum(nums, target):
    num_pairs = {}
    for i, num in enumerate(nums):
        diff = target - nums[i]
        if diff in num_pairs:
            return [num_pairs[diff], i]
        else:
            num_pairs[num] = i
    return

    # Solution Runtime: O(n)