#!/usr/bin/env python3

#Griffin Pundt
#NSSA221-01
#Script 1 Assignment
import os
from time import sleep
import subprocess


#This function gets the default gateway of the linux device
def get_gateway_address():
	output =  os.system('ip route show > output.txt')
	file = open('output.txt', 'r')
	output_string = file.read()
	split_string = output_string.split(" ")
	default_gateway = split_string[2]
	#print(default_gateway)
	os.system('rm output.txt')
	return default_gateway

#the ping function will ping whatever address is passed in
def ping(address):
	os.system("clear")
	print("Pinging to ", address, "\n")
	sleep(1)
	online  = os.system("ping -w 3 " + address)
	print("\n\n")
	if(online == 0):
		print("Ping to ", address, " was successful!")
	else:
		print("Ping to ", address, " was unsucessful!")

def main():
	#infinite loop to allow user to continue prompting
	sentinel = True
	while(sentinel):
		os.system("clear")
		print('*' * 54)
		print("************** PING TEST TROUBLESHOOTER **************")
		print("*" * 54, "\n\nEnter Selection\n")
		print("\t1 - Test connectivity to your gateway.\n")
		print("\t2 - Test for remote connectivity.\n")
		print("\t3 - Test for DNS resolution.\n")
		print("\t4 - Display gateway IP Address.\n\n")

		#different input will result in different function
		user_input = input("Please enter a number (1-4) or 'Q/q' to quit the program. ")
		if(user_input == "q" or user_input == "Q"):
			#quits program
			os.system("clear")
			print("Thank you for your time!\nHave a wondeful day!")
			sleep(3)
			os.system("clear")
			sentinel = False
		elif(user_input == '1'):
			#pings gateway
			os.system("clear")
			ping(get_gateway_address())
			sleep(4)
		elif(user_input == '2'):
			#pings remote address
			os.system("clear")
			ping('129.21.3.17')
			sleep(4)
		elif(user_input == '3'):
			#pings remote DNS
			os.system("clear")
			ping('www.google.com')
			sleep(4)
		elif(user_input == '4'):
			#shows default gateway
			os.system("clear")
			print("Your Default Gateway IP address is: ", get_gateway_address(), "!")
			sleep(4)
		else:
			#If user inputs someting stupid, program doesnt crash
			os.system("clear")
			print("*" * 37, "\n")
			print("*********** INVALID INPUT ***********\n")
			print("*" * 37, "\n\n")
			print("Please enter a number (1-4) or 'Q/q' to quit.")
			sleep(4)


main()
