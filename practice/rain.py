"""Takes data from rain guage at sunnyside and prints a summary of the data: date with the most rain &
year with most rain.
"""
# setup:
import statistics



# input: reads the text file


def each_line_of_file(filename):
    with open('sunnyside.txt', newline='') as f:
        lines = f.readlines()
        lines = [lines.replace('-', '0') for lines in lines]
    return lines

# print(each_line_of_file('sunnysideeez.txt'))


def split_lines(lines):
    listed_lines = [x.strip().split('\n') for x in lines]
    listed_lines_reduced = listed_lines[11:-1]
    line_list = []
    for listed_lines_split in listed_lines_reduced:
        line_list += [y.split() for y in listed_lines_split] # everything to here works properly

    return line_list


# reduce list of lists down to only items in position 0 and 1

def remove_junk(line_list):
    usable_list = []
    for z in line_list:
        usable_list += [z[0:2]]

    return usable_list    # everything works to this point


# create dict of {date:rainfall}


def dict_dates(y): # creates the dict and converts the value to an int
    d = {key: value for (key, value) in y}
    d = {str(k): int(v) for k, v in d.items()}
    return d

def most_rain(d): # gives result for day with the most rain, still need to make it look pretty
    z = max(zip(d.values(), d.keys()))
    return z


def wet_year(d): # seperates the dict into lists and averages baseed on year, 2002 - 2016


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




    return winning_year_str + ' inches of rain. Wow! Thats a lot of rain!'


# output: prints out a the returns from transform
#
#
def main():
    filename = 'sunnyside.txt'

    lines = each_line_of_file(filename)
    lines_split = split_lines(lines)
    final_list = remove_junk(lines_split)
    dict_to_check = dict_dates(final_list)
    rainy_day = most_rain(dict_to_check)
    day_with_most_rain = 'The day that had the most rain was: ' + str(rainy_day)
    rainy_year = wet_year(dict_to_check)

    print(day_with_most_rain)
    print(rainy_year)


if __name__ == '__main__':
    main()
