"""Asks user for a single word and converts it into pig latin"""

# setup
VOWELS = ['a', 'e', 'i', 'o', 'u']

def word_to_translate_from_user():
    """Asks user for a word, converts to lower case, removes puncuation
    and converts to a list.
    """
    word_to_translate = input('Please give me a word to translate into pig latin: ')
    word_to_translate_lower = word_to_translate.lower()
    word_to_translate_strip = word_to_translate_lower.strip('.?!')
    word_to_translate_list = list(word_to_translate_strip)
    return word_to_translate_list


def pig_latin_translator(word_to_translate_list):
    """Takes return from, word_to_translate_from_user and
    translates to pig latin.
    """
    if word_to_translate_list[0] in VOWELS:
        translated_word = '' .join(word_to_translate_list) + 'yay'
    else:
        translated_word = '' .join(word_to_translate_list[1:]) + '' .join(word_to_translate_list[0]) + 'ay'
    return translated_word

def main():
    """Runs word_to_translate_from_user function, passes to
    pig_latin_translator and prints output.
    """
    given_word = word_to_translate_from_user()
    output_text = pig_latin_translator(given_word)
    output = str(output_text)
    print('The pig latin version will be: ' + output)
    return output

main()
