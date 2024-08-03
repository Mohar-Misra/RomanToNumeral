def romanToInt(s):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total + roman[s[-1]]


class Solution(object):
    pass


# Create an instance of the Solution class
solution = Solution()

# Input Roman numeral from the user
roman_numeral = input("Enter a Roman numeral: ")

# Convert the input to uppercase (to handle lowercase input)
roman_numeral = roman_numeral.upper()

# Calculate the numeral
result = romanToInt(roman_numeral)

# Print the result
print(f"The numeral is {result}")
