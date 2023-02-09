# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
# You must also not convert the inputs to integers directly.

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# 

# Test Cases:
 
    # Example 1:

    # Input: 
    #     num1 = "11", num2 = "123"
    # Output: 
    #     "134"

    # Example 2:

    # Input: 
    #     num1 = "456", num2 = "77"
    # Output: 
    #     num1 = "456", num2 = "77"


def addStrings(num1, num2):
    if len(num1) >= 1 and len(num2) <= 10^4:
        sum_digits = []

        first_num_add = ''
        second_num_add = ''

        if len(num1) > len(num2):
            first_num_add, second_num_add = num1, num2
        else: 
            first_num_add, second_num_add = num2, num1

        first_num_add = first_num_add[::-1]
        second_num_add = second_num_add[::-1]

        carry = 0
        i = 0

        while i < len(first_num_add):
            if i < len(second_num_add):
                s = int(second_num_add[i]) + int(first_num_add[i]) + carry
            else:
                s = int(first_num_add[i]) + carry

            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0

            sum_digits.append(s)
            i += 1

        if carry:
            sum_digits.append(carry)

        return "".join(map(str, sum_digits[::-1]))

    # Solution Runtime: O(n)