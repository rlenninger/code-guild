"""Takes data from rain gauge at Sunnyside and prints a summary of the data: date with the most rain &
year with most rain.
"""
# setup:
FILENAME = 'sunnyside.txt'


def open_file_and_read_lines(filename):
    """Opens sunnyside.txt and reads it line by line."""
    with open(FILENAME, newline='') as f:
        lines = f.readlines()
    header_removed = lines[11:-1]
    return header_removed


def parse_relevant_lines_into_date_amount(lines):
    """Places list of lines into list of tuples containing date and daily total, skips dates with missing data.

    >>> parse_relevant_lines_into_date_amount(['01-JAN-9999 0 1 2 3 4', '02-JAN-9999 5 6 7 8 9', '03-JAN-9999 - - - -'])
    [('01-JAN-9999', 0), ('02-JAN-9999', 5)]
    """
    return [parse_line_into_date_amount(line) for line in lines if should_process_input_line(line)]


def should_process_input_line(line):
    """Skips lines with missing data.

    >>> should_process_input_line('02-JAN-9999 5 6 7 8 9')
    True
    >>> should_process_input_line('03-JAN-9999 - - - - -')
    False
    """
    return line.split()[1] != '-'


def parse_line_into_date_amount(line):
    """
    >>> parse_line_into_date_amount('01-JAN-9999 0 1 2 3 4')
    ('01-JAN-9999', 0)
    """
    date_amount_tuple = tuple(line.split()[0:2])
    date_amount_tuple_int = date_amount_tuple[0], int(date_amount_tuple[1])
    return date_amount_tuple_int


def create_dict_from_list_of_dates_and_rain(y):
    """Creates a dict from the list.

    >>> create_dict_from_list_of_dates_and_rain([('12-MAY-1999', 3)])
    {'12-MAY-1999': 3}
    """
    d = {key: value for (key, value) in y}
    return d


def most_rain(p):
    """Returns the key for max of dict daily totals.

    >>> most_rain([('10-DEC-1988', 1), ('14-JAN-1999', 10)])
    '14-JAN-1999'
    """
    dict_of_parsed_lines = create_dict_from_list_of_dates_and_rain(p)
    day_with_most_rain = max(dict_of_parsed_lines, key=dict_of_parsed_lines.get)
    return day_with_most_rain


def get_year_with_most_rain(parsed_lines):
    """Returns year with max amount of rain.

    >>> get_year_with_most_rain([('10-DEC-1988', 1), ('14-JAN-1999', 10), ('01-OCT-1988', 4), ('05-MAY-1999', 3)])
    '1999'
    """
    total_by_year_list = remove_day_month(parsed_lines)
    total_by_year_dict = create_year_dict(total_by_year_list)

    total_by_year_max = max(total_by_year_dict, key=total_by_year_dict.get)
    return total_by_year_max


def remove_day_month(parsed_lines):
    """Slices the list of dates into years

    >>> remove_day_month([('DEC-1999', 9)])
    [('1999', 9)]
    """

    list_of_years_and_rainfall = []
    for date, rain in parsed_lines:
        date_sliced = date[-4:]
        list_of_years_and_rainfall += [(date_sliced, rain)]
    return list_of_years_and_rainfall


def create_year_dict(list_of_year_and_rainfall):
    """Creates a dict from year list and sums rain value.

    >>> create_year_dict([('1999', 1), ('1999', 2)])
    {'1999': [3]}
    """
    year_and_rainfall_amount = {}
    for date_sliced, rain in list_of_year_and_rainfall:
        if date_sliced not in year_and_rainfall_amount:
            year_and_rainfall_amount[date_sliced] = []
        year_and_rainfall_amount[date_sliced] += [rain]
    total_by_year = dict(zip(year_and_rainfall_amount.keys(), [[sum(item)] for item in year_and_rainfall_amount.values()]))
    return total_by_year


def output(day_with_most_rain, total_by_year_max):
    """Combines output strings for program.

    >>> output('DEC_31-1999', '1922')
    The date that had the most rain was: DEC_31-1999
    1922 was the wettest year from this data sample.
    """
    output_one = 'The date that had the most rain was: ' + day_with_most_rain
    output_two = total_by_year_max + ' was the wettest year from this data sample.'
    output_three = output_one + '\n' + output_two
    print(output_three)


def main():
    """Handler to run the program."""
    read_file = open_file_and_read_lines(FILENAME)
    parsed_lines = parse_relevant_lines_into_date_amount(read_file)
    day_with_most_rain = most_rain(parsed_lines)
    year_with_most_rain = get_year_with_most_rain(parsed_lines)
    output_day_and_year = output(day_with_most_rain, year_with_most_rain)

if __name__ == '__main__':
    main()
