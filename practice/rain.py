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

# Finds the common keys
# def dict_yearly_totals(d):



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

    winning_year = [yr15, yr16, yr14, yr13, yr12, yr11, yr10, yr09, yr08, yr07, yr06, yr05, yr04, yr03, yr02]

    print(winning_year)
    return winning_year # need to generate a if, elif statement to return a print of winning year


# output: prints out a the returns from transform
#
#
def main():
    filename = 'sunnyside.txt'

    lines = each_line_of_file(filename)
    lines_split = split_lines(lines)
    final_list = remove_junk(lines_split)
    dict_to_check = dict_dates(final_list)
    # rainy_day = most_rain(dict_to_check)
    # day_with_most_rain = 'The day that had the most rain was: ' + str(rainy_day)
    rainy_year = wet_year(dict_to_check)

    print(rainy_year)


if __name__ == '__main__':
    main()
main()