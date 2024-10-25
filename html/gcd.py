def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

# Example usage
number1 = 56
number2 = 98
gcd = find_gcd(number1, number2)
print'The GCD of {0} and {1} is:'.format(number1,number2),gcd
