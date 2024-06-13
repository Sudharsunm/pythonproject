#Importing the required modules
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import mysql.connector


db=mysql.connector.connect(user="root",passwd="passw0rd",host="localhost") 
 
my_cursor=db.cursor() #getting the cursor object
my_cursor.execute("CREATE DATABASE IF NOT EXISTS Shop") #creating the database named library

db=mysql.connector.connect(user="root",passwd="passw0rd",host="localhost",database='Shop') 
my_cursor=db.cursor()
query="CREATE TABLE IF NOT EXISTS products (date VARCHAR(10),prodName VARCHAR(20), prodPrice VARCHAR(50))"
my_cursor.execute(query) #executing the query

db=mysql.connector.connect(user="root",passwd="passw0rd",host="localhost",database='Shop') 
my_cursor=db.cursor()
query="CREATE TABLE IF NOT EXISTS sale (custName VARCHAR(20), date VARCHAR(10), prodName VARCHAR(30),qty INTEGER, price INTEGER )"
my_cursor.execute(query) #executing the query

def prodtoTable():
    pname= prodName.get()
    price = prodPrice.get()
    dt = date.get()
    #Connecting to the database
    db=mysql.connector.connect(user="root",passwd="passw0rd",host="localhost",database='Shop') 
    cursor = db.cursor()
    query = "INSERT INTO products(date,prodName,prodPrice) VALUES(%s,%s,%s)"
    details = (dt,pname,price)

    #Executing the query and showing the pop up message
    try:
        cursor.execute(query,details)
        db.commit()
        messagebox.showinfo('Success',"Product added successfully")
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Error","Trouble adding data into Database")
    
    wn.destroy()
#Function to get details of the product to be added
def addProd(): 
    global prodName, prodPrice, date, Canvas1,  wn
    
    #Creating the window
    wn = tkinter.Tk() 
    wn.title("SSSS BAZAAR")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='LightBlue1')
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg='LightBlue1',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add a Product", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Getting Date
    lable1 = Label(labelFrame,text="Date : ", fg='black')
    lable1.place(relx=0.05,rely=0.3, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Product Name
    lable2 = Label(labelFrame,text="Product Name : ", fg='black')
    lable2.place(relx=0.05,rely=0.45, relheight=0.08)
        
    prodName = Entry(labelFrame)
    prodName.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)
        
    # Product Price
    lable3 = Label(labelFrame,text="Product Price : ", fg='black')
    lable3.place(relx=0.05,rely=0.6, relheight=0.08)
        
    prodPrice = Entry(labelFrame)
    prodPrice.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)
           
    #Add Button
    Btn = Button(wn,text="ADD",bg='#d1ccc0', fg='black',command=prodtoTable)
    Btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
    
    Quit= Button(wn,text="Quit",bg='#f7f1e3', fg='black',command=wn.destroy)
    Quit.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()

#Function to remove the product from the database
def removeProd():
    #Getting the product name from the user to be removed
    name = prodName.get()
    name = name.lower()
    
    #Connecting to the database
    db=mysql.connector.connect(user="root",passwd="passw0rd",host="localhost",database='Shop') 
    cursor = db.cursor()
    
    #Query to delete the respective product from the database
    query = "DELETE from products where LOWER(prodName) = '"+name+"'"
   #Executing the query and showing the message box
    try:
        cursor.execute(query)
        db.commit()
        #cur.execute(deleteIssue)
        #con.commit()

        messagebox.showinfo('Success',"Product Record Deleted Successfully")

    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Please check Product Name")
 
    wn.destroy()
#Function to get product details from the user to be deleted
def delProd(): 

    global prodName, Canvas1,  wn
    #Creating a window
    wn = tkinter.Tk() 
    wn.title("SSSS BAZAAR")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg="misty rose")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg="misty rose",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Product", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Product Name to Delete
    lable = Label(labelFrame,text="Product Name : ", fg='black')
    lable.place(relx=0.05,rely=0.5)
        
    prodName = Entry(labelFrame)
    prodName.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Delete Button
    Btn = Button(wn,text="DELETE",bg='#d1ccc0', fg='black',command=removeProd)
    Btn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    Quit = Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()

