# URLMask
![banner](https://user-images.githubusercontent.com/71789855/140232354-64b5ca13-e6bd-40dc-96cd-8820778b6690.png)


Python program for Linux users to change a URL to ANY domain.


A program that can take any url and mask it to any domain name you like. E.g. netflix.com, facebook.com, google.com, reddit.com.

PLEASE USE RESPONSIBLY. THIS PROGRAM WAS CREATED FOR EDUCATIONAL PURPOSES ONLY AND I DO NOT CONDONE ANY ILLEGAL USE FOR THIS WHATSOEVER.
SENDING OUT ANY URL/LINK THAT IS DECEITFUL TO ANYONE UNAWARE IS ILLEGAL. BE RESPONSIBLE.






#


**INSTALL AND LAUNCH**

**Step (1):**
`git clone https://github.com/thecarpetjasp/URLMask`



**Step (2):**
`cd URLMask`


**Step (3): (OPTIONAL)**
`python3 install.py`
*This step will add the program to '/usr/bin/' so that you can run the program anywhere from your terminal.*


**Step (4):**
`python3 urlmask.py`
or if you followed step (3):
`urlmask`


#





**TUTORIAL / PRE-MADE TEMPLATES**

**Step (1):**
Input the URL that you want to mask.

![input_url](https://user-images.githubusercontent.com/71789855/140272713-a5453982-5edc-4ec0-9bfd-10f4aba3c293.png)

#

**Step (2):**
Select one of the many pre-made templates for your desired URL.

![choose_template](https://user-images.githubusercontent.com/71789855/140272700-5ea07d94-4324-4153-9646-864886aed938.png)

#

**Step (3):**
Choose your own TLD (*Top Level Domain*) out of *.com* & *.co.uk*.

![choose_TLD](https://user-images.githubusercontent.com/71789855/140272703-150c5ada-90df-4724-b357-98ed782ebdc4.png)

#

**Step (4):**
Choose if you would like 'World Wide Web' attached with your URL.

![choose_www](https://user-images.githubusercontent.com/71789855/140272704-26b25f99-4c99-40ce-aadc-19cfe78d9a8b.png)

#

**Step (5):**
Your new URL will be output immediately.

![output](https://user-images.githubusercontent.com/71789855/140272714-74c939e4-2c5d-435c-a407-db86525f075e.png)


#


**TUTORIAL / CUSTOM TEMPLATES**

If the URL you wish to copy is not listed on the template list - you can make your own.


**Step (1):**
Choose option 11 for *custom* on the template list.

![choosing_custom](https://user-images.githubusercontent.com/71789855/140272706-51c80a36-01cb-4cb6-9141-ef7275870702.png)

#

**Step (2):**
Now copy the directory path of your chosen URL. 
Be sure to start the copy of your directory from the first English character after the TLD (*'.co.uk', '.com'*)

![copy_directory](https://user-images.githubusercontent.com/71789855/140272707-5179701b-3486-4ce0-a7d6-ed9a22b64442.png)
![paste_directory](https://user-images.githubusercontent.com/71789855/140272716-ce6d2d2e-a70b-4db4-a747-df65afe6ba6c.png)

#

**Step (3):**
Enter the domain name of the URL.

![input_custom_domain](https://user-images.githubusercontent.com/71789855/140272712-ebf95e57-1287-4f66-9656-66c17b633a04.png)

#

**Step (4):**
Your custom URL will output immediately after.

![custom_output](https://user-images.githubusercontent.com/71789855/140272710-7de9d451-e9d0-499b-816a-78ee80af1971.png)

#


**Comparison**

Here's a comparison shot. On top you have a REAL Google Drive URL. On the bottom you have a FAKE Google Drive URL generated with URLMask.py.

![comparison](https://user-images.githubusercontent.com/71789855/140248587-3afa833a-1a51-476c-96dc-d9e4d1f13eb1.png)


#

**NOTE:** *Something to bear in mind...*

Mozilla Firefox is the only browser that will warn you about accessing these URL's. I've tested on all platforms and Firefox is the only browser that will alert a warning.

The URL's all work without any warning message for:
  * Google Chrome
  * Microsoft Edge
  * iPhone / iMac Safari
  * Android Chrome

If you are testing your URL's on Kali Linux, then it's a good chance you're using Mozilla Firefox which will explain any message you might receive when visiting the URL's.
