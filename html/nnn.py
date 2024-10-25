n = input("Enter an integer n: ")

# Compute nn and nnn
nn = n * 2   # This creates the string 'nn'
nnn = n * 3  # This creates the string 'nnn'

# Convert the strings to integers and compute the result
result = int(n) + int(nn) + int(nnn)

# Display the result
print("The result of n + nn + nnn is:", result)
