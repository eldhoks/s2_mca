names=["alice","bob","charlie","david","eva","frank","grace"]

count_a=0
for name in names:
        count_a+=name.lower().count('a')
print("the letter 'a' occurs {0} times in the list of names.".format(count_a))

