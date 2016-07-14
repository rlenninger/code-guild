"""
Prompts user for a ward in snake_case or CamelCase and converts it into the opposite case.
"""

# setup: import regex and get word from user
import re


def get_user_word():
    """Asks user for the word to be converted.
    """
    word_to_change = input('Please give me a word and I will convert it to snake_case or CamelCase. ')
    return word_to_change


def check_word_case(word_to_change):
    """Checks if word_to_change needs to be converted to snake or camel case.
    >>> check_word_case('snake_case')
    'SnakeCase'
     """
    if word_to_change.islower() == True: # convert to camel
        final_output = convert_to_camel(word_to_change)
    if word_to_change.islower() != True: # convert to snake
        final_output = convert_to_snake(word_to_change)
    return final_output

# transform: converts to CamelCase or snake_case


def convert_to_camel(snake_to_camel_word):
    """converts a word form snake_case to CamelCase
    >>> convert_to_camel('snake_case')
    'SnakeCase'
    """
    snake_split = snake_to_camel_word.split('_')
    snake_split = [element.capitalize() for element in snake_split]
    output = ''.join(snake_split)
    return output
# convert_to_snake()


def convert_to_snake(camel_to_snake):
    """converts a word from CamelCase to snake_case.
    >>> convert_to_snake('CamelCase')
    'camel_case'
    """
    camel_split = re.findall('[A-Z][a-z]*', camel_to_snake)
    camel_split = [element.lower() for element in camel_split]
    output = '_'.join(camel_split)
    return output

def main():
    ask_for_word = get_user_word()
    check_for_case = check_word_case(ask_for_word)
    print(check_for_case)

if __name__ == '__main__':
    main()

