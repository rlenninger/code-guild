"""Takes data from rain gauge at Sunnyside and prints a summary of the data: date with the most rain &
year with most rain.
"""
# setup:
filename = 'sunnyside.txt'


def each_line_of_file(filename):
    """Opens sunnyside.txt and reads it line by line."""
    with open(filename, newline='') as f:
        lines = f.readlines()

    return lines


def split_lines(lines):
    """Strips and splits the lines into lists."""
    listed_lines = [x.strip().split('\n') for x in lines]
    listed_lines_reduced = listed_lines[11:-1]
    line_list = []
    for listed_lines_split in listed_lines_reduced:
        line_list += [y.split() for y in listed_lines_split]

    return line_list


def remove_junk(line_list):
    """Cleans up the list and sets daily rain amount to an int.

    >>> remove_junk([['test', '1', '2', '3']])
    [['test', 1]]
    """
    temp_list = []
    for z in line_list:
        temp_list += [z[0:2]]
    temp_list2 = []
    for date, rain in temp_list:
        if rain != '-':
            int_rain = int(rain)
            temp_list2 += [[date, int_rain]]
    return temp_list2


def dict_dates(y):
    """Creates a dict from the list.

    >>> dict_dates([['test', 1]])
    {'test': 1}
    """
    d = {key: value for (key, value) in y}
    d = {str(k): int(v) for k, v in d.items()}
    return d


def most_rain(d):
    """Returns the key for max of dict daily totals.

    >>> most_rain({'test': 1})
    'test'
    """
    day_with_most_rain = max(d, key=d.get)
    return day_with_most_rain


def create_year_list(temp_list2):
    """Slices the list of dates into years

    >>> create_year_list([['Dec1999', 'Party over! OOPS! out of time']])
    [['1999', 'Party over! OOPS! out of time']]
    """
    temp_list3 = []
    for date, rain in temp_list2:
        date_sliced = date[-4:]
        temp_list3 += [[date_sliced, rain]]
    return temp_list3


def create_year_dict(temp_list3):
    """Creates a dict from year list and sums rain value.

    >>> create_year_dict([['1999', 1], ['1999', 2]])
    {'1999': [3]}
    """
    yearly_totals = {}
    for date_sliced, rain in temp_list3:
        if date_sliced not in yearly_totals:
            yearly_totals[date_sliced] = []
        yearly_totals[date_sliced] += [rain]
        total_by_year = dict(zip(yearly_totals.keys(), [[sum(item)] for item in yearly_totals.values()]))
    return total_by_year


def get_max_year(total_by_year):
    """Returns year with max amount of rain.

    >>> get_max_year({'1999':200, '1998':100})
    '1999'
    """
    total_by_year_max = max(total_by_year, key=total_by_year.get)
    return total_by_year_max


def output(day_with_most_rain, total_by_year_max):
    """Combines output strings for program."""
    output_one = 'The date that had the most rain was: ' + str(day_with_most_rain)
    output_two = str(total_by_year_max) + ' was the wettest year from this data sample.'
    output_three = str(output_one) + '\n' + output_two
    print(output_three)
    return output_three


def main():
    """Handler to run the program."""
    lines = each_line_of_file(filename)
    lines_split = split_lines(lines)
    final_list = remove_junk(lines_split)
    dict_to_check = dict_dates(final_list)
    rainy_day = most_rain(dict_to_check)
    wet_year_list = create_year_list(final_list)
    year_dict = create_year_dict(wet_year_list)
    max_year = get_max_year(year_dict)
    final_output = output(rainy_day, max_year)
    return final_output

if __name__ == '__main__':
    main()
