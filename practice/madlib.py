""" A simple mad lib exercise."""

# setup
print("Let's write some mad-libs!")
# input
print('Choose a noun: ')
noun = str(input())
print('Choose a adjective: ')
adj = str(input())
print('Choose anouther noun: ')
noun_two = str(input())

# transform/output
print('The ' + str(noun) + ' jumped over the ' + str(adj)
    + ' ' + str(noun_two) + '.')
# setup
print('That was fun! Lets try another.')

# input adjectives 2 - 9
adj_two = input('Adjective: ')
adj_three = input('Adjective: ')
adj_four = input('Adjective: ')
adj_five = input('Adjective: ')
adj_six = input('Adjective: ')
adj_seven = input('Adjective: ')
adj_eight = input('Adjective: ')
adj_nine = input('Adjective: ')
# input nouns 3 - 5
noun_three = input('Noun: ')
noun_four = input('Noun: ')
noun_five = input('Noun: ')
# input verbs 1 - 4
verb_one = input('Verb: ')
verb_two = input('Verb: ')
verb_three = input('Verb: ')
verb_four = input('Verb: ')
verb_five = input('Verb: ')


# transform/output
print('The most ' + str(adj_two) + ' thing in the world, I think, \n'
    + 'is the inability of the ' + str(noun_three) + ' mind to '
    + str(verb_one) + ' all its contents. \n'
    + 'We live on a ' + str(adj_three) + ' island of ' + str(adj_four) + '\n'
    + 'in the midst of black seas of infinity, and it was not meant that \n'
    + 'we should voyage far. The ' + str(noun_four) + ', each '
    + str(adj_five) + ' in its own direction, have hitherto \n'
    + str(verb_two) + ' us little; but some day the ' + str(verb_three) + '\n'
    + 'together of ' + str(adj_six) + ' ' + str(noun_four) + ' will open up such \n'
    + str(adj_seven) + ' vistas of reality, and of our ' + str(adj_eight)
    + ' position therein, \n that we shall either go ' + str(verb_four) + '\n'
    + 'from the revelation or flee from the deadly light into the peace and \n'
    + 'safety of a new ' + str(adj_nine) + ' ' + str(noun_five) + '.')
