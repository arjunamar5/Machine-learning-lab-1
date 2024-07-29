def highest_occurring_char(input_string):
    # Remove spaces and convert to lowercase for uniformity
    input_string = input_string.replace(" ", "").lower()

    # Create a dictionary to count occurrences of each character
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the character with the highest occurrence
    highest_char = None
    highest_count = 0

    for char, count in char_count.items():
        if count > highest_count:
            highest_count = count
            highest_char = char

    return highest_char, highest_count


# Example usage
input_string = input("Enter a string: ")
char, count = highest_occurring_char(input_string)
if char:
    print(f"The highest occurring character is '{char}' with a count of {count}.")
else:
    print("No characters to count.")
