import tkinter
from tkinter import *
import requests
from requests import *
import tkinter.messagebox as tmsg
import os

root = Tk()

# The ip address Function is here

def ip_func():

    IP_Address = ipentry.get()

    response = requests.get(f"http://ip-api.com/json/{IP_Address}").json()


    # tmsg.showinfo("result" , f"status -> { response['status'] }")
    tmsg.showinfo("IP_TRACER" , f"  Status - > { response['status'] } \n \n  Country - > { response['country'] } \n \n CountryCode - > { response['countryCode'] } \n \n City - > { response['city'] } \n \n Region - > { response['region'] } \n \n RegionName - > { response['regionName'] } \n \n Zip - > { response['zip'] } \n \n latitude - > { response['lat'] } \n \n longitude - > { response['lon'] } \n \n Timezone - > { response['timezone'] } \n \n ISP - > { response['isp'] } \n \n Organisation - > {response['org']} \n \n IP_Address - > {response['query']}")

# save function is here

def save():
    ipad = ipentry.get()

    response = requests.get(f"http://ip-api.com/json/{ipad}").json()

    nullvar = ""

    checking_file = os.path.isfile("ip_Tracer.txt")

    print(checking_file)

    if (ipad == nullvar):
        tmsg.showerror("Error" , "Please Enter any value")
    else:
        if (checking_file == True):
        
            with open("ip_Tracer.txt" , "a") as f:

                f.write(f"\n \n     IP_address you entered -> {response['query']} \n \n   Status - > { response['status'] } \n   Country - > { response['country'] } \n  CountryCode - > { response['countryCode'] } \n  City - > { response['city'] } \n  Region - > { response['region'] } \n  RegionName - > { response['regionName'] } \n  Zip - > { response['zip'] } \n  latitude - > { response['lat'] } \n  longitude - > { response['lon'] } \n  Timezone - > { response['timezone'] } \n  ISP - > { response['isp'] } \n  Organisation - > {response['org']} \n  IP_Address - > {response['query']} \n  \n")

        elif (checking_file == False):

            with open("ip_Tracer.txt" , "a") as f:

                f.write(f"\n \n     IP_address you entered -> {response['query']} \n \n  Status - > { response['status'] } \n   Country - > { response['country'] } \n  CountryCode - > { response['countryCode'] } \n  City - > { response['city'] } \n  Region - > { response['region'] } \n  RegionName - > { response['regionName'] } \n  Zip - > { response['zip'] } \n  latitude - > { response['lat'] } \n  longitude - > { response['lon'] } \n  Timezone - > { response['timezone'] } \n  ISP - > { response['isp'] } \n  Organisation - > {response['org']} \n  IP_Address - > {response['query']} \n  \n")


root.geometry("360x600")
root.title("IP TRACER")
root.minsize(360,600)
root.configure(bg = "#ABB2B9")

Font_tuple = ("Franklin Gothic Demi Cond", 20, "bold")
Font_tuple1 = ("Footlight MT Light", 12, "bold")
Font_tuple2 = ("Tempus Sans ITC" , 13 , "italic")

icophoto = PhotoImage(file = 'TRACER.png')
root.iconphoto(False , icophoto)

fr1 = Frame(root , bg = "#154360" , padx = 10 , pady = 8 , borderwidth = 7 , relief = FLAT)
fr1.pack(fill = X , padx = 5 , pady = 4 , anchor = "n" , side = "top")

fr2 = Frame(root , bg = "#0E6655" , padx = 20 , pady = 30 , borderwidth = 7 , relief = FLAT)
fr2.pack(fill = X , padx = 10 , pady = 8 , side = "top")

fr3 = Frame(root , bg = "#154360" , padx = 20 , pady = 15 , borderwidth = 7 , relief = FLAT)
fr3.pack(fill = X , padx = 10 , pady = 8 , side = "top")

fr4 = Frame(root , bg = "red" , padx = 20 , pady = 15 , borderwidth = 7 , relief = FLAT)
fr4.pack(fill = X , padx = 10 , pady = 8 , side = "top")

Label(fr1 , text = "- - - IP Tracing GUI - - -" , fg = "white" , bg = "#154360" , font = Font_tuple).pack()

Label(fr2 , text = "Enter the ip address : - " , bg = "#0E6655" , fg = "#1B2631" , font = Font_tuple ).pack()

ipadressval = StringVar()

ipentry = Entry(fr2 , width = 40 , textvariable = ipadressval , borderwidth = 7 , bg = "#82E0AA" , fg = "#1B2631" , relief = RAISED , font = Font_tuple1)
ipentry.pack(padx = 10 , pady = 10 , anchor = "n" , side = "top")

trace = Button(fr2 , text = "TRACE" , font = "couriersnew 13 bold" , padx  = 5 , pady = 3 , bg = "#cce7e8" , borderwidth = 4 , relief = RAISED , command = ip_func)
trace.pack( side = "top" , padx = 5 , pady = 16 )

Label(fr3 , text = "Enter the IP address in \n IPV4 format Ex :- 192.168.26.12" , bg = "#154360" , font = Font_tuple1 ).pack(side = "top" , anchor = "n" , pady = 1)

# Label(fr3 , text = "Status" , bg = "#154360" , font = "timesnewroman 8 bold" ).pack(side = "top" , anchor = "n" , pady = 1)
Button(fr4 , text = "    Save   " , bg = "white" , fg = "black" , padx = 10  , pady = 4 , borderwidth = 3 , relief = SUNKEN , font = Font_tuple1 , command = save).pack(side = "bottom" , anchor = "s" , padx = 5 , pady = 4)
Label(fr4 , text = "if you want to save the input \n in a file then click on the save button" , font = Font_tuple1 , bg = "red" , fg = "black" , padx = 3 , pady = 3 ).pack(side = "bottom" , anchor = "nw" , fill = X ) 


root.mainloop()
