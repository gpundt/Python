#!/usr/bin/env python3

#NAME: Griffin Pundt
#CLASS: NSSA221
#ASSIGNEMNT: Script04

import os
from geoip import geolite2
import re

#First we iterate through every line in the syslog
#Find each entry where there is a failed login attempt
#Track the IP address of the attacker's device
#keep track of the number of times that IP tries to log in
#use geolite2 to locate country of origin
#print to standard output, make it look nice
def main():
	os.system("date > date.txt")
	with open("date.txt") as file:
		date = file.readline().strip()
	os.system("rm date.txt | clear")
	print("Attacker Report - " + date)
	print("\nCOUNT\tIP ADDRESS\tCOUNTRY")

	#array used to store each failed login attempt
	failed_array = []
	with open("syslog.log") as file:
		#Iterate through syslog.log
		for line in file:
			z = re.findall(r"\bFailed", line)
			if z:
				failed_array.append(line)

	#Below loop isolates each IP address
	#array used to store each IP address
	ip_array = []
	for entry in failed_array:
		entry = entry.split(" from ")
		ip_section = entry[1].split(" ")
		ip = ip_section[0]
		ip_array.append(ip)

	#creates dictionary to store IP and number of login attepts from said IP
	#ip = key
	#value = count
	ip_dict = {}
	for ip in ip_array:
		if ip in ip_dict:
			#if IP already in dictionary -> increment its count
			ip_dict[ip] += 1
		else:
			#if IP not in dictionary -> set its count to 1
			ip_dict[ip] = 1

	#sorts the dictionary by count -> ascending order
	sorted_tuples = sorted(ip_dict.items(), key=lambda item: item[1])
	sorted_ip = {k: v for k, v in sorted_tuples}
	for key in sorted_ip:
		#iterate through each entry in dictionary
		#if IP count is greater than or equal to 10, find its country of origin
		if(int(sorted_ip[key]) >= 10):
			match = geolite2.lookup(str(key))
			if match is not None:
				#if country of origin exists, print number of failed attempts, IP, country of origin
				print(str(sorted_ip[key]) + "\t" + str(key) + "\t" + match.country)



	print("\n")

main()
