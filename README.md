Welcome to the XPG Cracker 1.0 repo!
It is only Windows compatible (for now).
It can be used to perform a dictionary password attack on pages.
For now you can perform the atack on the page.py (located in the repository) - to use it on other pages, you have to modify the source code.

It uses multiple requests in parallel.
The speed varies on the amout of workers you choose, i've managed to get around a 600 passes/sec with 300 workers
!WARNING! Too many workers might cause your device to crash!

How to launch the test page?
1. Open up terminal or powershell (don't turn it off or close it when testing)
2. Make sure you have python installed
3. To launch it make sure you are in the same directory as the script
4. Use python page.py to start
5. Check the address where it was hosted on e.g. http://127.0.0.1:5000/login in your browser to see if it works

How to use the cracker?
1. Open up the terminal or powershell
2. Make sure you have python installed
3. To launch it make sure you are in the same directory as the script
4. Use python cracker.py to start the menu
5. Choose all the parameters - the page, the username, the wordlist (use wordlists in the same folder as the cracker, I'm not sure if it works with paths), and the amount of workers
6. Wait for it to find the password, it'll print it out when it'll find it

USE IT ONLY ON YOUR PRIVATE NETWORKS.
I AM NOT RESPONSIBLE FOR ANY HARM DONE WITH THIS TOOL.

https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt - a really good wordlist to use with this tool.

By Maciusk
