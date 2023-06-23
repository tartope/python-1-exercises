from exercises import ex1, ex2, ex3, ex4, ex5, ex9


def main():
    # print('ding dong')
    # ex1.ex1()
    # ex1.hello_world(3)
    # ex2.array_to_string([1,2,3])
    # ex3.add_numbers([1.0, 1.1, "1"])
    
    # sentence = input("Enter sentence: ")
    # num_words = ex4.count_words(sentence)
    # print(num_words)

    # ex5.replace_period(sentence, punctuation)
    # sentence = "Test.  This is a test.  Testing."
    # punctuation = "!"
    # sentence2 = ex5.replace_period(sentence, punctuation)
    # print(sentence2)

    # ex9.vowel_counter()
    sentence = input("Enter sentence: ")
    num_vowels = ex9.vowel_counter(sentence)
    print(num_vowels)

              




if __name__ == '__main__':
    main()
