"""Program checks to see if a credit card number is valid."""
# get a credit card number

def get_cc_number():
    """Asks user for a CC number."""
    user_cc_num = input('Please enter a credit card number to check. ')
    # user_cc_num = '4556737586899855'
    return user_cc_num

# math credit card number
def get_check_digit(user_cc_num):
    """"This generates the check digit
    >>> get_check_digit('12')
    '2'
    """
    return user_cc_num[-1]

def get_validation_digit(user_cc_num):
    """Retrives the validation digit.
    >>> get_validation_digit('4556737586899855')
    5
    """
    # 1. slice off last digit
    shortened_validation_digit = user_cc_num[:-1]

    # 2. reverse digits
    reversed_digit_list = reverse_digit_list(shortened_validation_digit)
    reversed_digits_as_ints = str_to_ints_in_list(reversed_digit_list)

    # 3. Multiply the odd reversed digits by two.
    multiplied_ints = multiply_even_index_ints(reversed_digits_as_ints)

    # 4. subtract nine from numbers > 9
    subtracted_ints = subtracting_large_ints(multiplied_ints)

    # 5. Sum all subtracted values.
    sum_values = sum(subtracted_ints)

    # 6. Take the 1s digit of that sum
    return str(sum_values % 10)

def str_to_ints_in_list(str_list):
    """Converts strings to ints in the list.
    >>> str_to_ints_in_list(['1', '2', '3'])
    [1, 2, 3]
    """
    int_list = [int(x) for x in str_list]
    return int_list

def multiply_even_index_ints(int_list):
    # Fix so to multiple odd in index rather than odd numbers
    """Fix so to multiple odd in index rather than odd numbers.
    >>> multiply_even_index_ints([1, 2, 3])
    [2, 2, 6]
    """
    return [x if i % 2 == 1 else x * 2 for i, x in enumerate(int_list)]
    # [x * 2 for i, x in enumerate(int_list) if is_odd(i)]

def is_odd(number):
    """More math for validation check.
    >>> is_odd(3)
    True
    """
    return (number % 2 == 1)


def subtracting_large_ints(int_list):
    """More math for validation check.
    >>> subtracting_large_ints([10, 2, 6])
    [1, 2, 6]
    """
    return [x - 9 if x > 9 else x for x in int_list]


def reverse_digit_list(digits):
    """Reverese digits for validation check.

    >>> reverse_digit_list("12345678")
    ['8', '7', '6', '5', '4', '3', '2', '1']
    """
    reversed_value = reversed(digits)
    return list(reversed_value)

def check_validation(check_digit, validation_digit):
    """Looks to see if check digit is equal to validation digit.
    >>> check_validation(1, 1(
    'Valid!'
    )
    """
    if check_digit == validation_digit:
        is_valid = True
    else:
        is_valid = False
    return is_valid

def generate_validation_statement(is_card_valid_bool):
    """Generates print statment for output."""
    if is_card_valid_bool == True:
        output_statement = 'Valid!'
    else:
        output_statement = 'Invalid!'
    return output_statement

# tell us if the CC is valid

def main():
    """Runs the program."""
    cc_num = get_cc_number()
    check_digit = get_check_digit(cc_num)
    validation_digit = get_validation_digit(cc_num)
    validitation_value = check_validation(check_digit, validation_digit)
    output_statement = generate_validation_statement(validitation_value)
    print(output_statement)
    return output_statement
main()
