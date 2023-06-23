def count_words():
    sentence = input("Enter sentence: ")
    counter = 0
    # print(sentence)
    for word in sentence.split():
        counter += 1
    print(f"Number of Words: {counter}")
    pass
