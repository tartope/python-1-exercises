# This function takes 2 strings (a sentence, a punctuation)
def replace_period(string, punctuation):
    # Change the string to a list and assign to a variable
    new_list = list(string)
    #  Loop through the list to access the element and index
    for i in range(len(new_list)):
        # If the element is equal to a "."
        if new_list[i] == ".":
            # Reassign the punctuation to the element
            new_list[i] = punctuation
    # Return the new list joined as a sentence
    return "".join(new_list)

