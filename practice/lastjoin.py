"""Joins words together and uses separators"""

# setup

# input
word_list = (input('Please enter words separated by a space. ')).split()

count = len(word_list)
if count == 1:
    word_string = str(word_list)
elif count == 2:
    word_string = ' and '.join(word_list)
else:
    # word_string.join(word_list[0:-1]
    #
    # temp = word_list[-1]
    # word_string = word_string + ', and ' + temp
    word_string = ', '.join(word_list[0:-1])
    word_string = word_string + ', and ' + word_list[-1]


# output
print(word_string)
