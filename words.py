def print_upper_words(list, must_start_with):
    """ This functions prints every sinngle word"""
    for word in list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
