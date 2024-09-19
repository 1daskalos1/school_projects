'''
define a function to take in two parameters: x (a number of base 10)
and b_y the base you wish to convert x to
'''


def decimal_to_base(x, b_y):
    base_num = []  #create a list to store our results
    while x > 0:  #while the current number is nonzero
        base_num.append(x % b_y)  #add the remainder of our number/base to our list
        x = x // b_y  # perform integer division and replace x by the new value
    base_num.reverse()  #reverse the list, since the desired number is actually the reverse of this process
    string_list = map(str, base_num)  #Convert our list base_num to strings so that we can then concatenate
    result = ''.join(string_list)  #Concatenate the list
    return result  #Return the concatenated result


'''
define a function to take in two parameters: x (a number)
and b_x the base of this number, the expansion gives us a number in the familiar base 10
'''


def expansion_of_number(x, b_x):
    number_array = [int(i) for i in str(x)]  #create an array of int which converts all elements i to int
    reversed_array = list(reversed(number_array))  #reverse the order of the array
    expansion = sum(v * (b_x ** s) for s, v in enumerate(reversed_array))
    '''
    The expansion first enumerates reversed array providing the ith value with its position in the array
    So for each element in reversed_array, you get its position (s) and its value (v).
    '''
    return expansion


x = int(input("Enter a number: "))
b_x = int(input("What base is this number from: "))
b_y = int(input("What base would you like this number to be converted to: "))

# Convert the number to the desired base
if b_x == 10:
    converted_number = decimal_to_base(x, b_y)
else:
    if b_y == 10:
        converted_number = expansion_of_number(x, b_x)
    else:
        # First convert to decimal
        decimal_number = expansion_of_number(x, b_x)
        # Then convert from decimal to the desired base
        converted_number = decimal_to_base(decimal_number, b_y)

print(f"The representation of {x} in base {b_y} is {converted_number}")