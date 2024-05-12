from tkinter import *
import mysql.connector as mc
import tkinter.messagebox
from PIL import ImageTk, Image
from tkinter import messagebox,ttk
from tkinter import font
from datetime import datetime
import random
#for buttons and spins
#----------
clicked=None
hi=None
q=None
spin_1=None
spin_2=None
spin_3=None
total_label=None
notes_entry=None
#----------
def add_items_to_db():
    
    customer_name = txt_customer_name.get()
    contact_number = txt_contact_number.get()
    product_1 = clicked.get()
    product_2 = hi.get()
    product_3 = q.get()
    products_purchased = f"{product_1},{product_2},{product_3}"
    quant_1=spin_1.get()
    quant_2=spin_2.get()
    quant_3=spin_3.get()
    quantities=f"{quant_1},{quant_2},{quant_3}"
    additional_info = notes_entry.get()
    add_customer_query = "INSERT INTO customer_info (customer_name,contact_number,products_purchased,quantities,additional_info)VALUES (%s,%s,%s,%s,%s)"
    customer_data = (customer_name,contact_number,products_purchased,quantities,additional_info)
    try:   
        connection = mc.connect(host ="localhost",user="root",password="",database="pharma_info")
        cursor = connection.cursor()
        cursor.execute(add_customer_query,customer_data)
        connection.commit()
        messagebox.showinfo("Success", "Items added successfully!")
            # Code to update available quantity
        for index, product in enumerate([product_1, product_2, product_3]):
            if product != "Select" and [quant_1, quant_2, quant_3][index]:
                cursor.execute("SELECT avail_quant FROM avail_med WHERE medicine_name = %s", (product,))
                current_avail_quant = cursor.fetchone()[0]
                current_avail_quant = int(current_avail_quant)
                quantity = int([quant_1, quant_2, quant_3][index])
                new_avail_quant = max(0, current_avail_quant - quantity)

                # Update the available quantity in the database
                cursor.execute("UPDATE avail_med SET avail_quant = %s WHERE medicine_name = %s", (new_avail_quant, product))
                connection.commit()
    
    except mc.Error as error:
        print("Error adding items:", error)
        messagebox.showerror("Error", "Failed to add items to the database")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

rates = {
    'ACETAMINOPEN':92,
    'IBUPROFEN':60,
    'ASPIRIN':78,
    'AMOXICILLIN':78,
    'OMEPARAZOLE ':81,
    'METFORMIN':81,
    'SIMVASTATIN':98,
    'LORATADINE':38,
    'DIPHENHYDRAMINE ':38,
    'CETIRIZINE':52,
    'PREDNISONE':72,
    'LISINOPRIL':62,
    'RANITIDINE ':90,
    'ALBUTEROL':98,
    'ATORVASTATINE':48,
    }
def calculate_total():
    quantity_1 = int(spin_1.get())
    quantity_2 = int(spin_2.get())
    quantity_3 = int(spin_3.get())

    product_1 = clicked.get()
    product_2 = hi.get()
    product_3 = q.get()

    rate_1 = rates.get(product_1, 0)
    rate_2 = rates.get(product_2, 0)
    rate_3 = rates.get(product_3, 0)

    total_cost = (quantity_1 * rate_1) + (quantity_2 * rate_2) + (quantity_3 * rate_3)
    total_label.config(text=f"Total Cost: ₹{total_cost}")
    total_label.place(x=650,y=590)


