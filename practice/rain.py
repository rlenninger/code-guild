"""Takes data from rain guage at sunnyside and prints a summary of the data: date with the most rain &
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
    """Cleans up the list and sets daily rain amount to an int."""
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
    """Creates a dict from the list."""
    d = {key: value for (key, value) in y}
    d = {str(k): int(v) for k, v in d.items()}
    return d


def most_rain(d):
    """Returns the key for max of dict daily totals."""
    day_with_most_rain = max(d, key=d.get)
    return day_with_most_rain


def wet_year(d):
    """Converts dict into lists of yearly rain fall totals & finds the year with most rainfall."""

    yr16 = [value for key, value in d.items() if key.endswith('16')]
    yr16 = sum(yr16)
    yr15 = [value for key, value in d.items() if key.endswith('15')]
    yr15 = sum(yr15)
    yr14 = [value for key, value in d.items() if key.endswith('14')]
    yr14 = sum(yr14)
    yr13 = [value for key, value in d.items() if key.endswith('13')]
    yr13 = sum(yr13)
    yr12 = [value for key, value in d.items() if key.endswith('12')]
    yr12 = sum(yr12)
    yr11 = [value for key, value in d.items() if key.endswith('11')]
    yr11 = sum(yr11)
    yr10 = [value for key, value in d.items() if key.endswith('10')]
    yr10 = sum(yr10)
    yr09 = [value for key, value in d.items() if key.endswith('09')]
    yr09 = sum(yr09)
    yr08 = [value for key, value in d.items() if key.endswith('08')]
    yr08 = sum(yr08)
    yr07 = [value for key, value in d.items() if key.endswith('07')]
    yr07 = sum(yr07)
    yr06 = [value for key, value in d.items() if key.endswith('06')]
    yr06 = sum(yr06)
    yr05 = [value for key, value in d.items() if key.endswith('05')]
    yr05 = sum(yr05)
    yr04 = [value for key, value in d.items() if key.endswith('04')]
    yr04 = sum(yr04)
    yr03 = [value for key, value in d.items() if key.endswith('03')]
    yr03 = sum(yr03)
    yr02 = [value for key, value in d.items() if key.endswith('02')]
    yr02 = sum(yr02)

    winning_year = max([yr15, yr16, yr14, yr13, yr12, yr11, yr10, yr09, yr08, yr07, yr06, yr05, yr04, yr03, yr02])

    if winning_year == yr16:
        winning_year_str = '2016 had ' + str(yr16)
    elif winning_year == yr15:
        winning_year_str = '2015 had ' + str(yr15)
    elif winning_year == yr14:
        winning_year_str = '2014 had ' + str(yr14)
    elif winning_year == yr13:
        winning_year_str = '2013 had ' + str(yr13)
    elif winning_year == yr12:
        winning_year_str = '2012 had ' + str(yr12)
    elif winning_year == yr11:
        winning_year_str = '2011 had ' + str(yr11)
    elif winning_year == yr10:
        winning_year_str = '2010 had ' + str(yr10)
    elif winning_year == yr09:
        winning_year_str = '2009 had ' + str(yr09)
    elif winning_year == yr08:
        winning_year_str = '2008 had ' + str(yr08)
    elif winning_year == yr07:
        winning_year_str = '2007 had ' + str(yr07)
    elif winning_year == yr06:
        winning_year_str = '2006 had ' + str(yr06)
    elif winning_year == yr05:
        winning_year_str = '2005 had ' + str(yr05)
    elif winning_year == yr04:
        winning_year_str = '2004 had ' + str(yr04)
    elif winning_year == yr03:
        winning_year_str = '2003 had ' + str(yr03)
    elif winning_year == yr02:
        winning_year_str = '2002 had ' + str(yr02)
    return winning_year_str


def output(day_with_most_rain, winning_year_str):
    """Combines output strings for program."""
    output_one = 'The date that had the most rain was: ' + str(day_with_most_rain)
    output_two = str(winning_year_str) + ' inches of rain. Wow! That is a lot of rain!'
    output_three = str(output_one) + '\n' + output_two
    return output_three


def main():
    """Handler to run the program."""
    lines = each_line_of_file(filename)
    lines_split = split_lines(lines)
    final_list = remove_junk(lines_split)
    dict_to_check = dict_dates(final_list)
    rainy_day = most_rain(dict_to_check)
    rainy_year = wet_year(dict_to_check)
    final_output = output(rainy_day, rainy_year)
    print(final_output)
    return final_output

if __name__ == '__main__':
    main()
