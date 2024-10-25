#promt the user for a list of intergers.

input_values=raw_input("enter a list of integers seperated by spaces:")


#split the input string into a list of strings the convert into integres.

int_list=[int (num) for num in input_values.split()]

#replace values graeter than 100 with 'over'

modified_list=['over' if num>100 else num for num in int_list]
print("modified_list:",modified_list)
