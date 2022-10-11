import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog


def noOfwords():
    with open("word.txt", "r") as Words:
        words = Words.read()
        list = words.split(" ")
        del list[-1]
        list.sort(key = len, reverse = True)
        noOf = len(list)

    messagebox.showinfo("Number Of Words", noOf)


# method to find the Longest Word in the file
def longestWord():
    with open("word.txt", "r") as Words:
        words = Words.read()
        list = words.split(" ")
        del list[-1]
        list.sort(key=len, reverse=True)
    #max_word = len(max(list, default="", key=len))
    #max_word1= [word for word in words if len(word) == max_word]
    messagebox.showinfo("Longest Of Words", list[0])



# method to find the Average length of each Word in the file
def avgLen():
    with open("word.txt", "r") as Words:
        words = Words.read()
        list = words.split(" ")
        del list[-1]
        list.sort(key=len, reverse=True)
        length = 0
        for i in list:
            length += len(i)
        avgLen = length / len(list)


        messagebox.showinfo("The Average Length Of words", avgLen)

counterWindow = tkinter.Tk()
counterWindow.title("Words Counter In a File")
counterWindow.geometry("350x280+300+300")
        #Number Of words Display button  and Entry
        #self.noOfwords_entry = tkinter.Entry(width=20)
noOfwords_button = tkinter.Button(text='Number Of Words',bg='black',fg= 'white', command=noOfwords)
        #self.noOfwords_entry.pack(side='left')
noOfwords_button.grid(column=0, row=0, sticky=W, padx=5, pady=5)


        #Longest Word In the file button and entry
        #self.longestWord_entry = tkinter.Entry(width=20)
longestWord_button = tkinter.Button(text='Longest Word', bg='black',fg= 'white', command=longestWord)
        #self.longestWord_entry.pack(side='left')
longestWord_button.grid(column=1, row=0, sticky=W, padx=5, pady=5)


        #Average Length of words in the file button and entry
        #self.avgLen_entry = tkinter.Entry(width=20)
avg = Label(text="", font=('Calibri 15'))
avg.grid(column=2, row=0, sticky=W, padx=5, pady=5,)
#avg.pack()
avgLen_button = tkinter.Button(text='Average Length',bg='black',fg= 'white', command=avgLen)
        #self.avgLen_entry.pack(side='left')
avgLen_button.grid(column=3, row=0, sticky=W, padx=5, pady=5)


tkinter.mainloop()