#Function to show all the products in the database
def viewProds():
    global  wn
    #Creating the window to show the products details
    wn = tkinter.Tk() 
    wn.title("SSSS BAZAAR")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn) 
    Canvas1.config(bg="old lace")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(wn,bg='old lace',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingLabel = Label(headingFrame1, text="View Products", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(wn,bg='old lace')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    #Connecting to the database
    db=mysql.connector.connect(user="root",passwd="passw0rd",host="localhost",database='Shop') 
    cursor=db.cursor()
    #Query to get the product details
    query="Select * from products"
    try:
        cursor.execute(query)
        #Fetching all the records from the database
        result = cursor.fetchall()
        for i in result:
            Label(labelFrame, text="%-10s%-40s%-30s"%(i[0],i[1],i[2]),bg='old lace',fg='black').place(relx=0.07,rely=y)
            y += 0.1
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Failed to fetch files from database")
    
    #Quit button
    Quit = Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()

#Function to generate bill
def bill():
    global Canvas1, wn
    #Creating the window to get customer details for bill generation
    wn = tkinter.Tk() 
    wn.title("SSSS BAZAAR")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg="lavender blush")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(wn,bg='lavender blush',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingLabel = Label(headingFrame1, text="Generate Bill", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(wn,bg='lavender blush')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
        
    # Customer Name
    lable = Label(labelFrame,text="Customer Name : ", bg='lavender blush', fg='black')
    lable.place(relx=0.05,rely=0.2, relheight=0.08)
        
    custName = Entry(labelFrame)
    custName.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Date
    lable2 = Label(labelFrame,text="Date : ", bg='lavender blush', fg='black')
    lable2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
    
    # Adding the fields for products dynamically from the database
    db = mysql.connector.connect(user="root", passwd="passw0rd", host="localhost", database='Shop')
    cursor = db.cursor()
    query = "SELECT prodName FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    
    entries = []
    
    for i, prod in enumerate(products):
        lable3 = Label(labelFrame, text=f"{prod[0]} Quantity:", bg='lavender blush', fg='black')
        lable3.place(relx=0.05, rely=(0.5 + i*0.1), relheight=0.08)
        
        qty = Entry(labelFrame)
        qty.place(relx=0.3, rely=(0.5 + i*0.1), relwidth=0.62, relheight=0.08)
        
        entries.append((prod[0], qty))
        
    def generate_bill():
        name = custName.get()
        dt = date.get()
        items = []
        
        for prod_name, qty_entry in entries:
            qty = qty_entry.get()
            if qty:
                items.append((prod_name, int(qty)))
        
        if not items:
            messagebox.showinfo("Error", "No items added to bill")
            return
        
        # Generating the bill
        db = mysql.connector.connect(user="root", passwd="passw0rd", host="localhost", database='Shop')
        cursor = db.cursor()
        
        total = 0
        bill_details = f"Customer Name: {name}\nDate: {dt}\n\nItems:\n"
        for prod_name, qty in items:
            query = f"SELECT prodPrice FROM products WHERE prodName = '{prod_name}'"
            cursor.execute(query)
            price = cursor.fetchone()[0]
            total_price = int(price) * qty
            total += total_price
            bill_details += f"{prod_name} - {qty} x {price} = {total_price}\n"
            
        bill_details += f"\nTotal: {total}"
        
        # Saving the sale details to the database
        for prod_name, qty in items:
            cursor.execute("INSERT INTO sale (custName, date, prodName, qty, price) VALUES (%s, %s, %s, %s, %s)",
                           (name, dt, prod_name, qty, int(price)))
        db.commit()
        
        messagebox.showinfo("Bill Details", bill_details)
    
    # Generate Bill Button
    Btn = Button(wn, text="Generate Bill", bg='#d1ccc0', fg='black', command=generate_bill)
    Btn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)
    
    Quit = Button(wn, text="Quit", bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)
    
    wn.mainloop()

#Creating the main window
root = tkinter.Tk() 
root.title("SSSS BAZAAR")
root.configure(bg='mint cream')
root.minsize(width=500,height=500)
root.geometry("700x600")

Canvas1 = Canvas(root)
Canvas1.config(bg="powder blue")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="powder blue",bd=5)
headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
headingLabel = Label(headingFrame1, text="Welcome to \n SSSS BAZAAR", fg='grey19', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Product Details",bg='old lace', fg='black',command=addProd)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Delete Product",bg='old lace', fg='black',command=delProd)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="View Products",bg='old lace', fg='black',command=viewProds)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="Generate Bill",bg='old lace', fg='black',command=bill)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()