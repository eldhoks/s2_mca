# Get input from the user
input_string =raw_input("Enter a string: ")

# Check if the string has at least two characters
if len(input_string) > 1:
    # Swap the first and last characters
    modified_string = input_string[-1] + input_string[1:-1] + input_string[0]
else:
    # If the string is too short, keep it as is
    modified_string = input_string

# Display the result
print("Modified string:", modified_string)
