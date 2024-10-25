current_year= int(input("enter the current year:"))
final_year=int(input("enter the final year:"))

leap_year=[]

for year in range(current_year,final_year+1):
  if(year%4==0 and year%100!=0):
     leap_year.append(year)
print"leap years are:"
print leap_year
