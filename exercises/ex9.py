# This function takes in a string
def vowel_counter(string):
    # Set a count variable to zero
    count = 0
    # Loop through the string
    for char in string:
        # If the character is in "aeiouAEIOU"
        if char in "aeiouAEIOU":
            # Increment the count variable
            count +=1
    # Return the count in an f string
    return f"Number of vowels: {count}"