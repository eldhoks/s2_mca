# Get input from the user
input_string =raw_input("Enter a string: ")

# Check if the string is not empty
if input_string:
    # Get the first character
    first_char = input_string[0]
    
    # Replace all occurrences of the first character with '$', except the first one
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    
    # Display the result
    print"Modified string:", modified_string
else:
    print("Empty string provided.")
