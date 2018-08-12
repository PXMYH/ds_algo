#!/usr/bin/env python

# 53. Maximum Subarray
# 
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

''' the following method has time complexity O(n^2)'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, list_sum = None, None
        list_len = len(nums)
        # print "list_len: " + str(list_len)
        for i in range (1, list_len+1):
          # print "i=" + str(i)
          for j in range (list_len - i + 1):
            # print "j=" + str(j)
            nums_slice = nums[j:j+i]
            list_sum = sum(nums_slice)
            # print "list_sum=" + str(list_sum)
            if list_sum > max_sum:
              max_sum = list_sum
        return max_sum

''' O(n) solution '''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
        return max_sum