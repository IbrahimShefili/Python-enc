# Lazımlı modulların import edilməsi
import base64
from base64 import encode
from tkinter import *
from tkinter import messagebox

# Proqram pəncərəsinin dizaynı
container = Tk()
container.geometry('600x600')
container.title('Base32 Encode and Decode')
container.config(background='#88cffa')

# Dəyişənlərin elanı
message_text = StringVar()
smessage = StringVar()
choice = StringVar()

# Lazimi textbox və butonların yaradılması
label1 = Label(container, text="BASE32 ENCODE & DECODE", font='helvetica 16 bold', background='#88cffa').pack(padx=80, pady=20)
label2 = Label(container, text="Enter Message: ", font='helvetica 14 bold', background='#88cffa').place(x=100, y=120)
entry1 = Entry(container, font='helvetica 14 italic', textvariable=message_text, disabledbackground='black',background='white').place(x=275, y=120)
label5 = Label(container, text="Select Mode: ", font='helvetica 14 bold', background='#88cffa').place(x=100, y=175)
entry4 = Entry(container, font='helvetica 14 italic', textvariable=choice, disabledbackground='black',background='white').place(x=275, y=175)
label6 = Label(container, text="(Enter 'e' for 'encode' and 'd' for 'decode')", font='helvetica 11 italic', background='#88cffa').place(x=100, y=220)
button1 = Button(container, text="SHOW RESULT", font='helvetica 14 bold', background='#88cffa', command=lambda:choice_data()).place(x=220, y=260)
label4 = Label(container, text="Resulting Text: ", font='helvetica 14 bold', background='#88cffa').place(x=90, y=325)
entry3 = Entry(container, font='helvetica 14 italic', textvariable=smessage, disabledbackground='black',background='white').place(x=250, y=325)
button3 = Button(container, text="RESET", font='helvetica 14 bold', background='#88cffa', command=lambda:reset_data()).place(x=255, y=375)

# Reset butonuna basdıqda nə baş verəcəyinin bəlirləyən funksiya
def reset_data():
    message_text.set("--")
    smessage.set("--")
    choice.set("--")

# Seçimdən aslı olaraq datanın şifrələnəcəyini yaxud deşifrələnəcəyini müəyyən edən funksiya
def choice_data():
    if choice.get() in ("e", "E"):
        smessage.set(encode_data(message_text.get()))
    elif choice.get() in ("d", "D"):
        smessage.set(decode_data(message_text.get()))
    else:
        messagebox.showerror("Check Validity", "Try Again")

# Məlumatın şifrələnməsini həyata keçirən funksiya
def encode_data(message_string):
    message_string_text = message_string.encode("cp437")
    message_base = base64.b32encode(message_string_text) 
    return (message_base)

# Məlumatın deşifrələnməsini həyata keçirən funksiya
def decode_data(message_string):
    message_string_text = message_string.encode("cp437")
    decode_string = base64.b32decode(message_string_text)
    return (decode_string)

# Pəncərənin davamlı olaraq ekran görsənməsini həyata keçirmək üçün onun frame-ini loopa salırıq pənəcərə istifadəçi close-a basana qədər ekranda qalacaq 
container.mainloop()