# Given a string s, return the longest palindromic substring in s.

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Test Cases:
 
    # Example 1:

    # Input: 
    #     s = "babad"
    # Output: 
    #     "bab"

    # Example 2:

    # Input: 
    #     s = "cbbd"
    # Output: 
    #     "bb"


def longestPalindrome(s):    
    while len(s) >= 1 and len(s) <= 1000:
        longest_palindrome = ''
        string_length = len(s)
        for i in range(string_length):
            for j in range((i + 1), (string_length + 1)):
                palindrome = s[i:j]
                if palindrome == palindrome[::-1]:
                    if len(palindrome) > len(longest_palindrome):
                        longest_palindrome = palindrome
        return longest_palindrome

    # Solution Runtime: O(n^3)
