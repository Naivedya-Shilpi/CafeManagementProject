import tkinter as tk # importing tkinter
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox

#main window
root=tk.Tk() 
root.title("cafe menu") # it gives window a title 
window_width = 1000 
window_height = 600
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
centre_x=int(screen_width/2-window_width/2)
centre_y=int(screen_height/2-window_height/2)
root.geometry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')
root.iconbitmap("C:/Users/Parija Sharma/.vscode/tkinter/coffee.ico") #this displays icon of your window
root.config(bg="#CFBCA3") 
#heading label
heading_label=tk.Label(root,text="CAFE MANAGEMENT SYSTEM",
                       font=("Georgia",26,"bold"),
                       anchor="center",
                       fg="#654321",
                       relief="raised",
                       bd=10) #this is main heading of window
heading2_label=tk.Label(root,text="-------------------Our cafe's best seller--------------------",
                        font=("Monotype Corsiva",16,"bold"),
                        anchor="center",
                        fg="#654321",
                        bg="#CFBCA3")
heading_label.grid(row=0,column=0,columnspan=7,pady=10)
heading2_label.grid(row=1,column=0,columnspan=7,pady=10)

#best seller panel
image_paths=[
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/Screenshot_20-10-2024_122333_www.bing.com.jpeg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/Frappe-Coffee.jpg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/brownie.jpeg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/burger.jpeg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/expresso.jpeg",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/pizza.webp",
    "C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/doughnuts.jpg",
]

captions={
    "Cinnemon Roll":120,
            "Frappe Coffee":150,
            "Brownie":150,
            "Burger":80,
            "Espresso":150,
            "Pizza":260,
            "Doughnuts":85}

selected_items=[]
image_objects=[]
total_price=0


def button_click(caption):
    global total_price
    price=captions[caption]
    selected_items.append((caption,price))
    total_price+=price

    cart_listbox.insert(tk.END, f"{caption} - Rs {price}")
    update_total()
    total_label.config(text=f"total : Rs{total_price}")

    
# Display images in a grid 
for index,path in enumerate(image_paths):
    try:
        img=Image.open(path).resize((100,100),Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        image_objects.append(img)
    except Exception as e:
        print(f"Error loading image at{path}:{e}")
        continue

#buttons with their respective pictures:
 
    my_button=ttk.Button(root,image=img,command=lambda c=list(captions.keys())[index]:button_click(c))
    my_button.grid(row=2,column=index,padx=35 , pady=10)
#Display the caption under each image
    caption_label=tk.Label(root,text=list(captions.keys())[index],font=("Monotype Corsiva",12,"bold"))
    caption_label.grid(row=3,column=index,padx=35,pady=10)


beveragemenu={
    'Espresso': 150,
    'Cappuccino': 100,
    'Latte': 120,
    'Americano': 120,
    'Frappe Coffee': 150,
    'Hot Chocolate': 50,
    'Iced Latte': 120,
    'Cold Brew': 100,
    'Tea': 100,
    'Fresh Lemonade': 80
    }
foodmenu={
    'Avocado Toast': 120,
    'Breakfast Sandwich (egg, cheese, bacon)': 120,
    'Veggie Wrap': 80,
    'Grilled Cheese': 100,
    'Caesar Salad': 200,
    'Burger': 80,
    'Pizza': 260,
    "Doughnuts":85,
    "Brownie":150,
    "Cinnemon Roll":120,
    }

selected_items=[]

def add_item():
    item=menu_combo.get().strip()
    if item:
        price=beveragemenu.get(item)
        if price is not None:
            selected_items.append((item,price))
            cart_listbox.insert(tk.END,f"{item}- Rs{price}")
            update_total()
        else:
             print("item not found")
      
def add_item2():
    item=menu2_combo.get().strip()
    if item:
        price=foodmenu.get(item)
        if price is not None:
            selected_items.append((item,price))
            cart_listbox.insert(tk.END,f"{item}- Rs{price}")
            update_total()
        else:
            print("item not found")
      

def update_total():
    global total_price
    total_price=sum(price for __, price in selected_items)
    total_label.config(text=f"total : Rs{total_price}")

# Billing system to display detailed bill
def generate_bill():
    if selected_items:
        bill = "\n".join([f"{item}: Rs {price}" for item, price in selected_items])
        total_price = sum(price for _, price in selected_items)
        bill += f"\n\nTotal: Rs {total_price}"
        messagebox.showinfo("Bill", f"--- Your Bill ---\n\n{bill}")
    else:
        messagebox.showwarning("Empty Cart", "Your cart is empty. Please add items to the cart.")

# Widgets for the GUI


add_label=tk.Label(root,text="Select an item",font=("Bookman Old Style",12,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=5)
add_label.grid(row=9,column=0,padx=20,pady=5)

menu_combo=ttk.Combobox(root,values=list(beveragemenu.keys()))
menu_combo.grid(row=10,column=0,padx=20,pady=5)

add_button=tk.Button(root,text="add to cart",command=add_item,font=("Bookman Old Style",10,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=4)
add_button.grid(row=11,column=0,padx=20,pady=5)

add2_label=tk.Label(root,text="Select an item",font=("Bookman Old Style",12,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=5)
add2_label.grid(row=9,column=1,padx=20,pady=5)

menu2_combo=ttk.Combobox(root,values=list(foodmenu.keys()))
menu2_combo.grid(row=10,column=1,padx=20,pady=5)

add2_button=tk.Button(root,text="add to cart",command=add_item2,font=("Bookman Old Style",10,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=4)
add2_button.grid(row=11,column=1,padx=20,pady=5)

cart_listbox=tk.Listbox(root,width=30,height=5) 
cart_listbox.grid(row=12,column=0,padx=20,pady=20,columnspan=2)
total_label=tk.Label(root,text="Total: Rs 0.00",width=15,font=("Bookman Old Style",10,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=4)
total_label.grid(row=13,column=0,padx=20,pady=20,columnspan=2)

qr_label=tk.Label(root,text="scan qr code to see menu",font=("Bookman Old Style",10,"bold"),fg="#4A0909",bg="#E8B878",relief="groove",bd=3)
qr_label.grid(row=13, column=2,padx=20,pady=20)

qr_img= Image.open("C:/Users/Parija Sharma/OneDrive/Desktop/tkinter/menu.png").resize((100,100),Image.LANCZOS)
qr_img =ImageTk.PhotoImage(qr_img)

qr_label_img = tk.Label(root, image=qr_img,font=("Bookman Old Style",10,"bold"),fg="#4A0909",bg="#E8B878",relief="raised",bd=4)
qr_label_img.grid(row=12, column=2, padx=20, pady=20)

# Button to generate bill
bill_button = tk.Button(root, text="Generate Bill", command=generate_bill, font=("Bookman Old Style", 12, "bold"), fg="#4A0909", bg="#E8B878", relief="raised", bd=5)
bill_button.grid(row=14, column=0, columnspan=2, pady=20)
root.mainloop()