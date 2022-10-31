#!/usr/bin/env python3
#Name: Griffin Pundt
#Class: NSSA221
#Assignment: Script 03
#Date 10/15/2022


import os
import time

#shows the options for the user to use, prompts user input
#this will be at the top of main, so whenever we loop back we will reset at the main menu
def show_menu():
	os.system("clear")
	print("\t" + '*' *  40)
	print("\t" + "*"*11 + " Shortcut Creator " + "*"*11)
	print("\t" + "*"*40)

	print("\n\nEnter Selection:")
	print("\n\n\t1 - Create a shortcut in your home directory.")
	print("\n\t2 - Remove a shortcut from your home directory.")
	print("\n\t3 - Run shortcut report.")

	user_input = input('\n\nPlease enter a number (1 - 3) or "Q/q" to quit the program.\t') 

	return user_input


def main():
	#gets user so we can get home directory
	os.system("whoami >> user.txt")
	with open("user.txt") as file:
		user = file.readline()
		user = user.strip()
	os.system("rm user.txt")

	#gets home directory
	os.system("pwd >> home_directory.txt")
	with open("home_directory.txt") as file:
		home_directory = file.readline()
		home_directory = home_directory.strip()
	os.system("rm home_directory.txt")

	#main functionality
	sentinel = True;
	while(sentinel):
	#each user input from main menu will activate different part of main
		user_input = show_menu()
		#create a link
		if(user_input == "1"):
			os.system("clear")
			source_file = input("Please enter the file name to create a shortcut:\t")
			file_path = home_directory + "/" + source_file
			#print(file_path)
			time.sleep(2)
			if(os.path.exists(file_path) is True):
				input("Found " + file_path + ".\nSelect Y/y to create shortcut:\t")
				print("Creating shortcut, Please wait...")
				link = "/home/" + user +"/" + source_file
				os.symlink(file_path, link)
				time.sleep(2)
				print("Shortcut created. Returning to Main Menu...")
				time.sleep(2)

			else:
				print("\nSorry, couldnt find " + source_file + "\nReturning to Main Menu.")
				time.sleep(4)
		#remove a link
		elif(user_input == "2"):
			os.system("clear")
			destination_file = input("Please enter the shortcut/link to remove:\t")
			file_path = "/home/" + user + "/" + destination_file
			if(os.path.exists(file_path) is True):
				time.sleep(2)
				input("Found " + destination_file + "\nAre you sure you want to remove " + destination_file + "? Press Y/y to confirm:\t")
				print("Removing link, please wait...")
				os.system("rm " + file_path)
				time.sleep(2)
				print("\nLink removed. Returning to Main Menu...")
				time.sleep(2)
			else:
				time.sleep(2)
				print("Sorry, couldn't find " + destination_file + "!\nReturning to Main Menu...")
				time.sleep(2)
		#shows link log
		elif(user_input == "3"):
			os.system("clear")
			print("\t" + "*" * 39)
			print("\t" + "*" * 11 + " Shortcut Report " + "*" * 11)
			print("\t" + "*" * 39)

			print("\n\nYour current directory is /home/" + user + "/.")
			os.system("find /home/" + user + "/ -type l >> links.txt")
			links = []
			files = []
			with open ("links.txt") as file:
				for _ in range(30):
					link = file.readline()
					if(link != ""):
						link = link.strip()
						desired_file = link.split("/")
						if(link != ""):
							links.append(link)

						files.append(desired_file[len(desired_file)-1])
			os.system("rm links.txt")
			print("\nThe number of links is " + str(len(links)) + ".")
			print("\n\nSYMBOLIC LINK\t\t\tTARGET PATH")
			i = 0
			while(i < len(files)):
				print(files[i] + "     \t\t\t" + links[i])
				i += 1

			user_input = input("\nTo return to Main Menu, press ENTER:")
			os.system("clear")
			print("Returning to Main Menu...")
			time.sleep(2)

		#quits program
		elif(user_input == 'q' or user_input == "Q"):
			os.system("clear")
			print("Quitting program: returning to shell...\nHave a wonderful day!")
			time.sleep(2)
			os.system("clear")
			sentinel = False

		#if user is silly and inputs bad stuff, tells them to stop and loops again
		else:
			os.system("clear")
			print("Please enter a valid command...")
			time.sleep(2)

main()
