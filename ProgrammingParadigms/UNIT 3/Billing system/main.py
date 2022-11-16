from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import random, os
from tkinter import messagebox
import tempfile

absolute_path = os.path.dirname(__file__)

cashier_relative_path = "Images/cashier.png"
im1_relative_path = "Images/im1.png"
im2_relative_path = "Images/im2.jpg"
middle_relative_path = "Images/middle.png"
sup_relative_path = "Images/sup.png"

cashier_absolute_path = os.path.join(absolute_path, cashier_relative_path)
im1_absolute_path = os.path.join(absolute_path, im1_relative_path)
im2_absolute_path = os.path.join(absolute_path, im2_relative_path)
middle_absolute_path = os.path.join(absolute_path, middle_relative_path)
sup_absolute_path = os.path.join(absolute_path, sup_relative_path)

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Sofware")#titulo de la ventana
        
        ###################VARIABLES##############################
        self.c_name= StringVar()
        self.c_phon= StringVar()
        self.bill_no= StringVar()
        z= random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email= StringVar()
        self.search_bill= StringVar()
        self.product= StringVar()
        self.prices= IntVar()
        self.qty= IntVar()
        self.sub_total= StringVar()
        self.tax_input= StringVar()
        self.total= StringVar()
        


        #Product categories
        self.Category=["Selec Option","Cell phones", "Photography","Smart home"]
        
        #SUBCATEGORIES CELLPHONES
        self.SubCatCellphones=["iPhone", "Samsung", "Xiaomi", "Motorola"]
        

        self.iPhone= ["iPhone X", "iPhone Xr", "iPhone 11", "iPhone 12", "iPhone 13"]
        self.priceX= 10000
        self.priceXr = 12000
        self.priceiPhone11= 16000
        self.priceiPhone12= 19000
        self.priceiPhone13= 250000

        self.Samsung=["GalaxyS10", "Galaxy A22","Zflip"]
        self.S10=6999
        self.A22=3950
        self.Zflip= 22047
        
        self.xiaomi=["Redmi 9","Note 11", "PocoF4"]
        self.red9=999
        self.note11=3899
        self.F4=8499

        self.Motorola=["G60", "E20", "G52", "E32"]
        self.G60=3989
        self.E20=1999
        self.G52=7469
        self.E32= 4029


        self.SubCatPhotography=["Camera", "VideoCamera", "Drones"]
        self.Camera=["Instax mini", "GoPro","Canon M50" ]
        self.instax=4600
        self.GoPro =5330
        self.canon = 13489

        self.VideoCamara= ["VAK VD-534K", "Andoer 4K", "Camcoders PXW-Z190"]
        self.VAK=4361
        self.Andoer=2099.99
        self.camcoders=96120.48

        self.Drones =["Binden S7", "Binden Falcon GD93", "Fpv Combo"]
        self.S7= 3749
        self.GD93= 1759
        self.Fpv=114.33

        self.SubCatSmarthome= ["Lighting","Security", "Automation"]
        self.lighting=["Dimmer Light Switch", "LED strip", "Mart bulb"]
        self.dimmer=246.22
        self.strip=399
        self.bulb= 199

        self.security=["Electrick lock Lloyds","Save box STEREN", "Interphone video LC-1178"]
        self.lock=699
        self.savebox= 1979
        self.inter=3199

        self.Automation=["Echo Dot", "Google Nest", "Smoke Alarm Google"]
        self.Echo=849
        self.goNest=1988
        self.smoke=2999

       
        #Image1 sup
        
        img=Image.open(sup_absolute_path)
        img=img.resize((650,130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root, image=self.photoimg)
        lbl_img.place(x=0, y=0, width=400, height=130)
        #Image2 sup
        img1=Image.open(sup_absolute_path)
        img1=img1.resize((650,130), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_img1=Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=260, y=0, width=400, height=130)
        #Image3  sup
        img2=Image.open(sup_absolute_path)
        img2=img2.resize((650,130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl_img2=Label(self.root, image=self.photoimg2)
        lbl_img2.place(x=520, y=0, width=400, height=130)
        #Image4  sup
        img3=Image.open(sup_absolute_path)
        img3=img3.resize((650,130), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl_img3=Label(self.root, image=self.photoimg3)
        lbl_img3.place(x=780, y=0, width=400, height=130)
        #Image5 sup
        img4=Image.open(sup_absolute_path)
        img4=img2.resize((650,130), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbl_img4=Label(self.root, image=self.photoimg4)
        lbl_img4.place(x=1040, y=0, width=400, height=130)
        
        #Title
        lbl_title= Label(self.root, text="Billing Software Store ", font=("times new roman", 35, "bold"), bg="#5ba383", fg="white")
        lbl_title.place(x=0, y=130, width=1400, height=45)

        Main_Frame=Frame (self.root, bd=5, relief=GROOVE, bg="#dae8e2")
        Main_Frame.place(x=0, y=175, width=1530, height=620)

        #Customer Label Frame
        Cust_Frame= LabelFrame(Main_Frame, text="Customer", font=("times new roman", 12, "bold"), bg="#5ba383", fg="white")
        Cust_Frame.place(x=10, y=5, width=300, height=140)

        self.lbl_mob= Label(Cust_Frame, text="Mobile No.", font=("times new roman", 12,"bold"), bg="#5ba383")
        self.lbl_mob.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.entry_mob= ttk.Entry(Cust_Frame, textvariable=self.c_phon,font=("times new roman", 10), width=24)
        self.entry_mob.grid(row=0, column=1)

        self.lblCustName= Label(Cust_Frame, font=("times new roman", 12,"bold"), bg="#5ba383", text="Customer name",bd=4)
        self.lblCustName.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.txtCustName= ttk.Entry(Cust_Frame, textvariable= self.c_name,font=("times new roman", 10), width=24)
        self.txtCustName.grid(row=1, column=1, stick=W, padx=5, pady=2)
        
        self.lblEmail= Label(Cust_Frame, font=("times new roman", 12,"bold"), bg="#5ba383", text="Email",bd=4)
        self.lblEmail.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txtEmail= ttk.Entry(Cust_Frame, textvariable=self.c_email,font=("times new roman", 10), width=24)
        self.txtEmail.grid(row=2, column=1, stick=W, padx=5, pady=2)

        #Product Label Frame
        Product_Frame= LabelFrame(Main_Frame, text="Product", font=("times new roman", 12, "bold"), bg="#5ba383", fg="white")
        Product_Frame.place(x=320, y=5, width=600, height=140)

        #Category
        self.lblCategory= Label(Product_Frame,font=("times new roman", 12,"bold"), bg="#5ba383", text="Select categories",bd=4)
        self.lblCategory.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame, values=self.Category,font=("times new roman", 10,"bold"), width=24, state="readonly")
        self.Combo_Category.grid(row=0, column=1, stick=W, padx=5, pady=2)

        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)



        #Subcategory
        self.lblSubCategory= Label(Product_Frame, font=("times new roman", 12,"bold"), bg="#5ba383", text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.Combo_SubCategory=ttk.Combobox(Product_Frame, value=[""] ,font=("times new roman", 10,"bold"), width=24, state="readonly")
        self.Combo_SubCategory.grid(row=1, column=1, stick=W, padx=5, pady=2)

        self.Combo_SubCategory.bind("<<ComboboxSelected>>", self.Product_add)


        #Product name
        self.lblName= Label(Product_Frame, font=("times new roman", 12,"bold"), bg="#5ba383", text="Product name",bd=4)
        self.lblName.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame, textvariable=self.product,font=("times new roman", 10,"bold"), width=24, state="readonly")
        self.ComboProduct.grid(row=2, column=1, stick=W, padx=5, pady=2)
        
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)


        #Product price
        self.lblPrice= Label(Product_Frame, font=("times new roman", 12,"bold"), bg="#5ba383", text="Price",bd=4)
        self.lblPrice.grid(row=0, column=2, stick=W, padx=5, pady=2)

        self.Combo_Price=ttk.Combobox(Product_Frame, textvariable=self.prices ,font=("times new roman", 10,"bold"), width=24, state="readonly")
        self.Combo_Price.grid(row=0, column=3, stick=W, padx=5, pady=2)
        


        #Product quantity
        self.lblQty= Label(Product_Frame, font=("times new roman", 12,"bold"), bg="#5ba383", text="Qty",bd=4)
        self.lblQty.grid(row=1, column=2, stick=W, padx=5, pady=2)

        self.Combo_Qty=ttk.Entry(Product_Frame, textvariable=self.qty,font=("times new roman", 10), width=31)
        self.Combo_Qty.grid(row=1, column=3, stick=W, padx=5, pady=2)

        #Middle Frame
        MiddleFrame= Frame(Main_Frame, bd=10)
        MiddleFrame.place(x=10, y=150, width=910,height=230)
        #Image1 
        img12=Image.open(middle_absolute_path)
        img12=img12.resize((230, 180), Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame, image=self.photoimg12)
        lbl_img12.place(x=0, y=0, width=390, height=180)
        #Image2 
        img13=Image.open(cashier_absolute_path)
        img13=img13.resize((280,210), Image.Resampling.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        lbl_img13=Label(MiddleFrame, image=self.photoimg13)
        lbl_img13.place(x=400, y=0, width=390, height=180)


        #Search
        Search_Frame=Frame(Main_Frame,bd=2, bg="white")
        Search_Frame.place(x=935, y=10, width=400, height=35)
        
        self.lblBill= Label(Search_Frame, font=("times new roman", 12,"bold"),fg="white", bg="#5ba383", text="Bill number",bd=4)
        self.lblBill.grid(row=0, column=0, stick=W, padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill ,font=("times new roman", 10,"bold"), width=26)
        self.txt_Entry_Search.grid(row=0, column=1, stick=W, padx=2)

        self.BtnSearch=Button(Search_Frame, text="Search", font=("times new roman", 10, "bold"), bg="#07705d", fg="white", width=13, cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)




        #RightFrame Bill 

        RightLabelFrame = LabelFrame(Main_Frame, text="Bill", font=("times new roman", 14, "bold"), bg="#5ba383", fg="white")
        RightLabelFrame.place(x=935, y=50, width=400, height=330)

        scroll_y= Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea=Text(RightLabelFrame, yscrollcommand=scroll_y.set, bg="white", fg="blue", font=("times new roman", 10, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        #Bill counter LabelFrame
        Botton_Frame=LabelFrame(Main_Frame, text="Bill counter",font=("times new roman", 12, "bold"), bg="#5ba383", fg="white", bd=4)
        Botton_Frame.place(x=0, y=385, width=1520, height=125)


        self.lblSubTotal= Label(Botton_Frame, font=("times new roman", 12,"bold"), bg="#5ba383", text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Enty_SubTotal=ttk.Entry(Botton_Frame, textvariable=self.sub_total,font=("times new roman", 10,"bold"), width=26)
        self.Enty_SubTotal.grid(row=0, column=1, stick=W, padx=5, pady=2)

        self.lbl_tax= Label(Botton_Frame, font=("times new roman", 12,"bold"), bg="#5ba383", text="Tax",bd=4)
        self.lbl_tax.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.txt_tax=ttk.Entry(Botton_Frame, textvariable= self.tax_input,font=("times new roman", 10,"bold"), width=26)
        self.txt_tax.grid(row=1, column=1, stick=W, padx=5, pady=2)

        self.lblAmount= Label(Botton_Frame, font=("times new roman", 12,"bold"), bg="#5ba383", text="Total",bd=4)
        self.lblAmount.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txt_Amount=ttk.Entry(Botton_Frame,textvariable= self.total ,font=("times new roman", 10,"bold"), width=26)
        self.txt_Amount.grid(row=2, column=1, stick=W, padx=5, pady=2)

        #Button Frame
        Btn_Frame=Frame(Botton_Frame,bd=2, bg="white")
        Btn_Frame.place(x=320, y=0)

        self.BtnAddToCart=Button(Btn_Frame, command=self.AddItem,text="Add to cart", font=("times new roman", 15, "bold"), bg="#07705d", fg="white", width=13, cursor="hand2")
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btngenerate_bill=Button(Btn_Frame, command=self.gen_bill,text="Generate Bill", font=("times new roman", 15, "bold"), bg="#07705d", fg="white", width=13, cursor="hand2")
        self.Btngenerate_bill.grid(row=0, column=1)
        
        self.BtnSave=Button(Btn_Frame, command= self.save_bill,text="Save", font=("times new roman", 15, "bold"), bg="#07705d", fg="white", width=13, cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint=Button(Btn_Frame, command=self.iprint,text="Print", font=("times new roman", 15, "bold"), bg="#07705d", fg="white", width=13, cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear=Button(Btn_Frame, text="Clear", font=("times new roman", 15, "bold"), bg="#07705d", fg="white", width=13, cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit=Button(Btn_Frame, text="Exit", font=("times new roman", 15, "bold"), bg="#07705d", fg="white", width=13, cursor="hand2")
        self.BtnExit.grid(row=0, column=5)
    
        self.welcome()

        self.l=[]
    #=====================================Functions declaration==============================================
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)

        if self.product.get()=="":
            messagebox.showerror("Error", "Please Select the Product Name")
        else:
            self.textarea.insert(END, f"\n {self.product.get()}\t\t\t\t{self.qty.get()}\t{self.m}")
            self.sub_total.set(str('$.%.2f'%(sum(self.l))))
            self.tax_input.set(str("$.%.2f"%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('$.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))
            
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error", "Please Add To Cart")
        else:
            text = self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text )
            self.textarea.insert(END, "\n=====================================================")
            self.textarea.insert(END, f"\n Sub amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n=====================================================")



    def save_bill(self):
        op = messagebox.askyesno("Save bill", "Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get(1.0, END)
            f1=open('Bills/'+str(self.bill_no.get())+".txt", 'w')
            f1.write(self.bill_data)
            op = messagebox.showinfo("Saved", f"Bill no. {self.bill_no.get()} saved succesfully")

            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0, "end-1c")
        filename= tempfile.mktemp('.txt')
        open(filename, 'w').write(q)
        os.startfile(filename, "print")





    def welcome(self):
            self.textarea.delete(1.0, END)
            self.textarea.insert(END, "\t\t Welcome to UPY's store")
            self.textarea.insert(END, f"\n Bill number:{self.bill_no.get()}")
            self.textarea.insert(END, f"\n Customer name:{self.c_name.get()}")
            self.textarea.insert(END, f"\n Phone number :{self.c_phon.get()}")
            self.textarea.insert(END, f"\n Customer email:{self.c_email.get()}")

            self.textarea.insert(END, "\n=====================================================")
            self.textarea.insert(END, "\n Products\t\t\t\tQty\tPrice")
            self.textarea.insert(END, "\n=====================================================")
  


    def Categories(self, event=""):
            if self.Combo_Category.get()=="Cell phones":
                self.Combo_SubCategory.config(value=self.SubCatCellphones)
                self.Combo_SubCategory.current(0)
            
            if self.Combo_Category.get()=="Photography":
                self.Combo_SubCategory.config(value=self.SubCatPhotography)
                self.Combo_SubCategory.current(0)

            if self.Combo_Category.get()=="Smart home":
                self.Combo_SubCategory.config(value=self.SubCatSmarthome)
                self.Combo_SubCategory.current(0)

    def Product_add(self, event=""):
        #Cellphones
        if self.Combo_SubCategory.get()=="iPhone":
            self.ComboProduct.config(value=self.iPhone)

        if self.Combo_SubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)

        if self.Combo_SubCategory.get()=="Xiaomi":
            self.ComboProduct.config(value=self.xiaomi)

        if self.Combo_SubCategory.get()=="Motorola":
            self.ComboProduct.config(value=self.Motorola)

        #Camera
        if self.Combo_SubCategory.get()=="Camera":
            self.ComboProduct.config(value=self.Camera)
        
        if self.Combo_SubCategory.get()=="VideoCamera":
            self.ComboProduct.config(value=self.VideoCamara)

        if self.Combo_SubCategory.get()=="Drones":
            self.ComboProduct.config(value=self.Drones)

        #Smart home
        if self.Combo_SubCategory.get()=="Lighting":
            self.ComboProduct.config(value=self.lighting)
        
        if self.Combo_SubCategory.get()=="Security":
            self.ComboProduct.config(value=self.security)

        if self.Combo_SubCategory.get()=="Automation":
            self.ComboProduct.config(value=self.Automation)

    def price(self,event=""):
        #iphone
        if self.ComboProduct.get()=="iPhone X":
            self.Combo_Price.config(value=self.priceX)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="iPhone Xr":
            self.Combo_Price.config(value=self.priceXr)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="iPhone 11":
            self.Combo_Price.config(value=self.priceiPhone11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="iPhone 12":
            self.Combo_Price.config(value=self.priceiPhone12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="iPhone 13":
            self.Combo_Price.config(value=self.priceiPhone13)
            self.Combo_Price.current(0)
            self.qty.set(1)

        #Samsung
        if self.ComboProduct.get()=="GalaxyS10":
            self.Combo_Price.config(value=self.S10)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Galaxy A22":
            self.Combo_Price.config(value=self.A22)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Zflip":
            self.Combo_Price.config(value=self.Zflip)
            self.Combo_Price.current(0)
            self.qty.set(1)

        #Xiaomi
        if self.ComboProduct.get()=="Redmi 9":
            self.Combo_Price.config(value=self.red9)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Note 11":
            self.Combo_Price.config(value=self.note11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="PocoF4":
            self.Combo_Price.config(value=self.F4)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        #Motorola
        if self.ComboProduct.get()=="G60":
            self.Combo_Price.config(value=self.G60)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="E20":
            self.Combo_Price.config(value=self.E20)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="G52":
            self.Combo_Price.config(value=self.G52)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="E32":
            self.Combo_Price.config(value=self.E32)
            self.Combo_Price.current(0)
            self.qty.set(1)

        #Camera
        if self.ComboProduct.get()=="Instax mini":
            self.Combo_Price.config(value=self.instax)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="GoPro":
            self.Combo_Price.config(value=self.GoPro)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Canon M50":
            self.Combo_Price.config(value=self.canon)
            self.Combo_Price.current(0)
            self.qty.set(1)
        
        #VideoCamera
        if self.ComboProduct.get()=="VAK VD-534K":
            self.Combo_Price.config(value=self.VAK)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Andoer 4K":
            self.Combo_Price.config(value=self.Andoer)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Camcoders PXW-Z190":
            self.Combo_Price.config(value=self.camcoders)
            self.Combo_Price.current(0)
            self.qty.set(1)

        #Drones
        if self.ComboProduct.get()=="Binden S7":
            self.Combo_Price.config(value=self.S7)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Binden Falcon GD93":
            self.Combo_Price.config(value=self.GD93)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Fpv Combo":
            self.Combo_Price.config(value=self.Fpv)
            self.Combo_Price.current(0)
            self.qty.set(1)

        #LIGHTING
        if self.ComboProduct.get()=="Dimmer Light Switch":
            self.Combo_Price.config(value=self.dimmer)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="LED strip":
            self.Combo_Price.config(value=self.strip)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mart bulb":
            self.Combo_Price.config(value=self.bulb)
            self.Combo_Price.current(0)
            self.qty.set(1)

        #Security
        if self.ComboProduct.get()=="Electrick lock Lloyds":
            self.Combo_Price.config(value=self.lock)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Save box STEREN":
            self.Combo_Price.config(value=self.savebox)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Interphone video LC-1178":
            self.Combo_Price.config(value=self.inter)
            self.Combo_Price.current(0)
            self.qty.set(1)
    
        #Automation
        if self.ComboProduct.get()=="Echo Dot":
            self.Combo_Price.config(value=self.Echo)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Google Nest":
            self.Combo_Price.config(value=self.goNest)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Smoke Alarm Google":
            self.Combo_Price.config(value=self.smoke)
            self.Combo_Price.current(0)
            self.qty.set(1)








if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()