def open_window():    
    entered_username = username.get()
    entered_password = password.get()
    #--------------------------------------------------------------------------------------------------------
    global txt_customer_name,txt_contact_number,clicked,hi,q,spin_1,spin_2,spin_3,total_label,notes_entry
    #---------------------------------------------------------------------------------------------------------
    txt_customer_name=StringVar()
    txt_contact_number=StringVar()
    
    if entered_username == "gugan" and entered_password == "123":
        root1 = Toplevel(root) 
        root1.title("Welcome")
        root1.geometry('10000x10000')
            
        title=Label(root1,text='WELCOME BACK!',bg='purple3',fg='black',font=('times new roman',25,'bold'),relief=GROOVE,bd=12)
        title.pack(fill=X)
        #initializing entry variables
        
        #label of toplevel
       
        date_label = Label(root1, text="", font=('times new roman',18,'bold'))
        date_label.place(x=850, y=150)

        time_label = Label(root1, text="", font=('times new roman',18,'bold'))
        time_label.place(x=1100, y=150)
        def update_datetime():
            
            current_date = datetime.now().date()
            current_time = datetime.now().time().strftime('%H:%M:%S')

            date_label.config(text="Date: " + str(current_date))
            time_label.config(text="Time: " + str(current_time))

            root1.after(1000, update_datetime)

        update_datetime()
        def generate_bill():
            
            product_1 = clicked.get()
            product_2 = hi.get()
            product_3 = q.get()
    
            quantity_1 = int(spin_1.get())
            quantity_2 = int(spin_2.get())
            quantity_3 = int(spin_3.get())

            rate_1 = rates.get(product_1, 0)
            rate_2 = rates.get(product_2, 0)
            rate_3 = rates.get(product_3, 0)

            total_cost_1 = quantity_1 * rate_1
            total_cost_2 = quantity_2 * rate_2
            total_cost_3 = quantity_3 * rate_3
           
                
            total_cost= total_cost_1 + total_cost_2 + total_cost_3
            customer_name = txt_customer_name.get()
            contact_number = txt_contact_number.get()
            quotes=[
               "The greatest wealth is health",
               "Health is wealth.",
	       "Good health, good life.",
	       "Wellness begins within.",
	       "Nourish your body,\n nourish your soul.",
               "Healthy habits, happy life.", 
	       "Fitness is not a destination,\n it’s a journey.",
	       "Invest in your health.",
	       "Healthy mind, healthy life."
	        ]          
            random_quote = random.choice(quotes)
            
            bill_info = f"Name:{customer_name}\n Number:{contact_number}\n\n"\
                        f"Product 1: {product_1} - Quantity: {quantity_1} \n Cost: ₹{total_cost_1}\n" \
                        f"Product 2: {product_2} - Quantity: {quantity_2} \n Cost: ₹{total_cost_2}\n" \
                        f"Product 3: {product_3} - Quantity: {quantity_3} \n Cost: ₹{total_cost_3}\n" \
                        f"Total Cost: ₹{total_cost}\n "\
                        f"Thank You: \"{random_quote}\"\n" \
               

            f2=LabelFrame(root1,text='BILLING SECTION',font=('times new roman',18,'bold'),relief=GROOVE,bd=10,bg='purple',fg='black')
            f2.place(x=900, y=270,width=600,height=500)
            bill_label = Label(f2, text = bill_info, font=('Dubai Medium', 15, 'bold'),relief=GROOVE,bd=10,bg='black',fg='white')
            bill_label.pack()
        
        def show_contact_details():
            
            contact_info = "MAILID:Goodwillpharma@gmail.com\nPHONE:+91 9087858548"
            messagebox.showinfo("Contact Information", contact_info)
        contact_button = Button(root1, text='CONTACT INFO', font='arial 15 bold', padx=15, pady=8, bg='goldenrod2', fg='black', relief=RAISED, bd=10, width=10, command=show_contact_details)
        contact_button.place(relx=0.03, rely=0.7)
        Label(root1,text='Customer Details',font=('times new roman',18,'bold'),relief=GROOVE,bd=10,bg='purple3',fg='black').place(x=0,y=80,relwidth=1)

        lbl=Label(root1,text='Customer Name',font=('times new roman',18,'bold'),relief=SUNKEN,bd=5,bg='purple3',fg='white').place(x=50,y=150)
        txt_customer_entry=Entry(root1,width=15,textvariable=txt_customer_name,font='arial 15 bold',relief=SUNKEN,bd=5,).place(x=250,y=150)
        
        lb2=Label(root1,text='Phone Number',font=('times new roman',18,'bold'),relief=SUNKEN,bd=5,bg='purple3',fg='white').place(x=450,y=150)
        txt_contact_entry=Entry(root1,width=15,textvariable=txt_contact_number,font='arial 15 bold',relief=SUNKEN,bd=5,).place(x=650,y=150)

        Label(root1,text='Product Details',font=('times new roman',18,'bold'),relief=GROOVE,bd=10,bg='purple3',fg='black').place(x=0,y=200,relwidth=1)
        total_label = Label(root1, text="", font=('times new roman', 18, 'bold'))
        total_label.place(x=850, y=400)

        note_label = Label(root1, text='Additional Notes:', font=('times new roman', 18, 'bold'))
        note_label.place(x=50, y=500)

        notes_entry = Entry(root1, width=50, font='arial 15 bold', relief=SUNKEN, bd=5)
        notes_entry.place(x=250, y=500)

        calculate_button = Button(root1, text='Calculate Total', font=('times new roman', 18, 'bold'), relief=RAISED, bd=10, bg='goldenrod2', fg='black', command=calculate_total)
        calculate_button.place(x=50, y=400)

        #combo-1
        
        
        Label(root1,text='Medicine Name -1:',font=('times new roman',18,'bold'),relief=SUNKEN,bd=5,bg='purple3',fg='white').place(x=50,y=250)
        clicked=StringVar()
        clicked.set('Select')
        
        options=[
        'ACETAMINOPEN',
	'IBUPROFEN',
	'ASPIRIN',
	'AMOXICILLIN',
	'OMEPARAZOLE ',
	'METFORMIN',
	'SIMVASTATIN',
	'LORATADINE',
	'DIPHENHYDRAMINE ',
	'CETIRIZINE',
	'PREDNISONE',
        'LISINOPRIL',
        'RANITIDINE ',
        'ALBUTEROL',
        'ATORVASTATINE',
        ]
        c=ttk.Combobox(root1,textvariable=clicked,values=options,width=15,state='readonly')
        c.place(x=300,y=250)
        bold_font = font.Font(weight='bold')
        c['font']=bold_font
        
        Label(root1,text='Quantity',font=('times new roman',18,'bold'),relief=SUNKEN,bd=5,bg='purple3',fg='white').place(x=500,y=250)
                                                                                                                               
        spin_1 = Spinbox(root1,from_=1 , to = 100,width=20)
        spin_1.place(x=630,y=250)
        #next combo-1
        
        Label(root1,text='Medicine Name -2:',font=('times new roman',18,'bold'),relief=SUNKEN,bd=5,bg='purple3',fg='white').place(x=50,y=300)
        hi=StringVar()
        hi.set('Select')
        a=ttk.Combobox(root1,textvariable=hi,values=options,width=15,state='readonly')
        a.place(x=300,y=300)
        bold_font = font.Font(weight='bold')
        a['font']=bold_font

        Label(root1,text='Quantity',font=('times new roman',18,'bold'),relief=SUNKEN,bd=5,bg='purple3',fg='white').place(x=500,y=295)
                                                                                                                               
        spin_2 = Spinbox(root1,from_=1 , to = 100,width=20)
        spin_2.place(x=630,y=295)
        #next combo-2

        Label(root1,text='Medicine Name -3:',font=('times new roman',18,'bold'),relief=SUNKEN,bd=5,bg='purple3',fg='white').place(x=50,y=350)
        q=StringVar()
        q.set('Select')
        b=ttk.Combobox(root1,textvariable=q,values=options,width=15,state='readonly')
        b.place(x=300,y=350)
        bold_font = font.Font(weight='bold')
        b['font']=bold_font
        b.insert(0,"Availability")

        Label(root1,text='Quantity',font=('times new roman',18,'bold'),relief=SUNKEN,bd=5,bg='purple3',fg='white').place(x=500,y=340)
                                                                                                                               
        spin_3 = Spinbox(root1,from_=1 , to = 100,width=20)
        spin_3.place(x=630,y=340)
        save_button = Button(root1,text='SAVE INFO', font=('times new roman',18,'bold'),relief=RAISED, bd=10,bg='goldenrod2', fg='black',command=add_items_to_db).place(x=350,y=400)
        Button(root1,text='EXIT', font=('times new roman',18,'bold'),relief=RAISED, bd=10,bg='goldenrod2', fg='black',command=printing).place(x=650,y=400)
       
        
    
        bill=Button(root1,text='Generate Bill', font=('times new roman',18,'bold'),relief=RAISED,padx=4, pady=8, bd=10,bg='goldenrod2', fg='black',command=generate_bill)
        bill.place(relx=0.22 , rely=0.7)
        
    else:
        
        tkinter.messagebox.showerror("ACCESS DENIED!", "Invalid username or password")


