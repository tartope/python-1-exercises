# This function takes a sentence/string
def count_words(string):
    # Create a counter variable and set to zero
    counter = 0
    # print(string.split())
    # Split the string into words, place in a list, and loop through each word
    for word in string.split():
        # if the word is True
        if word:
            # Increase the counter
            counter += 1
    # Return the counter in this f string
    return f"Number of Words: {counter}"

