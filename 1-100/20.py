#!/usr/bin/env python

# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2 != 0:
            print "length is odd"
            return False
        else:
            stack = []

            mapping = {")": "(", "}": "{", "]": "["}

            for char in s:

                if char in mapping:

                    top_element = stack.pop() if stack else '#'

                    if mapping[char] != top_element:
                        return False
                else:
                    stack.append(char)

            return not stack