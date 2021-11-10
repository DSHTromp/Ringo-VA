from tkinter import *
import tkinter.messagebox
import sqlite3
from PIL import Image, ImageTk

def main():
    window = Tk()
    window.geometry("420x240")
    window.title("Registration")

    img = Image.open("C:/Users/daant/PycharmProjects/Eindwerkstuk-P3.6/Skin/Settings/istockphoto-1146311489-612x612.png")
    photo = ImageTk.PhotoImage(img)

    fn = StringVar()
    ln = StringVar()
    zc = StringVar()
    var = StringVar()


    def database():
        name1 = fn.get()
        last1 = ln.get()
        zip1 = zc.get()
        count1 = var.get()
        conn = sqlite3.connect("Form.db")
        with conn:
            cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS productregistration (Name TEXT, Last TEXT, Zipcode TEXT, Country TEXT)')
        cursor.execute('INSERT INTO productregistration (Name, Last, Zipcode, Country) VALUES(?,?,?,?)',
                       (name1, last1, zip1, count1))
        conn.commit()

        first = fn.get()
        sec = ln.get()
        zipc = zc.get()
        country = var.get()
        print(f"your Fullname is {first} {sec}")
        print(f"your zip code is {zipc}")
        print(f"your country is {country}")
        tkinter.messagebox.showinfo("Registration", 'User is successfully registered')


    def exitt():
        exit()


    lab = Label(image=photo)
    lab.place(x=240, y=60)

    label1 = Label(window, text="Registration", fg='White', bg='Black', font=("arial", 16, "bold")).pack()

    label2 = Label(window, text="This product contains copyrighted scrips by VSZ",
                    width=40, font=("arial", 12, "bold")).place(x=10, y=30)

    label3 = Label(window, text="First Name:", font=("arial", 12,)).place(x=10, y=60)
    entry_1 = Entry(window, textvar=fn)
    entry_1.place(x=100, y=64)

    label4 = Label(window, text="Last Name:", font=("arial", 12,)).place(x=10, y=90)
    entry_2 = Entry(window, textvar=ln)
    entry_2.place(x=100, y=94)

    label5 = Label(window, text="zip code:", font=("arial", 12,)).place(x=10, y=120)
    entry_3 = Entry(window, textvar=zc)
    entry_3.place(x=100, y=124)

    label6 = Label(window, text="Country:", font=("arial", 12,)).place(x=10, y=150)

    list1 = ['Netherlands', 'Germany', 'France', 'Belgium']
    droplist = OptionMenu(window, var, *list1)
    var.set("select Country")
    droplist.config(width=14)
    droplist.place(x=96, y=150)

    but_back = Button(window, text="Back", width=12, bg='brown', fg='white', command=exitt).place(x=50, y=185)

    but_next = Button(window, text="signup", width=12, bg='brown', fg='white', command=database).place(x=176, y=185)
    window.bind("<Return>", database)

    window.mainloop()


if __name__ == '__main__':
    main()