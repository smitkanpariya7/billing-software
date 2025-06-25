from tkinter import *
from tkinter import ttk, messagebox
import os
import time

class AdminPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x700+0+0")
        self.root.title("Admin Panel")
        bg_color = "#074463"

        Label(self.root, text="Admin Dashboard", bd=12, relief=GROOVE, bg=bg_color,
              fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        #============= Variables ===============
        self.search_bill = StringVar()
        self.bill_dir = "E:\\Billing Software\\invoice"  # <== Defined in one place

        #============= Search Section ============= 
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Search Bill", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=90, relwidth=1)

        Label(F1, text="Bill Number", fg="white", bg=bg_color, font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0, column=2, padx=10, pady=10)
        Button(F1, text="Show All Bills", command=self.show_all_bills, width=12, bd=7, font="arial 12 bold").grid(row=0, column=3, padx=10, pady=10)
        Button(F1, text="Delete Bill", command=self.delete_bill, width=12, bd=7, font="arial 12 bold").grid(row=0, column=4, padx=10, pady=10)
        Button(F1, text="Exit", command=self.Exit_app, width=10, bd=7, font="arial 12 bold").grid(row=0, column=5, padx=10, pady=10)

        #============= Table Frame =============  
        F2 = Frame(self.root, bd=10, relief=GROOVE, bg="white")
        F2.place(x=20, y=200, width=900, height=480)

        Label(F2, text="Customer Bills", font="arial 18 bold", bg="blue", fg="white", bd=7, relief=GROOVE).pack(fill=X)

        scroll_x = Scrollbar(F2, orient=HORIZONTAL)
        scroll_y = Scrollbar(F2, orient=VERTICAL)

        self.bill_table = ttk.Treeview(F2, columns=("bill_no", "cust_name", "phone", "date_time"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", font=("Arial", 11, "bold"))

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.bill_table.xview)
        scroll_y.config(command=self.bill_table.yview)

        self.bill_table.heading("bill_no", text="Bill Number")
        self.bill_table.heading("cust_name", text="Customer Name")
        self.bill_table.heading("phone", text="Phone Number")
        self.bill_table.heading("date_time", text="Date & Time")
        self.bill_table['show'] = 'headings'

        self.bill_table.column("bill_no", width=150, anchor=CENTER)
        self.bill_table.column("cust_name", width=300, anchor=CENTER)
        self.bill_table.column("phone", width=150, anchor=CENTER)
        self.bill_table.column("date_time", width=200, anchor=CENTER)

        self.bill_table.pack(fill=BOTH, expand=1)
        self.bill_table.bind('<Double-1>', self.display_selected_bill)

        #============= Bill Area Frame ==============  
        F3 = Frame(self.root, bd=10, relief=GROOVE)
        F3.place(x=940, y=200, width=380, height=480)
        Label(F3, text="Bill Details", font="arial 18 bold", bg="green", fg="white", bd=7, relief=GROOVE).pack(fill=X)

        scrol_y = Scrollbar(F3, orient=VERTICAL)
        self.textarea = Text(F3, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

    #============= Show All Bills =============  
    def show_all_bills(self):
        self.bill_table.delete(*self.bill_table.get_children())
        try:
            # Sort bills by modification time (latest first)
            bill_files = [file for file in os.listdir(self.bill_dir) if file.endswith(".txt")]
            bill_files.sort(key=lambda x: os.path.getmtime(os.path.join(self.bill_dir, x)), reverse=True)
            
            for file_name in bill_files:
                file_path = os.path.join(self.bill_dir, file_name)
                mod_time = os.path.getmtime(file_path)
                formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mod_time))
                
                with open(file_path, "r") as f:
                    lines = f.readlines()
                    bill_no = file_name.split(".")[0]
                    cust_name = "Unknown"
                    phone = "Unknown"
                    for line in lines:
                        if "Customer Name" in line:
                            cust_name = line.split(":")[1].strip()
                        elif "Phone Number" in line:
                            phone = line.split(":")[1].strip()
                    
                    # Insert data into the table
                    self.bill_table.insert("", END, values=(bill_no, cust_name, phone, formatted_time))
        except Exception as e:
            messagebox.showerror("Error", f"Error loading bills: {str(e)}")

    #============= Display Selected Bill =============  
    def display_selected_bill(self, event):
        selected_item = self.bill_table.focus()
        if not selected_item:
            return
        values = self.bill_table.item(selected_item, 'values')
        if values:
            self.search_bill.set(values[0])
            self.find_bill()

    #============= Find Bill =============  
    def find_bill(self):
        present = False
        try:
            for file_name in os.listdir(self.bill_dir):
                if file_name.split(".")[0] == self.search_bill.get():
                    file_path = os.path.join(self.bill_dir, file_name)
                    with open(file_path, "r") as f:
                        self.textarea.config(state='normal')
                        self.textarea.delete('1.0', END)
                        self.textarea.insert(END, f.read())
                        self.textarea.config(state='disabled')
                    present = True
                    break
            if not present:
                messagebox.showerror("Error", "Invalid Bill No")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    #============= Delete Bill =============  
    def delete_bill(self):
        bill_no = self.search_bill.get()
        if not bill_no:
            messagebox.showerror("Error", "Please select a bill to delete.")
            return

        bill_path = os.path.join(self.bill_dir, f"{bill_no}.txt")

        if not os.path.exists(bill_path):
            messagebox.showerror("Error", "Bill not found.")
            return

        op = messagebox.askyesno("Delete Bill", f"Are you sure you want to delete Bill No: {bill_no}?")
        if op:
            os.remove(bill_path)
            messagebox.showinfo("Success", "Bill deleted successfully.")
            self.textarea.config(state='normal')
            self.textarea.delete('1.0', END)
            self.search_bill.set("")
            self.show_all_bills()

    #============= Exit Application =============  
    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you want to exit?")
        if op:
            self.root.destroy()

#============= Main Execution =============  
if __name__ == "__main__":
    root = Tk()
    obj = AdminPage(root)
    root.mainloop()
