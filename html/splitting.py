input_colors=raw_input("enter color names seperated by commas:")

color_list=[color.strip() for color in input_colors.split(',')]
#Display the first and last color
if input_colors: #check if the list is not empty
  first_color=color_list[0]
  last_color=color_list[-1]
  print'first color:',first_color
  print'last color:',last_color
else:
  print("no colors entered")
