"""Asks user for a single word and converts it into pig latin"""

# setup
VOWELS = ['a', 'e', 'i', 'o', 'u']

# input

# word_to_translate = list(input('Please type a single word to translate: '))
word_to_translate = input('Please give me a word to translate into pig latin: ')
word_to_translate_lower = word_to_translate.lower()
word_to_translate_list = word_to_translate_lower.strip()

# transform

if word_to_translate_list[0] in VOWELS:
    translated_word = '' .join(word_to_translate_list) + 'yay'

else:
    translated_word = '' .join(word_to_translate_list[1:-1]) + 'ay' + '' .join(word_to_translate_list[0])

# output
print('The pig latin version will be: ' + translated_word)