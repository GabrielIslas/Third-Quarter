from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass
import os

absolute_path = os.path.dirname(__file__)

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Bookstore Inventory Management") #Titulo de la ventana
        self.root.config(bg="white") #color fondo

        #"""TITLE"""
        icon_title_path = "images/book5.png"
        icon_title_full_path = os.path.join(absolute_path, icon_title_path)
        self.icon_title=PhotoImage(file=icon_title_full_path)
        title=Label(self.root, text="Bookstore Inventory Management System", image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"), bg="#c9ab69", fg="black", anchor = "w", padx=20).place(x=0,y=0, relwidth=1, height =70)

        #Sing out
        btn_singout= Button(self.root, text = "Sing out", font=("times new roman", 15, "bold"),).place(x=1180, y= 10, height = 50, width = 150)

        #Clock
        self.lbl_clock=Label(self.root, text="Welcome to the bookstore Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15), bg="#453719", fg="white")
        self.lbl_clock.place(x=0,y=70, relwidth=1, height =30)

        #Left Menu
        MenuLogoPath = "images/librero.png"
        MenuLogoFullPath = os.path.join(absolute_path, MenuLogoPath)
        self.MenuLogo=Image.open(MenuLogoFullPath)
        self.MenuLogo= self.MenuLogo.resize((200,200), Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
       
        LeftMenu = Frame(self.root, bd=2, relief= RIDGE)
        LeftMenu.place(x=0, y=102, width=200, height = 565)

        lbl_menuLogo= Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        icon_side_path = "images/arrow3.png"
        icon_side_full_path = os.path.join(absolute_path, icon_side_path)
        self.icon_side=PhotoImage(file=icon_side_full_path)
        lbl_menu= Label(LeftMenu, text = "Menu", font=("times new roman", 20),bg = "#382d0d", fg="white").pack(side=TOP, fill = X)
       
        btn_employee = Button(LeftMenu, text = "Employee",command= self.employee, image= self.icon_side, compound=LEFT, padx=5, anchor="w" ,font=("times new roman", 20, "bold"),bg = "#f0dfaf", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill = X)
        btn_supplier = Button(LeftMenu, text = "Supplier", image= self.icon_side, compound=LEFT, padx=5, anchor="w" ,font=("times new roman", 20, "bold"),bg = "#f0dfaf", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill = X)
        btn_category = Button(LeftMenu, text = "Category", image= self.icon_side, compound=LEFT, padx=5, anchor="w" ,font=("times new roman", 20, "bold"),bg = "#f0dfaf", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill = X)
        btn_product = Button(LeftMenu, text = "Product", image= self.icon_side, compound=LEFT, padx=5, anchor="w" ,font=("times new roman", 20, "bold"),bg = "#f0dfaf", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill = X)      
        btn_sales = Button(LeftMenu, text = "Sales", image= self.icon_side, compound=LEFT, padx=5, anchor="w" ,font=("times new roman", 20, "bold"),bg = "#f0dfaf", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill = X)
        btn_exit = Button(LeftMenu, text = "Exit", image= self.icon_side, compound=LEFT, padx=5, anchor="w" ,font=("times new roman", 20, "bold"),bg = "#f0dfaf", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill = X)

        #Content
        self.lbl_employee= Label(self.root, text="Total employee\n[ 0 ]", bd= 5, relief= RIDGE, bg = "#c9ab69", fg= "black", font=("times new roman", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier= Label(self.root, text="Total supplier\n[ 0 ]", bd= 5, relief= RIDGE, bg = "#c9ab69", fg= "black", font=("times new roman", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category= Label(self.root, text="Total category\n[ 0 ]", bd= 5, relief= RIDGE, bg = "#c9ab69", fg= "black", font=("times new roman", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product= Label(self.root, text="Total product\n[ 0 ]", bd= 5, relief= RIDGE, bg = "#c9ab69", fg= "black", font=("times new roman", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales= Label(self.root, text="Total sales\n[ 0 ]", bd= 5, relief= RIDGE, bg = "#c9ab69", fg= "black", font=("times new roman", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        #Footer
        lbl_footer=Label(self.root, text="IMS- Inventory Managment System\n For any technical issue contact: 9994395101 ", font=("times new roman",12), bg="#453719", fg="white").pack(side=BOTTOM, fill = X)
       
######################################

    def employee(self):
        self.new_wind=Toplevel(self.root)
        self.new_obj= employeeClass(self.new_wind)





if __name__== "__main__":
    root=Tk()
    obj=IMS(root)
    
    root.mainloop()