# VortEX desktop assistant by Tejas Rajput.

# About

'''
This code doesn't contains any Artificial Intelligence or any AI's API. This code is just a desktop assistant that works on windows
only. This is just a small project that can make work of a windows user easy. This code is recommended to run on Windows 10 or 
Windows 11. If you love this project, you can give it a star on github.  
'''
'''
All commands:

1. explorer - this will open file explorer on your computer
2. google - this will open google's website on your web browser
3. youtube - this will open youtube on your web browser
4. chatgpt - this will open chatgpt.com on your web browser
5. copilot - this will open copilot.microsoft.com on your web browser
6. search - a prompt will ask you for your search, then it will search it on google
7. paint - this will open Microsoft Paint on your computer
8. name - VortEX will tell its name if you type this
9. word - this will open Microsoft Word on your computer
10. excel - this will open Microsoft Excel on your computer
11. google sheets - this will open docs.google.com/spreadsheets on your web browser.
12. google docs - this will open docs.google.com on your web browser
13. cmd - this will open Command Prompt on your computer
14. powershell - this will open Windows Powershell on your computer
15. calculator - this will open calculator on your computer
16. date, time, or year - this will show you the exact date and time
17. notepad - this will open Notepad on your computer
18. website - a prompt will ask you for your website's URL, this it will open it on your browser
19. restart pc or restart computer - this will restart your computer, so use it carefully
20. shutdown - this will shutdown your computer, so use it carefully
21. exit, quit, or close - this will exit the program

You can also type commands like "What is the time?", it will respond by giving you exact date and time.
This is because your message contained the word "time" which is already known in this program. But sometimes this program
can get illogical. For example, when you ask "What is powershell?", it will open windows powershell because your command contains
the word "powershell". As mentioned before, it can't tell you answers of questions that require intelligence. But if you really 
want to ask questions, you can use the search option and enter anything you want to search and then google can show you answer.
But this scripts isn't artificial intelligence itself.

If you enter any command that the program doesn't know like "turn off my pc", it will do nothing because it doesn't know this
command. And also, be cautious with the restart command. if you only type "restart" and don't type "pc" or "computer" after it,
VortEX will not recognize the command because saying restart can mean different things such as restarting an app instead of PC.
And they are also added for safety. So that accidenly typing "restart" can't restart your PC.
'''

# Updates in version 1.5

