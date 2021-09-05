"""
CP1404/CP5632 Practical
Word dictionary
"""

user_sentence = input(">>> ").lower()  # ensuring lower case for consistency
while user_sentence != "":
    user_words = user_sentence.split()  # splitting the sentence using the auto split
    user_dict = {}
    for word in user_words:  # sort by keys looking for the same key already existing
        if not(word in user_dict):
            user_dict[word] = 1  # starts at 1
        else:
            user_dict[word] = user_dict[word] + 1  # using word as the key a a simple counter for the assigned value

    for word in sorted(user_dict):  # sorting by keys inside the for loop
        # add 2 to the key width to account for the space and semicolon added to the key in printing
        print("{0:{1}} {2}".format(word+" :", max(len(key) for key in user_dict.keys())+2, user_dict[word]))

    user_sentence = input(">>> ").lower()
