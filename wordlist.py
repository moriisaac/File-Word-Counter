import tkinter
from  tkinter import *


def words_write():

        # enter the words
        try:
            noOfwords = int(noOfwords_entry.get())
            for num in range(noOfwords) :
                with open("word.txt", "w") as words:
                 words_enter = words_entry.get()

                 #dict = (words_enter)
                 words.write(words_enter + " ")
                 answer.config(text="Words Written Successfully!😊")

        except ValueError:
            answer.config(text="Invalid input! Try Again😪")

    # create Main Window
main_window = tkinter.Tk()
main_window.title("Word List Tracker")
main_window.geometry("500x280+300+300")

noOfwords_label = tkinter.Label(main_window,text='Enter number of words You Would like To write in a file:')
noOfwords_entry = tkinter.Entry(main_window,width=20)

noOfwords_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)
noOfwords_entry.grid(column=1, row=0, sticky=W, padx=5, pady=5)

words_label = tkinter.Label(text='Enter The words :')
words_entry = tkinter.Entry(main_window,width=20)

words_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)
words_entry.grid(column=1, row=1, sticky=W, padx=5, pady=5)

answer = tkinter.Label(main_window,text='')
answer.grid(column=1, row=2, sticky=W, padx=5, pady=5)
         #Create Navigation Button to the other window
word_button = tkinter.Button(main_window,text='Store Words Written', command=words_write)
word_button.grid(column=0, row=2, sticky=W, padx=5, pady=5)
tkinter.mainloop()
