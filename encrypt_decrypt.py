# python module for one-timepad
import onetimepad
# python module to create GUI		
import tkinter
# from tkinter import *

		
root = Tk()
root.title("CRYPTOGRAPHY")
root.geometry("600x200")

def encryptMessage():					
	pt = e1.get()

	# inbuilt function to encrypt a message
	ct = onetimepad.encrypt(pt, 'random')
	e2.delete(0, tkinter.END) 
	e2.insert(0, ct)

def decryptMessage():					
	ct1 = e3.get()

	# inbuilt function to decrypt a message
	pt1 = onetimepad.decrypt(ct1, 'random')
	e4.delete(0, tkinter.END)
	e4.insert(0, pt1)
	
# creating labels and positioning them on the grid
label1 = Label(root, text ='Plain text',font="Arial 15 bold")			
label1.grid(row = 10, column = 1)
label2 = Label(root, text ='Encrypted text',font="Arial 15 bold")
label2.grid(row = 11, column = 1)
l3 = Label(root, text ="Cipher text",font="Arial 15 bold")
l3.grid(row = 10, column = 10)
l4 = Label(root, text ="Decrypted text",font="Arial 15 bold")
l4.grid(row = 11, column = 10)

# creating entries and positioning them on the grid
e1 = Entry(root)
e1.grid(row = 10, column = 2)
e2 = Entry(root)
e2.grid(row = 11, column = 2)
e3 = Entry(root)
e3.grid(row = 10, column = 11)
e4 = Entry(root)
e4.grid(row = 11, column = 11)

# creating encryption button to produce the output
ent = Button(root, text = "encrypt", bg ="red", fg ="white",font="Arial 15 bold", command = encryptMessage)
ent.grid(row = 13, column = 2)

# creating decryption button to produce the output
b2 = Button(root, text = "decrypt", bg ="green", fg ="white",font="Arial 15 bold", command = decryptMessage)
b2.grid(row = 13, column = 11)


root.mainloop()
