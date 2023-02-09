# Given a string s, find the length of the longest substring without repeating characters.

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# Test Cases:
 
    # Example 1:

    # Input: 
    #     s = "abcabcbb"
    # Output: 
    #     3, "abc"

    # Example 2:

    # Input: 
    #     s = "bbbbb"
    # Output: 
    #     1, "b"

    # Example 3:

    # Input: 
    #     s = "pwwkew"
    # Output: 
    #     3, ""wke

def lengthOfLongestSubstring(s):
    while len(s) >= 0 and len(s) <= 5 * 10^4:
        longest_substring = ''
        for i in range(len(s)):
            for j in range((i + 1), (len(s) - 1)):
                substring = set(s[i:j])
                if len(substring) > len(longest_substring):
                    longest_substring = substring
        return len(longest_substring)

    # Solution Runtime: O(n^3)