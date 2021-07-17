import tkinter
from tkinter import *
import tkinter.font as font
import phonenumbers
from phonenumbers import carrier,geocoder
import tkinter.messagebox as tmsg
import os

root = Tk()

root.geometry("700x450")
root.title("Phone_info_ bot")
root.minsize(700,450)
# root.maxsize(700,450)
root.configure( bg = "#282828")

# phonenum function here

def phonenum():

    number = PhonenumEntry.get()

    phonenumber = phonenumbers.parse(number , None)

    country = geocoder.description_for_number(phonenumber , "en")
    serviceProvider = carrier.name_for_number(phonenumber , "en")

    tmsg.showinfo("Info" , f" the info of you nuber is \n Country =  {country} \n and \n Service provider = {serviceProvider}")


# Save Function Here
def Save():

    number = PhonenumEntry.get()
    nullvar = ""

    phonenumber = phonenumbers.parse(number , None)

    country = geocoder.description_for_number(phonenumber , "en")
    serviceProvider = carrier.name_for_number(phonenumber , "en")

    checking_file = os.path.isfile("save.txt")
    print(checking_file)

    if (phonenumber == nullvar):
        tmsg.ERROR("error" , "Please ! Enter the phone number first ")

    else:
        if (checking_file == True):

            with open("save.txt" , "a") as f:

                f.write(f"Phone nhumber  => {phonenumber} \n Country => {country} \n Service provider => {serviceProvider} \n")

        elif (checking_file == False):

            with open("save.txt" , "a") as f:

                f.write(f"Phone nhumber  => {phonenumber} \n Country => {country} \n Service provider => {serviceProvider} \n")

# For fonts
 
myFont = font.Font(family='Helvatica', size = 22 , weight='bold')
myFont2 = font.Font(family='Helvatica' , size = 12 , weight = 'bold')

# Frames

fr1 = Frame(root , bg = "#FC4445" , padx = 10 , pady = 10 , relief = FLAT )
fr1.pack( side = "top" , anchor = "n" , fill = X)

fr2 = Frame(root , bg = "#CAFAFE" , padx = 10 , pady = 10 , relief = FLAT )
fr2.pack( side = "bottom" , anchor = "s" , fill = X)

fr3 = Frame(root , bg = "#CAFAFE" , padx = 10 , pady = 10 , relief = FLAT )
fr3.pack( side = "bottom" , anchor = "s" , fill = X)

# Label

Label( fr1 , text = "Phone Info Bot " , font = myFont , fg = "#CAFAFE" ,bg = "#FC4445" ).pack()

Label(root , text = "Enter the phone number below which you want to trace or \n to find infomation about the phonenumber" , font = " monospace 15 bold" , pady = 20 , bg = "#282828" , fg = "black").pack( fill= X , side = "top" , anchor = "n" )

# Variable

phonenumvalue = IntVar()

# Entry or input Field

PhonenumEntry = Entry( root , font = myFont2 ,  width = 40 , textvariable = phonenumvalue , border = 4 , relief =  SUNKEN , borderwidth = 2 , bg = "white" )
PhonenumEntry.pack( side = "top" , anchor = "n" , pady = 7 ) 

# Button

But2 = Button( root , text = "Trace" , relief = RAISED , border = 2 , padx = 20 , pady = 4 , borderwidth = 4 , command = phonenum )
But2.pack( side = "top" , pady = 5)

# Label

Label(root , text = " You want to save the input Click the button below " , font = "cursive 14 bold" , fg = "black" , bg = "#282828").pack(pady = 20)

# Button

But1 = Button( root , text = "Save" , fg = "black" , font = myFont2 , padx = 20 , pady = 8 , relief = RAISED , command = Save ).pack( side = "top" , anchor = "n" )

# Label

Label( fr2 , text = "Note : The Phone number which you want to trace enter with the country code" , pady = 6 , fg = "red" , bg = "#CAFAFE" , font = myFont2).pack( side = "bottom" , anchor = "s")



root.mainloop()
