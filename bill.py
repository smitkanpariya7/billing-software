from tkinter import *
from tkinter import messagebox
import math,random,os
from fpdf import FPDF
from time import strftime

class Bill_App:
    #=================phone number validation================
    def validate_phone_number(self, input_text):
        return input_text.isdigit() and len(input_text) <= 10
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1360x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        # Function to update the time label
        def time():
            current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
            current_date = strftime('%d/%m/%Y') # Example: Sunday, 08 June 2025
            time_label.config(text=f"{current_time}\n{current_date}")
            time_label.after(1000, time)

        # Create a label for the digital clock on the left side of the screen
        time_label = Label(root, font=("times new roman", 14, "bold"), bg=bg_color, fg="white")
        time_label.place(x=1230, y=12)  # Position it at the left side, below the title

        # Start the time function
        time()
        
        #=============Variables======================
        #=============Cosmatics======================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #=============Grocery========================
        self.rice=IntVar()
        self.food_oil=IntVar() 
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #=============Cold Drinka====================
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        #=============Total Product Price and Tax variables====================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        #=============Customer Detail================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1,999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #=============Customer Detail================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=90,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",fg="white",bg=bg_color,font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=11,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl = Label(F1, text="Phone No.", fg="white", bg=bg_color, font=("times new roman", 14, "bold"))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)

        validate_phoneno = self.root.register(self.validate_phone_number)
        cphn_txt = Entry(F1, width=11, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN, validate="key", validatecommand=(validate_phoneno, '%P'))
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)
       
        #=============Cosmetics Frame================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=3,y=190,width=325,height=380)
        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        face_crm_lbl=Label(F2,text="Face Cream",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_crm_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        hair_gel_lbl=Label(F2,text="Hair Gell",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gel_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        body_lbl=Label(F2,text="Body Loshan",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============Grocery Frame================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=320,y=190,width=285,height=380)
        g1_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        g3_lbl=Label(F3,text="Daal",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        g4_lbl=Label(F3,text="Wheat",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        g5_lbl=Label(F3,text="Suger",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============Cold Drink Frame================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=600,y=190,width=300,height=380)
        c1_lbl=Label(F4,text="Maza",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        c2_lbl=Label(F4,text="Cock",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        c3_lbl=Label(F4,text="Frooti",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        c4_lbl=Label(F4,text="ThumbsUp",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        c5_lbl=Label(F4,text="Limca",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        c6_lbl=Label(F4,text="Sprite",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #=============Bill Area Frame================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=905,y=190,width=440,height=350)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=============Button Frame================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=3,y=560,relwidth=1,height=140)
        
        Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        Entry(F6,width=15,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN,state='readonly').grid(row=0,column=1,padx=10,pady=1)

        Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        Entry(F6,width=15,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN,state='readonly').grid(row=1,column=1,padx=10,pady=1)

        Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        Entry(F6,width=15,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN,state='readonly').grid(row=2,column=1,padx=10,pady=1)

        Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=3,padx=20,pady=1,sticky="w")
        Entry(F6,width=15,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN,state='readonly').grid(row=0,column=4,padx=10,pady=1)

        Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=3,padx=20,pady=1,sticky="w")
        Entry(F6,width=15,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN,state='readonly').grid(row=1,column=4,padx=10,pady=1)

        Label(F6,text="Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=3,padx=20,pady=1,sticky="w")
        Entry(F6,width=15,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN,state='readonly').grid(row=2,column=4,padx=10,pady=1)
        
        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=820,width=510,height=180)
        
        Button(btn_f,text="Total",command=self.total,bg="#f39c12",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
        Button(btn_f,command=self.bill_area,text="Generate Bill",bg="#1abc9c",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
        Button(btn_f,text="Clear",command=self.clear_data,bg="#e74c3c",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
        Button(btn_f,text="Exit",command=self.Exit_app,bg="#95a5a6",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)

        self.welcome_bill()
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_spr_p=self.spray.get()*180
        self.c_g_p=self.gell.get()*140
        self.c_l_p=self.loshan.get()*180
        self.total_cosmatic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_spr_p+
                                    self.c_g_p+
                                    self.c_l_p
                                  )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmatic_price))
        self.c_tax=round(self.total_cosmatic_price*0.05,2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        self.g_r_p=self.rice.get()*80
        self.g_fo_p=self.food_oil.get()*180
        self.g_w_p=self.wheat.get()*60
        self.g_d_p=self.daal.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*150
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_fo_p+
                                    self.g_w_p+
                                    self.g_d_p+
                                    self.g_s_p+
                                    self.g_t_p
                                  )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round(self.total_grocery_price*0.1,2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        self.cd_m_p=self.maza.get()*60
        self.cd_c_p=self.cock.get()*60
        self.cd_f_p=self.frooti.get()*50
        self.cd_th_p=self.thumbsup.get()*45
        self.cd_l_p=self.limca.get()*40
        self.cd_s_p=self.sprite.get()*60
        self.total_cold_drink_price=float(
                                    self.cd_m_p+
                                    self.cd_c_p+
                                    self.cd_f_p+
                                    self.cd_th_p+
                                    self.cd_l_p+
                                    self.cd_s_p
                                   )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round(self.total_cold_drink_price*0.05,2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))
        self.total_bill=float(
            self.total_cosmatic_price+
            self.total_grocery_price+
            self.total_cold_drink_price+
            self.c_tax+
            self.g_tax+
            self.cd_tax
        )
    def welcome_bill(self):
        self.textarea.config(state='normal')
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "WELCOME KHODAL RETAILS", "center")
        self.textarea.insert(END, f"\n==========================================")
        self.textarea.insert(END, f"\n Bill Number :{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name :{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number :{self.c_phon.get()}")
        self.textarea.tag_configure("center", justify='center')  
        
        self.textarea.insert(END, f"\n======================================")
        self.textarea.insert(END, f"\n Product\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n======================================")
        self.textarea.config(state='disabled')

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer Details are Required")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Selected")
        else:
            self.welcome_bill()
            self.textarea.config(state='normal')

            #=== Cosmetics ===
            if self.soap.get() != 0:
                self.textarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get() != 0:
                self.textarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.textarea.insert(END, f"\n Face Wash \t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get() != 0:
                self.textarea.insert(END, f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_s_p}")
            if self.gell.get() != 0:
                self.textarea.insert(END, f"\n Hair Gell \t\t{self.gell.get()}\t\t{self.c_g_p}")
            if self.loshan.get() != 0:
                self.textarea.insert(END, f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_l_p}")

            #=== Grocery ===
            if self.rice.get() != 0:
                self.textarea.insert(END, f"\n Rice   \t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.textarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            if self.daal.get() != 0:
                self.textarea.insert(END, f"\n Daal   \t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\n Wheat  \t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.textarea.insert(END, f"\n Sugar  \t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.textarea.insert(END, f"\n Tea   \t\t{self.tea.get()}\t\t{self.g_t_p}")
            
            #=== Cold Drink ===
            if self.maza.get() != 0:
                self.textarea.insert(END, f"\n Maza   \t\t{self.maza.get()}\t\t{self.cd_m_p}")
            if self.cock.get() != 0:
                self.textarea.insert(END, f"\n Cock   \t\t{self.cock.get()}\t\t{self.cd_c_p}")
            if self.frooti.get() != 0:
                self.textarea.insert(END, f"\n Frooti  \t\t{self.frooti.get()}\t\t{self.cd_f_p}")
            if self.thumbsup.get() != 0:
                self.textarea.insert(END, f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.cd_th_p}")
            if self.limca.get() != 0:
                self.textarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.cd_l_p}")
            if self.sprite.get() != 0:
                self.textarea.insert(END, f"\n Sprite  \t\t{self.sprite.get()}\t\t{self.cd_s_p}")

            self.textarea.insert(END, f"\n--------------------------------------")

            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Cosmetic Tax \t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Grocery Tax \t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n ColdDrink Tax\t\t\t{self.cold_drink_tax.get()}")
            
            self.textarea.insert(END, f"\n--------------------------------------")
            self.textarea.insert(END, f"\n Total Bill  \t\t\t Rs. {self.total_bill}")
            self.textarea.insert(END, f"\n---------------------------------------")
            
            self.textarea.config(state='disabled')
            self.save_bill()

        
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.textarea.get('1.0', END)
            try:
                with open(f"E:\\Billing Software\\invoice\\{self.bill_no.get()}.txt", "w", encoding="utf-8") as f:
                    f.write(self.bill_data)
                messagebox.showinfo("Saved", f"Bill no. :{self.bill_no.get()} saved successfully as Text File")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving bill: {e}")
        else:
            return
    
    def clear_data(self):
        op=messagebox.askyesno("clear","Do you want to Reset Entries?")
        if op>0:
            #=============Cosmatics======================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            #=============Grocery========================
            self.rice.set(0)
            self.food_oil.set(0) 
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #=============Cold Drinka====================
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            #=============Total Product Price and Tax variables====================
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #=============Customer Detail================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)

root.mainloop()