'''
Error Handeling:

In this new version of VortEX, we have added safe error handeling in the code so if any issue appears while running the code,
it will show you the exact error, which can prevent problems of a black screen flashing and exiting quickly. It will show the full
error that appeared so that you can search it online. For example, any syntax error, if you change update the code with syntax
errors. After showing the error, program will prompt you to press enter to exit. If you press enter, the program will exit.
This ensures safety for the program and better error handeling. 

Feature:

We have added a new command "commands" in the program by which, vortex will give you all the commmands that you can use in the 
program. It is essential for people who are new to it and don't know how to use it properly. 

We'll try bringing more good updates to this script. If you want a fueature in it, you can comment about it directly on github!
Or if you find any bugs, please report it in github so that we can fix it.

Thanks!
'''
try:
    import webbrowser
    import os
    import time
    import urllib.parse
    
    print("=== 🌌 VortEX Desktop Assitant V1.5 ===")
    print("\nType 'quit' or 'exit' or 'close' to exit. Or start typing to chat.")
    print("\nNote: This is not an Artificial Intelligence software. This is just a desktop assistant for Windows. Don't treat it\nas an AI. This software can't respond to casual chat.\nThanks!")
    print("\nVortEX: Hello! I am VortEX, your personal desktop assistant. What can I do for you?")
    while True:
        message = input("You: ")
        message = message.lower()
        if "explorer" in message:
            print("VortEX: Opening file explorer...")
            time.sleep(1)
            os.system("start explorer")
            continue
        elif "search" in message:
            query = input("VortEX: Enter the search you want: ")
            query = urllib.parse.quote(query)
            readable_query = query.replace("%20", " ")
            print(f"VortEX: Searching for {query}...")
            time.sleep(1)
            webbrowser.open(f"https://www.google.com/search?q={query}")
            continue
        elif "google sheets" in message:
            print("VortEX: Opening Google Sheets...")
            time.sleep(1)
            webbrowser.open("https://docs.google.com/spreadsheets")
        elif "google docs" in message or "google documents" in message:
            print("VortEX: Opening Google Docs...")
            time.sleep(1)
            webbrowser.open("https://docs.google.com")
        elif "google" in message:
            print("VortEX: Opening google...")
            time.sleep(1)
            webbrowser.open("https://www.google.com")
        elif "youtube" in message:
            print("VortEX: Opening youtube...")
            time.sleep(1)
            webbrowser.open("https://www.youtube.com")
        elif "chatgpt" in message:
            print("VortEX: Opening chatgpt...")
            time.sleep(1)
            webbrowser.open("https://chatgpt.com")
        elif "copilot" in message:
            print("VortEX: Opening copilot...")
            time.sleep(1)
            webbrowser.open("https://copilot.microsoft.com")
        elif "paint" in message:
            print("VortEX: Starting Microsoft Paint...")
            time.sleep(1)
            os.system("mspaint")
        elif "name" in message:
            print("VortEX: My name is VortEX. A Desktop Assistant created by Tejas Rajput.")
        elif "word" in message:
            try:
                print("VortEX: Starting Microsoft Word...")
                time.sleep(1)
                os.system("start winword")
            except:
                print("VortEX: There was a problem opening Microsoft Word. You may not have Word installed on your PC.")
        elif "excel" in message:
            try:
                print("VortEX: Starting Microsoft Excel...")
                time.sleep(1)
                os.system("start excel")
            except:
                print("VortEX: There was a problem opening Microsoft Excel. You may not have Excel installed on your PC.")
        elif "cmd" in message or "command prompt" in message:
            print("VortEX: Opening Command Prompt...")
            time.sleep(1)
            os.system("start cmd")
        elif "powershell" in message:
            print("VortEX: Opening Powershell...")
            time.sleep(1)
            os.system("start powershell")
        elif "calculator" in message:
            print("VortEX: Opening Calculator...")
            time.sleep(1)
            os.system("calc")
        elif "date" in message or "time" in message or "year" in message:
            print("VortEX: The current date and time is:\n")
            os.system("powershell date")
        elif "notepad" in message:
            print("VortEX: Starting Notepad...")
            time.sleep(1)
            os.system("start notepad")
        elif "website" in message:
            website = input("VortEX: Enter the website URL that you want to open: ")
            print(f"Opening {website}...")
            time.sleep(1)
            webbrowser.open(website)
        elif ("restart" in message and "pc" in message) or ("restart" in message and "computer" in message):
            print("VortEX: Restarting your computer...")
            time.sleep(1)
            os.system("shutdown /r /t 0")
        elif "shutdown" in message:
            print("VortEX: Shutting down your computer...")
            time.sleep(1)
            os.system("shutdown /s /t 0")
        elif "exit" in message or "quit" in message or "close" in message:
            print("VortEX: Exiting program...")
            time.sleep(1)
            break
        elif "commands" in message:
            print("All commands:")
            print('''
            1. explorer - this will open file explorer on your computer
            2. google - this will open google's website on your web browser
            3. youtube - this will open youtube on your web browser
            4. chatgpt - this will open chatgpt.com on your web browser
            5. copilot - this will open copilot.microsoft.com on your web browser
            6. search - a prompt will ask you for your search, then it will search it on google
            7. paint - this will open Microsoft Paint on your computer
            8. name - VortEX will tell its name if you type this
            9. word - this will open Microsoft Word on your computer
            10. excel - this will open Microsoft Excel on your computer
            11. google sheets - this will open docs.google.com/spreadsheets on your web browser.
            12. google docs - this will open docs.google.com on your web browser
            13. cmd - this will open Command Prompt on your computer
            14. powershell - this will open Windows Powershell on your computer
            15. calculator - this will open calculator on your computer
            16. date, time, or year - this will show you the exact date and time
            17. notepad - this will open Notepad on your computer
            18. website - a prompt will ask you for your website's URL, this it will open it on your browser
            19. restart pc or restart computer - this will restart your computer, so use it carefully
            20. shutdown - this will shutdown your computer, so use it carefully
            21. exit, quit, or close - this will exit the program
            22. commands - this shows all available commands
            ''')
        else:
            print("VortEX: Sorry. I didn't got that command. I am currently learning to answer more questions.")
except Exception as e:
    print("An error has occured when starting VortEX:")
    print(f'''{e}''')
    input("Press enter to exit...")
