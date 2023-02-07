# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Test Cases:
 
    # Example 1:

    # Input: 
    #     s = "anagram", t = "nagaram"
    # Output: 
    #     true

    # Example 2:

    # Input: 
    #     s = "rat", t = "car"
    # Output: 
    #     false


def isAnagram(s, t):
    while len(s) >= 1 and len(t) <= 5 * 10^4:
        letter_count_s = {}
        letter_count_t = {}
        for letter in s:
            if letter in letter_count_s:
                letter_count_s[letter] += 1
            else:
                letter_count_s[letter] = 1
        for letter in t:
            if letter in letter_count_t:
                letter_count_t[letter] += 1
            else:
                letter_count_t[letter] = 1
        if letter_count_s == letter_count_t:
            return True
        else:
            return False

    # Solution Runtime: O(n^3)

    # Alternative Single-Line Solution:
        # return sorted(s.strip()) == sorted(t.strip())