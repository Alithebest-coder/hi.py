from tkinter import*

window=Tk()

window.title("bob jr and droco jr")

window.geometry("500x500")
label=Label(text="Hi I am bob jr and this is droco jr and we are friends")

label.pack()

label2=Label(text="what is your name?")
label2.pack()
entry=Entry()
entry.pack()
button=Button(text=" a friendship was made")
button.pack()
window.mainloop()