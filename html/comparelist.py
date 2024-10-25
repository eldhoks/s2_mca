l1=[4,6,7,8]
l2=[10,3,4,1]
if len(l1)==len(l2):
 print"the list are of same length"
if sum(l1)==sum(l2):
 print"the list has same sum same values"
else:
 print("the list has different sum values")
if set(l1).intersection(l2):
 print("value repeats")
else:
 print("values does not repeat")
