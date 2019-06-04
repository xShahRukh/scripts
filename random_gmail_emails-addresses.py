#!/usr/bin/python

import random
import string

char_set = string.ascii_lowercase + string.digits
t=input("Enter loop \n")
count = 1
while t > 0:
	email = ''.join(random.sample(char_set*5, 12))+'@gmail.com'
	print "\n\nCount : ",count,"\nEmail : ",email,"\n"
	count = count + 1
	t= t-1
