# returns status code for web url
import requests
import sys
print("""     ,%&& %&& %
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
 jgs\\/;:   \'--' `---`           `\\//-\\///""")

run = True
while run: 
    # we need to establish some key commands
    
    entry_command = input("Welcome to InfoCreep. Enter -h for help! ")
    if entry_command == "-h":
        print("""I hope these help: 
            -h                     --> help menu
            scout http://target ip --> gain server code recon on target
            dnsRec <target ip>     --> use View.DNS through the shell, currently expanding""")
  
        # response = requests.get(target)
        # status = response.status_code

        # if len(sys.argv) != target:
        #    print("Incorrect usage, enter target IP to get http status")
        #    sys.exit(1)
        # else:
        #    for status in range(100, 511):
        #        if 200 <= status <= 226:
        #           print("slow processing: ", status)
        #        elif 200 <= status <= 226:
        #            print("It is live:", status)
        #        elif 300 <= status <= 308:
        #            print("website redirect, check nano file:", status)
        #        elif 400 <= status <= 451:
        #            print("Client error response: ", status)
        #        elif 500 <= status <= 511:
        #            print("likely server error: ", status)


    #exit_input = input("Do you want to check another URL? (Y/N)").strip().lower()
    #if exit_input != 'yes':
    #   run = False
        
            