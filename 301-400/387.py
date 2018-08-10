#!/usr/bin/env python

# Problem Description:
# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
# 
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

# Note: 
# This is not traditional algorithm of list iteration rather utilizing python specific feature OrderedDict
# Please be aware the performance is not up to standard
# The reason to put the algorithm here is just to think outside of the box and provide one more way to solve the problem

import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = collections.OrderedDict()
        s_list = list(s)
        for i in range (0, len(s_list)):
          if not str(s_list[i]) in s_dict:
            s_dict[str(s_list[i])] = 1
          else:
            s_dict[str(s_list[i])] += 1
        
        for k,v in s_dict.items():
          if v == 1:
            return s.index(k)
        
        return -1