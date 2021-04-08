from tkinter import *

window = Tk()

# top gui programing.  Label and entry numbers match.
# I really don't know what i'm doing please be kind

label1=Label(window, text="Title")
label1.grid(row=0, column=0)

title_input=StringVar()
entry1=Entry(window, textvariable=title_input, width=20)
entry1.grid(row=0, column=1)

label2=Label(window, text="Author")
label2.grid(row=0, column=2)

author_input=StringVar()
entry2=Entry(window, textvariable=author_input, width=20)
entry2.grid(row=0, column=3)

label3=Label(window, text="Year")
label3.grid(row=1, column=0)

year_input=StringVar()
entry3=Entry(window, textvariable=year_input, width=20)
entry3.grid(row=1, column=1)

label4=Label(window, text="ISBN")
label4.grid(row=1, column=2)

ISBN_input=StringVar()
entry4=Entry(window, textvariable=ISBN_input,width=20)
entry4.grid(row=1, column=3)

# list box
listbox1 = Listbox(window, height=6, width=35)
listbox1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll1=Scrollbar(window)
scroll1.grid(row=2, column=2, rowspan=6)

listbox1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=listbox1.yview)

# function buttons
button1=Button(window, text="View All", width=10)
button1.grid(row=2,column=3)

button2=Button(window, text="Search Entry",  width=10)
button2.grid(row=3,column=3)

button3=Button(window, text="Add Entry",  width=10)
button3.grid(row=4,column=3)

button4=Button(window, text="Update",  width=10)
button4.grid(row=5,column=3)

button5=Button(window, text="Delete",  width=10)
button5.grid(row=6,column=3)

button6=Button(window, text="Close",  width=10)
button6.grid(row=7,column=3)

window.mainloop()