root = Tk()
root.geometry('10000x10000')
root.title("PHARMACY MANAGEMENT SYSTEM")


# Load image
url = ImageTk.PhotoImage(Image.open(r"C:\Users\gugan\Downloads\pharmaa.png"))
l1 = Label(root, image=url)
l1.place(x=0, y=0)
f1=LabelFrame(root,text='welcome',font="Algerian 25 bold",bg='grey60',relief=SUNKEN,bd=10)
f1.place(x=450,y=280,width=600,height=350)

title=Label(root,text='BEWELL PHARMACY LOGIN PAGE🏥',bg='grey60',fg='black',font=('times new roman',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)
# Label details
Label(f1, text='USERNAME:', bg='purple3', fg='white', font="Calibri", padx=5, pady=5, relief=SUNKEN, bd=10, width=12).place(relx=0.08, rely=0.2)
Label(f1, text='PASSWORD:', bg='purple3', fg='white', font="Calibri", padx=5, pady=5, relief=SUNKEN, bd=10, width=12).place(relx=0.08, rely=0.5)

# Entry details
username = Entry(f1, width=20, bg='white', fg='black', font="Calibri", relief=SUNKEN, bd=10)
username.place(relx=0.4, rely=0.2)
password = Entry(f1, width=20, bg='white', fg='black', font="Calibri", relief=SUNKEN, bd=10)
password.place(relx=0.4, rely=0.5)
password.config(show="*")

def printing():
    if tkinter.messagebox.askokcancel("Warning","Are you sure that you want to exit "):
        root.destroy()


# Button details
Button(f1, text='LOGIN', font='arial 15 bold', bg='purple3', fg='black', relief=SUNKEN, bd=8,height=0, width=5,command=open_window).place(relx=0.1, rely=0.8)
Button(f1, text='EXIT', font='arial 15 bold', bg='purple3', fg='black', relief=SUNKEN, bd=8,height=0, width=5,command=printing).place(relx=0.5, rely=0.8)





root.mainloop()

 
