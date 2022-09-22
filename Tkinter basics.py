#GUI testing
import time
import tkinter as tk#insted of typing Tkinter every time we want to use the library we can just type tk. insted of tkinter. saving us time

#~~~~~~~~~~Basic window~~~~~~~~~~#
root = tk.Tk() #creates an object that is called root
#root.geometry('100x100') #changes the size in pixels of the window. The winodw will auto size if not specified
root.title('hello') #changes the text at the top of the window

#~~~~~~~~~~Label~~~~~~~~~~#
label = tk.Label(root, text='Hello World!') #creates a label called 'label' (creative I know)
label.pack() #packing is when the variable is put into the window in this case label is being packed into root. packing will always place thing in the next free slot

#~~~~~~~~~~Text~~~~~~~~~~#
text = tk.Text(root, height=3) #this makes a text box that is 3 row tall
text.pack() #packs the textbox into the 'root' object

#~~~~~~~~~~Entry~~~~~~~~~~#
entry = tk.Entry(root) #similar to text but is only 1 row tall no matter what
entry.pack() #packs the entry field into root

#~~~~~~~~~~Button~~~~~~~~~~#
button = tk.Button(root, text='Button!')
button.pack()

#~~~~~~~~~~Frames~~~~~~~~~~#
frame = tk.Frame(root) #creates a fram object under root
frame.columnconfigure(0, weight=1) #these 3 commands create a 3x3 grid layout for widgets
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

but1 = tk.Button(frame,text='1') #every single one of these fillowing 9 commands all do the same thing, they just store the button in a specific cell of the frame
but1.grid(row=0,column=0,sticky=tk.W+tk.E) #specifies where on the grid the button will go

but2 = tk.Button(frame,text='2')
but2.grid(row=0,column=1,sticky=tk.W+tk.E)

but3 = tk.Button(frame,text='3')
but3.grid(row=0,column=2,sticky=tk.W+tk.E)

but4 = tk.Button(frame,text='4')
but4.grid(row=1,column=0,sticky=tk.W+tk.E)

but5 = tk.Button(frame,text='5')
but5.grid(row=1,column=1,sticky=tk.W+tk.E)

but6 = tk.Button(frame,text='6')
but6.grid(row=1,column=2,sticky=tk.W+tk.E)

but4 = tk.Button(frame,text='7')
but4.grid(row=2,column=0,sticky=tk.W+tk.E)

but5 = tk.Button(frame,text='8')
but5.grid(row=2,column=1,sticky=tk.W+tk.E)

but6 = tk.Button(frame,text='9')
but6.grid(row=2,column=2,sticky=tk.W+tk.E)

frame.pack(fill='x') #packs everything in the frame object

#~~~~~~~~~~Opening Window~~~~~~~~~~#
root.mainloop() #opens 'root' as a window