import random
list1 = ['abcd sdasdsn das das','bcdefsdf dfjds fksdjf ','c sdfdsfsd','d dsds ','b','c','d','x','e','z']
print(list1)
random.shuffle(list1)
print(list1)
	
print((int)(0.9*len(list1)))
list2 = list1[:(int)(0.9*len(list1))]
list3 = list1[(int)(0.9*len(list1)):]
print(list2)
print(list3)
