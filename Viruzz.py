import colorama
from colorama import Fore,Style,Back,init
init(autoreset=True)
import os
import time
from gtts import gTTS
import phonenumbers
from phonenumbers import geocoder,carrier

print(Fore.LIGHTRED_EX + Style.BRIGHT + "Opening tool")
time.sleep(2)

for i in range(3):
    print(Fore.LIGHTRED_EX + Style.BRIGHT +"wait....")
    time.sleep(1)
time.sleep(4)
print( Fore.RED + Style.BRIGHT + "                 _____      ______ _________________        ____________          ")
time.sleep(2)
print( Fore.CYAN + Style.BRIGHT + "                      \    /      |      |     |    |       |          /          ")
time.sleep(2)
print( Fore.LIGHTGREEN_EX + Style.BRIGHT + "                       \  /       |      |_____|    |       |         /           ")
time.sleep(2)
print( Fore.LIGHTGREEN_EX + Style.BRIGHT + "                        \/        |      |\         |_______|        /__________  ")
time.sleep(2)
print( Fore.CYAN + Style.BRIGHT + "                                         | \                                      ")
time.sleep(2)
print( Fore.RED + Style.BRIGHT + "                                         |  \                                     ")

print("")
print("")

print( Fore.MAGENTA + Style.BRIGHT + " 01. I Love you virus")
print("")
print( Fore.MAGENTA + Style.BRIGHT + " 02. Triple six virus (666)")
print("")
print( Fore.MAGENTA + Style.BRIGHT + " 03. Hackster virus")
print("")
print( Fore.MAGENTA + Style.BRIGHT + " 04. Version")
print("")
print( Fore.MAGENTA + Style.BRIGHT + " 05. Help")
time.sleep(2)
print("")
print("")
print(Fore.RED + Style.BRIGHT + "Warning : ")
print(Fore.LIGHTRED_EX + " Use This tool Only if you know to come back to our initial position . ")
print("")
user = input(" Enter -> ")




if ( user == "01" or user == "1"):
    
    print(" You wank to start virus . Answer in yes(y) or no(n) ")
    answer = input(" answer => ")
    if ( answer == "y"):
        print("Starting....")
        time.sleep(2)
        msg = "You have been Hacked"
        language = "en"
        obj = gTTS( text=msg , lang=language , slow = False)
        obj.save("viruzz.mp4")

        time.sleep(2)

        while True:
            
            os.system("viruzz.mp4")

    elif ( answer == "n"):

        for i in range(100):

            print (Fore.BLUE + Back.LIGHTRED_EX + Style.BRIGHT + " ok ! Get lost....")
            time.sleep(1)
    
    else:

        print

###--------------------------- triple six virus -------------------------------###

elif ( user == "02" or user == "2"):

    print("Are you Ready . Answer in yes(y) or no(n) ")
    answer2 = input(" answer => ")

    if ( answer2 == "y"):
        print("Starting.....")
        time.sleep(2)
        print("Starting.....")

        while True:

            print(Fore.LIGHTRED_EX + Style.BRIGHT + Back.BLACK +"you are hacked")
            time.sleep(1)
            
    
    elif ( answer2 == "n"):
        
        for i in range(100):

            print( Fore.LIGHTBLUE_EX + Back.BLACK + Style.BRIGHT + "Ok! Get lost") 
            time.sleep(1)   
      


### ----------------------------Hackster virus -------------------------------###


elif ( user == "03" or user == "3" ):

    print("Are you ready . Answer in yes(y) or no(n) ")
    answer3 = input("answer => ")

    if ( answer3 == "y" ):

        que = input("What is your name -> ")
        print("")
        time.sleep(1)
        print(f"So hello {que}")
        print("")
        time.sleep(1)
        print("")
        print( Fore.LIGHTYELLOW_EX + Style.BRIGHT + "you want to hack...")
        time.sleep(1)
        print("")
        print("")
        print( Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "1) email")
        print( Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "2) phone number")
        print( Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "3) trace ip address")

        que1 = input(" Enter - > ")

        if ( que1 == "01" or que1 == "1"):

            email = input(Fore.YELLOW + " Enter The email which you want to hack ->  ")
            time.sleep(1)
            password = input(Fore.YELLOW + " Enter the path of password list -> ")
            
            with open (password , "r") as f:

                fread = f.read(password)
                
                print("It take some time")

        elif ( que1 == "02" or que1 == "2"):

            
            no = input(Fore.GREEN + Style.BRIGHT + "Enter the phone number with country code - > ")

            phoneNumber = phonenumbers.parse( no , None)

            country = geocoder.description_for_number( phoneNumber , "en")
            serviceProvider = carrier.name_for_number( phoneNumber , "en")

            print(Fore.MAGENTA + Style.BRIGHT +  f"COUNTRY -> {country}")
            print(Fore.MAGENTA + Style.BRIGHT +  f"SERVICE PROVIDER -> {serviceProvider}")

        elif ( que1 == "03" or que1 == "2"):

            ipadress = input(" enter the ip adress which you want to trace -> ")

elif ( user == "04" or user == "4"):

    print(Style.BRIGHT + Back.YELLOW + Fore.GREEN + " VERSION ----> 2021.0.02")
    print(Style.BRIGHT + Back.YELLOW + Fore.GREEN + " OWNER ------> Aditya12-cyber ")
    print(Style.BRIGHT + Back.YELLOW + Fore.GREEN + " check my github repository ----> https://github.com/aditya12-cyber/  ")

elif ( user == "05" or user == "5"):

    print("Owner -> aditya12-cyber")

    print( Fore.LIGHTCYAN_EX + Style.BRIGHT + " If you liked our tool then like us -- >")
    fedbck = input(Fore.GREEN + Style.BRIGHT + " you like our tool . Answer in yes(y) or no(n) -> ")
    if ( fedbck == "y"):
        print( Fore.CYAN + " Give our feedback ")
        time.sleep(1)
        feedback = input( Fore.BLUE +"Feedback - > ")

    
    elif ( fedbck == "n"):
        print(Fore.RED + "Tell our problem . I can help you  ")
        hlp = input( Fore.RED + " Problem - > ")

else:

    print( Fore.RED + Style.BRIGHT +           "                 _____      ______ _________________        ____________          ")
    print( Fore.CYAN + Style.BRIGHT +          "                      \    /      |      |     |    |       |          /          ")
    print( Fore.LIGHTGREEN_EX + Style.BRIGHT + "                       \  /       |      |_____|    |       |         /           ")
    print( Fore.LIGHTGREEN_EX + Style.BRIGHT + "                        \/        |      |\         |_______|        /__________  ")
    print( Fore.CYAN + Style.BRIGHT +          "                                         | \                                      ")
    print( Fore.RED + Style.BRIGHT +           "                                         |  \                                     ")
    time.sleep(2)
    print("Usage of this tool ->")
    print("Type 01,02,03,04,05 which tool you want to use ")
    
