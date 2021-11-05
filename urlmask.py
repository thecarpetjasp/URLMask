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
print (Fore.YELLOW +"\n\n")

# CREATING SUB DIRECTORIES FOR URL
while True:
	print (Fore.YELLOW + "Choose a template for your URL's domain & directory OR choose custom\n")
	print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "]" + Fore.YELLOW + " Google              " + Fore.RED + "[" + Fore.WHITE + "11" + Fore.RED + "]" + Fore.YELLOW + " Custom")
	print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "]" + Fore.YELLOW + " Facebook")
	print (Fore.RED + "[" + Fore.WHITE + "3" + Fore.RED + "]" + Fore.YELLOW + " Youtube")
	print (Fore.RED + "[" + Fore.WHITE + "4" + Fore.RED + "]" + Fore.YELLOW + " Reddit")
	print (Fore.RED + "[" + Fore.WHITE + "5" + Fore.RED + "]" + Fore.YELLOW + " drive.google")
	print (Fore.RED + "[" + Fore.WHITE + "6" + Fore.RED + "]" + Fore.YELLOW + " Instagram")
	print (Fore.RED + "[" + Fore.WHITE + "7" + Fore.RED + "]" + Fore.YELLOW + " Microsoft")
	print (Fore.RED + "[" + Fore.WHITE + "8" + Fore.RED + "]" + Fore.YELLOW + " Netflix")
	print (Fore.RED + "[" + Fore.WHITE + "9" + Fore.RED + "]" + Fore.YELLOW + " Paypal")
	print (Fore.RED + "[" + Fore.WHITE + "10" + Fore.RED + "]" + Fore.YELLOW + " Twitter")
	print ("")
	ask_for_sub = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
	print ("\n\n")
	if ask_for_sub == "1":
		search_query_beta = input(Fore.YELLOW + "Type a search query to customise directory. E.g 'earn free money': " + Style.RESET_ALL)
		search_query_alpha = (search_query_beta.replace(" ", "+"))
		sub_link_final = ("search%q=" + search_query_alpha + "&A=156JKBbf8y6484sJGD8j%")
		print ("\n\n")
		print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
		print ("")
		print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
		print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
		print ("")
		choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
		if choose_TLD == "1":
			url_hostname = ("google.co.uk")
		elif choose_TLD == "2":
			url_hostname = ("google.com")
		else:
			url_hostname = ("google.com")
		break
	elif ask_for_sub == "2":
                search_query_beta = input(Fore.YELLOW + "Type a page name to customise directory. E.g 'Horror Movies': " + Style.RESET_ALL)
                search_query_alpha = (search_query_beta.replace(" ", ""))
                sub_link_final = (search_query_alpha + "&page=True%")
                print ("\n\n")
                print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
                print ("")
                print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
                print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
                print ("")
                choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
                if choose_TLD == "1":
                        url_hostname = ("facebook.co.uk")
                elif choose_TLD == "2":
                        url_hostname = ("facebook.com")
                else:
                        url_hostname = ("facebook.com")
                break
	elif ask_for_sub == "3":
                sub_link_final = ("watch&=xpVfc")
                print ("\n\n")
                print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
                print ("")
                print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
                print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
                print ("")
                choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
                if choose_TLD == "1":
                        url_hostname = ("youtube.co.uk")
                elif choose_TLD == "2":
                        url_hostname = ("youtube.com")
                else:
                        url_hostname = ("youtube.com")
                break
	elif ask_for_sub == "4":
		subreddit_beta = input(Fore.YELLOW + "Type in your chosen subreddit. E.g. 'AskReddit': " + Style.RESET_ALL)
		subreddit_alpha = (subreddit_beta.replace(" ", ""))
		post_topic_beta = input(Fore.YELLOW + "Type in your chosen post topic. E.g. 'Make easy money': " + Style.RESET_ALL)
		post_topic_alpha = (post_topic_beta.replace(" ", "_"))
		sub_link_final = ("r-" + subreddit_alpha + "-" + post_topic_alpha + "%")
		print ("\n\n")
		print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
		print ("")
		print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
		print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
		print ("")
		choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
		if choose_TLD == "1":
			url_hostname = ("reddit.co.uk")
		elif choose_TLD == "2":
			url_hostname = ("reddit.com")
		else:
			url_hostname = ("reddit.com")
		break
	elif ask_for_sub == "5":
		sub_link_final = ("file-d-150pIZvDM6u42ZH63MQ-view%")
		print ("\n\n")
		print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
		print ("")
		print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
		print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
		print ("")
		choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
		if choose_TLD == "1":
			url_hostname = ("drive.google.co.uk")
		elif choose_TLD == "2":
			url_hostname = ("drive.google.com")
		else:
			url_hostname = ("drive.google.com")
		break
	elif ask_for_sub == "6":
		sub_link_final = ("p-CV03PieKWK-%")
		print ("\n\n")
		print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
		print ("")
		print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
		print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
		print ("")
		choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
		if choose_TLD == "1":
			url_hostname = ("instagram.co.uk")
		elif choose_TLD == "2":
			url_hostname = ("instagram.com")
		else:
			url_hostname = ("instagram.com")
		break
	elif ask_for_sub == "7":
		sub_link_final = ("en-gb&wa=signin1.0%")
		print ("\n\n")
		print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
		print ("")
		print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
		print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
		print ("")
		choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
		if choose_TLD == "1":
			url_hostname = ("microsoft.co.uk")
		elif choose_TLD == "2":
			url_hostname = ("microsoft.com")
		else:
			url_hostname = ("microsoft.com")
		break
	elif ask_for_sub == "8":
		sub_link_final = ("gb-login&page=%3A%2F%2F%")
		print ("\n\n")
		print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
		print ("")
		print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
		print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
		print ("")
		choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
		if choose_TLD == "1":
			url_hostname = ("netflix.co.uk")
		elif choose_TLD == "2":
			url_hostname = ("netflix.com")
		else:
			url_hostname = ("netflix.com")
		break
	elif ask_for_sub == "9":
		sub_link_final = ("&login=True%")
		print ("\n\n")
		print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
		print ("")
		print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
		print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
		print ("")
		choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
		if choose_TLD == "1":
			url_hostname = ("paypal.co.uk")
		elif choose_TLD == "2":
			url_hostname = ("paypal.com")
		else:
			url_hostname = ("paypal.com")
		break
	elif ask_for_sub == "10":
		sub_link_final = ("&lang=en-gb%")
		print ("\n\n")
		print (Fore.YELLOW + "Choose TLD (Top Level Domain):" + Style.RESET_ALL)
		print ("")
		print (Fore.RED + "[" + Fore.WHITE + "1" + Fore.RED + "] " + Fore.YELLOW + ".co.uk" + Style.RESET_ALL)
		print (Fore.RED + "[" + Fore.WHITE + "2" + Fore.RED + "] " + Fore.YELLOW + ".com" + Style.RESET_ALL)
		print ("")
		choose_TLD = input(Fore.YELLOW + "Choose by number: " + Style.RESET_ALL)
		if choose_TLD == "1":
			url_hostname = ("twitter.co.uk")
		elif choose_TLD == "2":
			url_hostname = ("twitter.com")
		else:
			url_hostname = ("twitter.com")
		break
	elif ask_for_sub == "11":

                # CREATING NEW DOMAIN NAME FOR URL
		print (Fore.YELLOW + "Copy the directory of a site you wish to mask. \nStart with the first english letter after the TLD (.com / .co.uk).")
		sub_link_beta1 = input("\nEnter your custom directory: " + Style.RESET_ALL)
		sub_link_beta2 = (sub_link_beta1.replace("/", "-"))
		sub_link_final = (sub_link_beta2.replace("?", "&"))
		print ("")
		url_hostname = input(Fore.YELLOW + "Please enter a hostname for the URL. E.g. 'google.co.uk', 'facebook.com': " + Style.RESET_ALL)
		break
	else:
		os.system("cls||clear")
		print (Fore.RED + "INVALID OPTION\n\n" + Style.RESET_ALL)


print (Fore.YELLOW + "\n\n")



print (Fore.YELLOW + "\n\n")

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
		print (Fore.RED + "INVALID OPTION\n\n" + Style.RESET_ALL)
os.system("cls||clear")
print (Fore.YELLOW + "YOUR NEW URL:\n" + Style.RESET_ALL)
print (complete_url)

# END OF PROGRAM.
