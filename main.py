from tkinter import *
root = Tk()
root.title("Renuga Jewellers wholesales")
root.state("zoomed")
# lable configuration
Tittle = Frame(root)
Tittle.grid(row=0,pady=20)
Tittle_lbl = Label(Tittle,text="RENUGA  JEWELLERS",font=("Times 30 bold")).grid(row=0)
label_frame = Frame(root)
label_frame.grid(row=1,pady=20)
company_name = Label(label_frame, text="Company Name",font=("Times 16"),height=3).grid(row=0, column=0,sticky="W",padx=40)
Purchase_date = Label(label_frame,text = "Purchase Date",font=("Times 16"),height=3).grid(row=1,column=0,sticky="W",padx=40)
Phone_Number =Label(label_frame,text="Phone No",font=("Times 16"),height=3).grid(row=2,column=0,sticky="W",padx=40)
Mobile_Number = Label(label_frame,text="Mobile No",font=("Times 16"),height=3).grid(row=3,column=0,sticky="W",padx=40)
Email = Label(label_frame,text="Email",font=("Times 16"),height=3).grid(row=4,column=0,sticky="W",padx=40)
GST_No = Label(label_frame,text="GST No",font=("Times 16"),height=3).grid(row=5,column=0,sticky="W",padx=40)
Door_No= Label(label_frame,text="Door No",font=("Times 16"),height=3).grid(row=0,column=2,sticky="W",padx=40)
Area = Label(label_frame,text="Area",font=("Times 16"),height=3).grid(row=1,column=2,sticky="W",padx=40)
City = Label(label_frame,text="City",font=("Times 16"),height=3).grid(row=2,column=2,sticky="W",padx=40)
District = Label(label_frame,text="District",font=("Times 16"),height=3).grid(row=3,column=2,sticky="W",padx=40)
State = Label(label_frame,text="State",font=("Times 16"),height=3).grid(row=4,column=2,sticky="W",padx=40)
Pincode = Label(label_frame, text="Pin Code",font=("Times 16"),height=3).grid(row=5,column=2,sticky="W",padx=40)

company_name_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=0, column=1,padx=50)
Purchase_date_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=1, column=1,padx=50)
Phone_Number_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=2, column=1,padx=50)
Mobile_Number_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=3, column=1,padx=50)
Email_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=4, column=1,padx=50)
GST_No_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=5, column=1,padx=50)
Door_No_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=0, column=3,padx=50)
Area_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=1, column=3,padx=50)
City_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=2, column=3,padx=50)
District_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=3, column=3,padx=50)
State_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=4, column=3,padx=50)
Pincode_txt = Entry(label_frame,width= 40,font=("Times 18")).grid(row=5, column=3,padx=50)
btn_frame = Frame(root)
btn_frame.grid(row = 2,columnspan=4,pady=70)
Submit_btn = Button(btn_frame,text="Submit",width=10,font=("Times 18"),bg="Green").grid(row=0,column=0)
Cancel_btn = Button(btn_frame,text="Cancel",width=10,font=("Times 18"),bg="Red").grid(row=0,column=1)
Reset_btn = Button(btn_frame,text="Reset",width=10,font=("Times 18"),bg="Blue").grid(row=0,column=2)
Exit_btn = Button(btn_frame,text="Exit",width=10,font=("Times 18"),bg="Black",fg="white").grid(row=0,column=3)

root.mainloop()