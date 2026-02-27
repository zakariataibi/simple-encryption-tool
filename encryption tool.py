import random
import string
from tkinter import *

chars = "  " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

label3 =None
label2 =None
label1 =None
button4 =None
entry =None
button1 = None
button2 = None
cipher_text = None
plain_text =None
label4 =None

#_____________________________________________ GUI _________________________________________________________#
 
widget = Tk()
widget.geometry("400x400") 
widget.title("CipherVault")
icon = PhotoImage(file ='icon.png' )
widget.iconphoto(True,icon)
widget.config(background='azure')

#_____________________________________________ FIRST BUTTON _________________________________________________#


def First_button():
 global button1
 button1 = Button(widget,text='Encrypt a message')
 button1.config(font=('Times New Roman',23,'bold '),bg='#9bbdb3',activebackground='#9bbdb3',command = open_new_window)
 button1.place(x=70,y=60)

#_____________________________________________ SECOND BUTTON ___________________________________________________#


def Second_button(): 
 global button2
 button2 = Button(widget,text='Decrypt a message')
 button2.config(font=('Times New Roman',23,'bold'),bg = '#9bbdb3',activebackground = '#9bbdb3',command = open_window)
 button2.place(x=70,y=150)

#_________________________________________ ENCRYPT________________________________________________________________#

def encrypt() :
 global cipher_text
 plain_text = entry.get()

 cipher_text = ""

 for letter in plain_text :
   if letter in chars:
    index = chars.index(letter)
    cipher_text += key[index]
   else:
    cipher_text+=letter
 label3.config(text=cipher_text)   # ← تحديث النص داخل الليبل

#_____________________________________________ THE NEW GUI1 ___________________________________________________#


def open_new_window():
 global label4
 global label2
 global label3
 global button4
 global entry
 global label1
 label1 = Label(widget,text='Enter to encrypt :')
 label1.config(font=('Times New Roman',15,'bold'),bg = "azure")
 label1.place(x=10,y=100)
 entry = Entry(widget,width=18,font=('Arial',15))
 entry.place(x=175,y=100)

 button4 = Button(widget,text='Submit')
 button4.config(font=('Times New Roman',15,'bold'),bg='azure',activebackground='azure',command=encrypt)
 button4.place(x=165,y=160)

 label2 = Label(widget,text='The Encrypted Message')
 label2.config(font=('Times New Roman',15,'bold'),bg = "azure")
 label2.place(x=85,y=230)

 label3 = Label(widget)
 label3.config(font=('Times New Roman',15,'bold'),bg = "azure")
 label3.place(x=85,y=280)


 label4 =Label(widget,text='Encryption Mode')
 label4.config(font=('Times New Roman',25,'bold'))
 label4.place(x=80,y=35)
 if button2:
  button2.place_forget()
 if button1:
  button1.place_forget()
 label = Label(widget,font=('Times New Roman',23,'bold'))
 

#_____________________________________________ DECRYPT ____________________________________________________#


def decrypt ():
 global plain_text
 cipher_text = entry.get()
 plain_text = ""

 for letter in cipher_text :
   if letter in key:
    index = key.index(letter)
    plain_text += chars[index]
   else:
    plain_text+=letter
 label3.config(text=plain_text)


#_____________________________________________ THE NEW GUI2 ___________________________________________________#


def open_window():
 global label4
 global label2
 global label3
 global button4
 global entry
 global label1
 label1 = Label(widget,text='Enter to decrypt :')
 label1.config(font=('Times New Roman',15,'bold'),bg = "azure")
 label1.place(x=10,y=100)
 entry = Entry(widget,width=18,font=('Arial',15))
 entry.place(x=175,y=100)

 button4 = Button(widget,text='Submit')
 button4.config(font=('Times New Roman',15,'bold'),bg='azure',activebackground='azure',command=decrypt)
 button4.place(x=165,y=160)

 label2 = Label(widget,text='The Decrypted Message')
 label2.config(font=('Times New Roman',15,'bold'),bg = "azure")
 label2.place(x=85,y=230)

 label3 = Label(widget)
 label3.config(font=('Times New Roman',15,'bold'),bg = "azure")
 label3.place(x=85,y=280)
 label3.config(text=plain_text)
 
 label4 =Label(widget,text='Decryption Mode')
 label4.config(font=('Times New Roman',25,'bold'))
 label4.place(x=80,y=35)
 if button2:
  button2.place_forget()
 if button1:
  button1.place_forget()
 label = Label(widget,text="ENCRYPTION",font=('Times New Roman',23,'bold'))

#_____________________________________________ GO BACK ___________________________________________________#

def back():
 if label4 :
  label4.place_forget()
 if label2 :
  label2.place_forget()
 if label3 :
  label3.place_forget()
 if label1: 
  label1.place_forget()
 if button4:
  button4.place_forget()
 if entry:
  entry.place_forget()
 widget.geometry("400x400")
 widget.title("CipherVault")
 icon = PhotoImage(file ='icon.png' )
 widget.iconphoto(True,icon)
 widget.config(background='azure')
 Second_button()
 First_button()


#_____________________________________________ BACK BUTTON ___________________________________________________#

button3 = Button(widget,text='←')
button3.config(font=('Times New Roman',15,'bold'),bg = '#9bbdb3',activebackground = '#9bbdb3',width = 2,height = 1,command = back)
button3.place(x=10,y=10)




First_button()
Second_button()
widget.mainloop()




  














