# In a string s of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) 
# of the group. In the above example, "xxxx" has the interval [3,6].

# A group is considered large if it has 3 or more characters.

# Return the intervals of every large group sorted in increasing order by start index.

# Constraints:

# 1 <= s.length <= 1000
# s contains lowercase English letters only.

# Test Cases:
 
    # Example 1:

    # Input: 
    #     s = "abbxxxxzzy"
    # Output: 
    #     [[3,6]]

    # Example 2:

    # Input: 
    #     s = "abc"
    # Output: 
    #     []

def largeGroupPositions(s):
        larger_same_character_groups = []
        i = 0
        for j in range(len(s) - 1):
            if j == len(s)-1 or s[j] != s[j + 1]:
                if j - (i + 1) >= 3:
                    larger_same_character_groups.append([i, j])
                i = j + 1
        
        return larger_same_character_groups

    # Solution Runtime: O(n)