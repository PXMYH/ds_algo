def is_palindrome(s):
    """
    method 1: brutal force
    loop through all possible combinations of substrings
    and check if the substring is a palindrome
    time complexity: O(n^3)
    space complexity: O(n)
    """

    def is_palindrome(s):
        # time complexity: O(n)
        # space complexity: O(n), need to allocate a new array to compare
        return True if s == s[::-1] else False

    if not s: return ""
    if len(s) == 1: return s

    max_length = float('-inf')
    for i in range(len(s)-1):
        for j in range(i+1, len(s)+1):
            if is_palindrome(s[i:j]):
                if j - i > max_length:
                    longest_palindrome, max_length = s[i:j], j - i

    return longest_palindrome
