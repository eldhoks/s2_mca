number=raw_input("enter the numbers seperated by spaces:")
numbers=[int (num)for num in number.split()]

odd_numbers=[num for num in numbers if num%2 !=0]
print 'list of odd_numbers:', odd_numbers
