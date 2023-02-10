# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Constraints:

# The given address is a valid IPv4 address.

# Test Cases:
 
    # Example 1:

    # Input: 
    #     address = "1.1.1.1"
    # Output: 
    #     "1[.]1[.]1[.]1"

    # Example 2:

    # Input: 
    #     address = "255.100.50.0"
    # Output: 
    #     "255[.]100[.]50[.]0"


def defangIPaddr(address):
    defanged_ip_address_characters = []
    for character in address:
        if character == '.':
            defanged_ip_address_characters.append('[.]')
        else:
            defanged_ip_address_characters.append(character)
    return ''.join(defanged_ip_address_characters)

    # Solution Runtime: O(n^2)

# ---------------------------------

# Alternative Solution:
def defangIPaddr(address):
    defanged_ip_address = address.replace(".","[.]")
    return defanged_ip_address

    # Solution Runtime: O(n)