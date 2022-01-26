'''GUI #1: Schedule input data from user.'''

'''Imports'''
import tkinter
from tkinter import *
from PIL import ImageTk, Image

'''Window Settings'''
def booking_info():
    info_window = Tk()
    info_window.title("Booking Information")
    info_window.geometry("400x400")
    info_window.configure(bg='lightblue')

    logo = ImageTk.PhotoImage(Image.open('hymussportslogo.png'))
    logo_label = Label(image=logo).pack()

    booking_name = Label(info_window, text = "Enter Customer Name:").pack()
    entry1 = Entry(info_window, width=60)
    entry1.pack()

    phone_num = Label(info_window, text = "Enter Phone Number:").pack()
    entry2 = Entry(info_window, width=60)
    entry2.pack()

    start_time = Label(info_window, text = "Enter Start Time:").pack()
    entry3 = Entry(info_window, width=60)
    entry3.pack()

    end_time = Label(info_window, text = "Enter End Time:").pack()
    entry4 = Entry(info_window, width=60)
    entry4.pack()

    note_box = Label(info_window, text = "Enter Note:").pack()
    entry5 = Entry(info_window, width=60)
    entry5.pack()

    '''Information Getter'''
    def get_booking_info():
        
        with open("bookingDataStorage.txt", "w") as f:
            f.write(entry1.get())
            f.write("\n")
            f.write(entry2.get())
            f.write("\n")
            f.write(entry3.get())
            f.write("\n")
            f.write(entry4.get())
            f.write("\n")
            f.write(entry5.get())
            f.write("\n")
        f.close()
        info_window.quit()
        
    finish = Button(info_window, text="Click to complete booking.", command=get_booking_info).pack()
    cancel = Button(info_window, text="Cancel", command=info_window.quit).pack()
    info_window.mainloop()

if __name__ == "__main__":
    booking_info()