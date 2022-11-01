#!/usr/bin/env python3

#Griffin Pundt
#NSSA 221 - 01
#Script02 Assignment

import os
import platform


#each function does what the function name implies
#top part of function acquires value and prints to standard output
#bottom part of function takes value and redirects to file_location


#get device hostname
def get_hostname(file_location):
	print("Hostname:\t\t", end="", flush=True)
	os.system("hostname")

	os.system("echo 'Hostname:\t\t' >> " + file_location)
	os.system("hostname >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get device domain suffix
def get_domain_suffix(file_location):
	print("Domain:\t\t\t", end="", flush=True)
	os.system("domainname")

	os.system("echo 'Domain:' >> " + file_location)
	os.system("domainname >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#----NETWORK INFO----
#get device ipv4 address
def get_ip(file_location):
	print("IPv4 Address:\t\t", end="", flush=True)
	ip = os.system("hostname -I | awk '{print $1}'")

	os.system("echo 'IPv4 Address:' >> " + file_location)
	os.system("hostname -I | awk '{print $1}' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get device default gateway
def get_gateway(file_location):
	os.system("ip route | grep default > gateway.txt")
	with open("gateway.txt") as file:
		line = file.readline()
	#print(line)
	split_line = line.split(" ")
	print("Gateway:\t\t" + split_line[2])
	os.system("rm gateway.txt")

	os.system("echo 'Gateway:' >> " + file_location)
	os.system("echo '" + split_line[2] + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get device network mask
def get_netmask(file_location):
	os.system("ifconfig | grep -i mask > netmask.txt")
	with open("netmask.txt") as file:
		line = file.readline()
	split_line = line.split(" ")
	print("Network Mask:\t\t" + split_line[12])
	os.system("rm netmask.txt")

	os.system("echo 'Network Mask:' >> " + file_location)
	os.system("echo '" + split_line[12] + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get device DNS addresses
def get_dns(file_location):
	with open("/etc/resolv.conf") as file:
		file.readline()
		file.readline()
		line1=file.readline()
	split_line1 = line1.split(" ")
	print("DNS1:\t\t\t" + split_line1[1].strip())

	os.system("echo 'DNS1:' >> " + file_location)
	os.system("echo '" + split_line1[1].strip() + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#----OS INFO----
#get device operating system
def get_os(file_location):
	os.system("grep '^NAME' /etc/os-release > os.txt")
	with open("os.txt") as file:
		line = file.readline()
	split_line = line.split('"')
	print("Operating System:\t" + split_line[1])
	os.system("rm os.txt")

	os.system("echo 'Operating System:' >> " + file_location)
	os.system("echo '" + split_line[1] + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get device operating system version
def get_os_version(file_location):
	os.system("grep '^VERSION' /etc/os-release > os_version.txt")
	with open("os_version.txt") as file:
		line = file.readline()
	split_line = line.split('"')
	print("Operating Version:\t" + split_line[1])
	os.system("rm os_version.txt")

	os.system("echo 'Operating Version:' >> " + file_location)
	os.system("echo '" + split_line[1] + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get device kernel version
def get_kernel_version(file_location):
	print("Kernel Version:\t\t", end="", flush=True)
	os.system("uname -r")

	os.system("echo 'Kernel Version:' >> " + file_location)
	os.system("uname -r >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#----STORAGE INFO----
#get device disk size
def get_disk_capacity(file_location):
	os.system("df -h / --output=size > capacity.txt")
	with open("capacity.txt") as file:
		file.readline()
		line = file.readline()
	print("Hard Drive Capacity:\t" + line.strip())
	os.system("rm capacity.txt")

	os.system("echo 'Hard Drive Capacity:' >> " + file_location)
	os.system("echo '" + line.strip() + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get available disk space
def get_available_space(file_location):
	os.system("df -h / --output=avail > available.txt")
	with open("available.txt") as file:
		file.readline()
		line = file.readline()
	print("Available Space:\t" + line.strip())
	os.system("rm available.txt")

	os.system("echo 'Available Space:' >> " + file_location)
	os.system("echo '" + line.strip() + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#----PROCESSOR INFO----
#get device CPU model
def get_cpu(file_location):
	os.system("lscpu | grep 'Model name' > cpu.txt")
	with open("cpu.txt") as file:
		line = file.readline()
	split_line = line.split(":")
	print("CPU Model:\t\t" + split_line[1].strip())
	os.system("rm cpu.txt")

	os.system("echo 'CPU Model:' >> " + file_location)
	os.system("echo '" + split_line[1].strip() + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get number of CPUs
def get_cpu_number(file_location):
	os.system("lscpu | grep 'CPU(s):' > cpu.txt")
	with open("cpu.txt") as file:
		line = file.readline()
	split_line = line.split(":")
	print("Number of Processors:\t" + split_line[1].strip())
	os.system("rm cpu.txt")

	os.system("echo 'Number of Processors:' >> " + file_location)
	os.system("echo '" + split_line[1].strip() + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get number of CPU cores
def get_cpu_cores(file_location):
	os.system("lscpu | grep 'Core(s)' > cpu.txt")
	with open("cpu.txt") as file:
		line = file.readline()
	split_line = line.split(":")
	print("Number of cores:\t" + split_line[1].strip())
	os.system("rm cpu.txt")

	os.system("echo 'Number of Cores:' >> " + file_location)
	os.system("echo '" + split_line[1].strip() + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#----MEMORY INFO----
#get device total RAM
def get_total_ram(file_location):
	os.system("free -g -h -t | grep 'Total' > ram.txt")
	with open("ram.txt") as file:
		line = file.readline()
	split_line = line.split(" ")
	#print(split_line)
	print("Total RAM:\t\t" + split_line[9].strip())
	os.system("rm ram.txt")

	os.system("echo 'Total RAM:' >> " + file_location)
	os.system("echo '" + split_line[9].strip() + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

#get device available RAM
def get_available_ram(file_location):
	os.system("free -g -h -t | grep 'Total' > ram.txt")
	with open("ram.txt") as file:
		line = file.readline()
	split_line = line.split(" ")
	print("Available RAM:\t\t" + split_line[23].strip())
	os.system("rm ram.txt")

	os.system("echo 'Available RAM:' >> " + file_location)
	os.system("echo '" + split_line[23].strip() + "' >> " + file_location)
	os.system("echo '\n' >> " + file_location)

def main():
	#first we create the log file that everything will be placed into
	os.system("hostname > hostname.txt")
	with open("hostname.txt") as file:
		hostname = file.readline()
	file_location = hostname.strip() + "_system_report.log"
	os.system("rm hostname.txt")
	#print(file_location)
	os.system("rm " + file_location)
	os.system("touch " + file_location)
	os.system("echo 'Name: Griffin Pundt' >> " + file_location)
	os.system("echo 'Class: NSSA221-01' >> " + file_location)
	os.system("echo 'Assignment: Script02' >> " + file_location)
	os.system("date >> " + file_location)
	os.system("echo '\n------------------\nSystem Report' >> " + file_location)


	#now that output file has been created, we can run each function
	os.system("clear")
	print("Device information")
	os.system("echo '\n-----------------\nDevice Information\n' >> " + file_location)
	get_hostname(file_location)
	get_domain_suffix(file_location)

	print("\nNetwork Information")
	os.system("echo '\n--------------------\nNetwork Information\n' >> " + file_location)
	get_ip(file_location)
	get_gateway(file_location)
	get_netmask(file_location)
	get_dns(file_location)

	print("\nOS Information")
	os.system("echo '\n-------------------\nOS Information\n' >> " + file_location)
	get_os(file_location)
	get_os_version(file_location)
	get_kernel_version(file_location)

	print("\nStorage Information")
	os.system("echo '\n-------------------\nStorage Information\n' >> " + file_location)
	get_disk_capacity(file_location)
	get_available_space(file_location)

	print("\nProcessor Information")
	os.system("echo '\n--------------------\nProcessor Information\n' >> " + file_location)
	get_cpu(file_location)
	get_cpu_number(file_location)
	get_cpu_cores(file_location)


	print("\nMemory Information")
	os.system("echo '\n-------------------\nMemory Information\n' >> " + file_location)
	get_total_ram(file_location)
	get_available_ram(file_location)
	os.system("echo '\n---end of system report---\n' >> " + file_location)

main()

