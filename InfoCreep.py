# returns status code for web url
import requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

welcome_shown = False
run = True
while run: 
    if not welcome_shown:
        print("""     
                    ,%&& %&& %
                    ,%&%& %&%& %&
                    %& %&% &%&% % &%
                    % &%% %&% &% %&%&,
                    &%&% %&%& %& &%& %
                    %%& %&%& %&%&% %&%%&
                    &%&% %&% % %& &% %%&
                    && %&% %&%& %&% %&%'
                    '%&% %&% %&&%&%%'%
                    % %& %& %&% &%%
                        `\%%.'  /`%&'
                        |    |            /`-._           _\\/
                        |,   |_          /     `-._ ..--~`_
                        |;   |_`\_      /  ,\\.~`  `-._ -  ^
                        |;:  |/^}__..-,@   .~`    ~    `o ~
                        |;:  |(____.-'     '.   ~   -    `    ~
                        |;:  |  \ / `\       //.  -    ^   ~
                        |;:  |\ /' /\_\_        ~. _ ~   -   //-
                        \\/;:   \'--' `---`           `\\//-\\///""")
        print("Welcome to InfoCreep. Enter -h for help! ")
        welcome_shown = True
    # we need to establish some key commands...and some ascii art
    if welcome_shown:
        command = input("> ")
    else:
        command = input("Welcome to InfoCreep. Enter -h for help! ")

    if command == "-h":
        print("""I hope these help: 
            -h                     --> help menu
            scout http://target ip --> gain server code recon on target
            dnsRec <target ip>     --> use View.DNS through the shell, currently expanding""")
    elif command.startswith("scout "):
        target_url = command.split("scout ")[1]

        try:
            r = requests.get(target_url)
            print(f"Status Code for {target_url}: {r.status_code}")

        except requests.exceptions.RequestException as e:
            # Handle any request-related exceptions
            print(f"Error connecting to {target_url}: {e}")
    
    elif command.lower() == "exit":
        print("Exiting InfoCreep...")
        break
        
            