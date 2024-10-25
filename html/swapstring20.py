def swap_and_merge(str1, str2):
    # Check if both strings have at least 2 characters
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings must have at least 2 characters."

    # Swap the characters at position 1
    new_str1 = str1[0] + str2[1] + str1[2:]
    new_str2 = str2[0] + str1[1] + str2[2:]

    # Merge the two strings with space
    result = new_str1 + " " + new_str2
    return result

# Example usage
string1 = "hello"
string2 = "world"
result = swap_and_merge(string1, string2)
print(result)
