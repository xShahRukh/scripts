#!/usr/bin/python

import random
import string
import requests

char_set = string.ascii_lowercase + string.digits
t=input("Enter loop \n")
count = 1
while t > 0:
	email = ''.join(random.sample(char_set*5, 12))+'@gmail.com'
	#url = 'http://www.limeroad.com/confirm_signup.json?email='+email
	#r = requests.post(url, allow_redirects=True)
	print "\n\nCount : ",count,"\nEmail : ",email,"\n"
	#print r.content
	count = count + 1
	t= t-1
