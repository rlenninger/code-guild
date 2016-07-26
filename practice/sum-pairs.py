"""A function that goes through a list and finds all pairs of numbers that would add together to the sum.

 """

# setup: list of numbers and a sum to check

num_list = [1, 2,3]

# print('list of numbers is ' + str(num_list))
#
# # get a number from user to check against the num_list
#
# num_to_check = int(input('If you give me a number I can look for pairs that will equal it when summed. '))
#
# print('number to check is: ' + str(num_to_check))

# transform: this step will check the num_list for for pairs that equal the num_to_check when summed
# num_to_check = 5




# for num in list, list[0 - -1] + list[0 - -1] (mapping??)

# this needs to be: if [0] + [1] = num_to_check then do thing if [0] + [2] = num_to_check then do thing ect. should be automated

def compair(num_to_check):
    """checks if any pairs in num_list can be summed to equal num_to_check
    >>> compair(5)
    [1, -1]
    """
    output_pairs = [num for num in num_list if num_list[0:-1] + num_list[0:-1] == num_to_check]
    return output_pairs

compair(5)
# out_put_str = compair(num_to_check)

# print('this is where we want to see the list pairs.' + str(out_put_str))
