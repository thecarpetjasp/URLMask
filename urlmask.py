#!/usr/bin/env python3
import time
import os
import colorama
from colorama import Fore, Style
# Creating a python program to mask a url.

# BANNER
os.system("cls||clear")
print (Fore.YELLOW)
print (" _ _  ___  _     __ __  ___  ___  _ __")
print ("| | || . \| |   |  \  \| . |/ __>| / /")
print ("| ' ||   /| |_  |     ||   |\__ \|  \ ")
print ("`___'|_\\_\\|___| |_|_|_||_|_|<___/|_\\_\\")
print ("")
time.sleep(0.5)

# SHORTENING URL
original_url = input("Enter the URL you want to mask: " + Style.RESET_ALL)
shortened_original_url = str(os.popen("curl -s https://is.gd/create.php\?format\=simple\&url\=" + original_url).read())
remove_junk = (shortened_original_url.replace("https://", ""))
final_short = remove_junk
print (Fore.YELLOW)

# CREATING SUB DIRECTORIES FOR URL
sub_link_input = input("Enter in a relevant sentence for your page. E.g. 'reset password': " + Style.RESET_ALL)
sub_link_final = (sub_link_input.replace(" ", "-"))
print (Fore.YELLOW)

# CREATING NEW DOMAIN NAME FOR URL
url_hostname = input("Please enter a hostname for the URL. E.g. 'netflix.com' 'facebook.com': " + Style.RESET_ALL)
print (Fore.YELLOW)

# CHOOSING FOR WORLD WIDE WEB
while True:
	ask_for_www = input(Fore.YELLOW + "Would you like to include 'www'? [Y/N]: " + Style.RESET_ALL)
	if ask_for_www == "y":
		complete_url = ("https://www." + url_hostname + "-" + sub_link_final + "@" + final_short)
		break
	elif ask_for_www == "Y":
		complete_url = ("https://www." + url_hostname + "-" + sub_link_final + "@" + final_short)
		break
	elif ask_for_www == "n":
		complete_url = ("https://" + url_hostname + "-" + sub_link_final + "@" + final_short)
		break
	elif ask_for_www == "N":
		complete_url = ("https://" + url_hostname + "-" + sub_link_final + "@" + final_short)
		break
	else:
		os.system("cls||clear")
		print (Fore.YELLOW + "INVALID OPTION" + Style.RESET_ALL)
		time.sleep(1)
		os.system("cls||clear")
os.system("cls||clear")
print (Fore.YELLOW + "YOUR NEW URL:\n" + Style.RESET_ALL)
print (complete_url)

# END OF PROGRAM.
