from tkinter import *
import tkinter.messagebox as box

def tog():
	if window.cget('bg')=='yellow':
		window.configure(bg='gray')
	else:
		window.configure(bg='yellow')
	var = box.askyesno('Message Box','Proceed? '+book.get())
	if var==1:
		box.showinfo('Yes Box','Proceeding...'+listbox.get(listbox.curselection()))
	else:
		box.showwarning('No Box','Cancelling...'+entry.get())
	
	
window=Tk()
window.title('Label example')
label = Label(window,text='Hello World!')
label.pack(padx=200,pady=10)
label.configure(text='Hello, World!!!')

btn_end = Button(window, text="Close",command=exit)
btn_end.pack(padx=150,pady=20)

btn_color = Button(window, text="Color",command=tog)
btn_color.pack(padx=150,pady=30)

frame = Frame(window)
entry = Entry(frame)
frame.pack(padx=150,pady=40)
entry.pack(side=LEFT)

# Listbox -------------------------------------
frame1 = Frame(window)
frame1.pack(padx=150,pady=50)
listbox = Listbox(frame1)
listbox.insert(1,'var 1')
listbox.insert(2,'var 2')
listbox.insert(3,'var 3')
listbox.pack(side=LEFT)

# Radiobuttons ----------------------------------
book = StringVar()
r1=Radiobutton(frame1,text='v1',variable=book,value='v1')
r2=Radiobutton(frame1,text='v2',variable=book,value='v2')
r3=Radiobutton(frame1,text='v3',variable=book,value='v3')
r2.select()

r1.pack(side=RIGHT)
r2.pack(side=RIGHT)
r3.pack(side=RIGHT)

# Checkbuttons ----------------------------------
frame2 = Frame(window)
frame2.pack(padx=150,pady=60)
v1=IntVar()
v2=IntVar()
b1=Checkbutton(frame2,text='text1',variable=v1,onvalue=1,offvalue=0)
b2=Checkbutton(frame2,text='text2',variable=v2,onvalue=1,offvalue=0) 
b1.pack(side=LEFT)
b2.pack(side=LEFT)

window.mainloop()
