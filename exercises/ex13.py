# import pyfiglet

# result = pyfiglet.figlet_format("S a c o y a", font = "caligraphy" )
# print(result)

def frame_it(list):
    # print("*********")
    # for word in list:
    #     if len(word) == 5:
    #         print("*", word, "*")
    #     elif len(word) == 2:
    #         print("*", word, "  ", "*")
    #     else:
    #         print("*", word, "   ", "*")
    # print("*********")

    size = max(len(word) for word in list)
    print('*' * (size + 4))
    for word in list:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))