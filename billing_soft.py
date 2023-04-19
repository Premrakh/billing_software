from tkinter import *
import math,random
from tkinter import messagebox
import os
class Bill_App():
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x730')
        self.root.title('My Software')
      # ======== Variables ===========================
    #    Cosmetics  
        self.soap=IntVar()
        self.cream=IntVar()
        self.wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.loshan=IntVar()
    #    Grocery 
        self.rice=IntVar()
        self.oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
    #    Cold Drinks  
        self.sprite=IntVar()
        self.redbull=IntVar()
        self.limca=IntVar()
        self.cock=IntVar()
        self.pepsi=IntVar()
        self.fruity=IntVar()
    # Total Price
        self.cos_price=StringVar()
        self.gro_price=StringVar()
        self.cold_price=StringVar()
    #  Tex
        self.cos_tex=StringVar()
        self.gro_tex=StringVar()
        self.cold_tex=StringVar()
    # Customer
        self.c_name=StringVar()
        self.c_no=StringVar()
        self.c_bill=StringVar()
        x=random.randint(10000,99999)
        self.c_bill.set(str(x))





    # ======== Billing Software label ==============
        self.bg_color='#392885'




        l1=Label(self.root,text='Billing Software', font=('aria 15',15,'bold'),bg=self.bg_color,fg='White',bd=7,relief=GROOVE,pady=10).pack(fill=X)
        # thm_btn=Button(l1,text='theme',bg='yellow').place(x=1000,y=20)

  
    # ======== Customer Details ================
        f1=LabelFrame(self.root,text='Customer Details',font=('aria 15',15,'bold'),bd=5,relief=GROOVE,bg=self.bg_color,fg='White',height=80)
        f1.pack(fill=X)
        c_name_lb=Label(f1,text='Customer Name : ',bg=self.bg_color,fg='white',font=('aria 12',12,'bold')).grid(row=0,column=0)
        c_name_en=Entry(f1,textvariable=self.c_name,bd=5,relief=SUNKEN,font=('aria 12',12),width=25).grid(row=0,column=1,padx=3)

        c_no_lb=Label(f1,text='Customer No : ',bg=self.bg_color,fg='white',font=('aria 12',12,'bold')).grid(row=0,column=2)
        c_no_en=Entry(f1,textvariable=self.c_no,bd=5,relief=SUNKEN,font=('aria 12',12),width=25).grid(row=0,column=3,padx=3)

        c_bill_lb=Label(f1,text='Bill No : ',bg=self.bg_color,fg='white',font=('aria 12',12,'bold')).grid(row=0,column=4)
        c_bill_en=Entry(f1,textvariable=self.c_bill,bd=5,relief=SUNKEN,font=('aria 12',12),width=25).grid(row=0,column=5,padx=3)

        srch_btn=Button(f1,text='Search',font=('aria 12',12,'bold'),command=self.find_bill,bg='green',fg='white').grid(row=0,column=6,padx=3,pady=10)

    # ========= Cosmetic ===========================

        f2=LabelFrame(self.root,text='Cosmetics',font=('aria 15',15,'bold'),bd=15,relief=GROOVE,bg=self.bg_color,fg='White')
        f2.place(x=0,y=140,width=300,height=350)
        soap=Label(f2,text='Bath Soap',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=0,column=0,padx=5,pady=7)
        soap_en=Entry(f2,textvariable=self.soap,width=12,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=7)
        
        cream=Label(f2,text='Face Cream',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=1,column=0,padx=5,pady=7)
        cream_en=Entry(f2,textvariable=self.cream,width=12,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=7)
        
        wash=Label(f2,text='Face Wash',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=2,column=0,padx=5,pady=7)
        wash_en=Entry(f2,textvariable=self.wash,width=12,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=7)
        
        spray=Label(f2,text='Hair Spray',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=3,column=0,padx=5,pady=7)
        spray_en=Entry(f2,textvariable=self.spray,width=12,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=7)

        gel=Label(f2,text='Hair Gel',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=4,column=0,padx=5,pady=7)
        gel_en=Entry(f2,textvariable=self.gel,width=12,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=7)

        loshan=Label(f2,text='Body Loshan',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=5,column=0,padx=5,pady=7)
        loshan_en=Entry(f2,width=12,textvariable=self.loshan,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=7)

    # ========= Grocery ===========================

        f2=LabelFrame(self.root,text='Grocery',font=('aria 15',15,'bold'),bd=15,relief=GROOVE,bg=self.bg_color,fg='White')
        f2.place(x=300,y=140,width=300,height=350)

        rice=Label(f2,text='Rice',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=0,column=0,padx=5,pady=7)
        rice_en=Entry(f2,width=12,textvariable=self.rice,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=7)
        
        oil=Label(f2,text='Food Oil',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=1,column=0,padx=5,pady=7)
        oil_en=Entry(f2,width=12,textvariable=self.oil,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=7)
        
        daal=Label(f2,text='Daal',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=2,column=0,padx=5,pady=7)
        daal_en=Entry(f2,width=12,textvariable=self.daal,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=7)
        
        wheat=Label(f2,text='Wheat',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=3,column=0,padx=5,pady=7)
        wheat_en=Entry(f2,width=12,textvariable=self.wheat,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=7)

        sugar=Label(f2,text='Sugar',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=4,column=0,padx=5,pady=7)
        sugar_en=Entry(f2,width=12,textvariable=self.sugar,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=7)

        tea=Label(f2,text='Tea',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=5,column=0,padx=5,pady=7)
        tea_en=Entry(f2,width=12,textvariable=self.tea,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=7)

    # ========= Cold Drinks ===========================

        f2=LabelFrame(self.root,text='Cold Drinks',font=('aria 15',15,'bold'),bd=15,relief=GROOVE,bg=self.bg_color,fg='White')
        f2.place(x=600,y=140,width=300,height=350)
        sprite=Label(f2,text='Sprite',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=0,column=0,padx=5,pady=7)
        sprite_en=Entry(f2,width=12,textvariable=self.sprite,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=7)
        
        red_bull=Label(f2,text='Redbull',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=1,column=0,padx=5,pady=7)
        red_bull_en=Entry(f2,width=12,textvariable=self.redbull,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=7)
        
        limca=Label(f2,text='Limca',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=2,column=0,padx=5,pady=7)
        limca_en=Entry(f2,width=12,textvariable=self.limca,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=7)
        
        cock=Label(f2,text='Cock',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=3,column=0,padx=5,pady=7)
        cock_en=Entry(f2,width=12,textvariable=self.cock,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=5,pady=7)

        pepsi=Label(f2,text='Pepsi',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=4,column=0,padx=5,pady=7)
        pepsi_en=Entry(f2,width=12,textvariable=self.pepsi,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=7)

        fruity=Label(f2,text='Fruity',bg=self.bg_color,fg='white',font=('times new roman',13,'bold')).grid(row=5,column=0,padx=5,pady=7)
        fruity_en=Entry(f2,width=12,textvariable=self.fruity,font=('aria 15',12,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=7)

    # =========== Text Area ====================
        f5=Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=900,y=140,width=450,height=350)
        bill_title=Label(f5,text='Bill Area',font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.textarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

    # ============== Total Amount ===============================
        f6=LabelFrame(self.root,text='Total Amount',bd=10,relief=GROOVE,bg=self.bg_color,fg='white',font=('aria 15',15,'bold'))
        f6.place(x=0,y=500,relwidth=1,height=170)
        
        t_cos=Label(f6,text='Total Cosmetic Price :',font=('times new roman',13,'bold'),bg=self.bg_color,fg='white').grid(row=1,column=0,padx=5,pady=5)
        t_cos_en=Entry(f6,width=20,textvariable=self.cos_price,bd=5,relief=SUNKEN,font=('aria 15',12,'bold')).grid(row=1,column=1,padx=5,pady=5)

        t_gro=Label(f6,text='Total Grocery Price :',font=('times new roman',13,'bold'),bg=self.bg_color,fg='white').grid(row=2,column=0,padx=5,pady=5)
        t_gro_en=Entry(f6,width=20,textvariable=self.gro_price,bd=5,relief=SUNKEN,font=('aria 15',12,'bold')).grid(row=2,column=1,padx=5,pady=5)

        t_drink=Label(f6,text='Total Cold Driks Price :',font=('times new roman',13,'bold'),bg=self.bg_color,fg='white').grid(row=3,column=0,padx=5,pady=5)
        t_drink_en=Entry(f6,width=20,textvariable=self.cold_price,bd=5,relief=SUNKEN,font=('aria 15',12,'bold')).grid(row=3,column=1,padx=5,pady=5)

        cos_tex=Label(f6,text='Total Cosmetic Price :',font=('times new roman',13,'bold'),bg=self.bg_color,fg='white').grid(row=1,column=3,padx=5,pady=5)
        cos_tex_en=Entry(f6,width=20,textvariable=self.cos_tex,bd=5,relief=SUNKEN,font=('aria 15',12,'bold')).grid(row=1,column=4,padx=5,pady=5)

        gro_tex=Label(f6,text='Total Grocery Price :',font=('times new roman',13,'bold'),bg=self.bg_color,fg='white').grid(row=2,column=3,padx=5,pady=5)
        gro_tex_en=Entry(f6,width=20,textvariable=self.gro_tex,bd=5,relief=SUNKEN,font=('aria 15',12,'bold')).grid(row=2,column=4,padx=5,pady=5)

        drink_tex=Label(f6,text='Total Cold Driks Price :',font=('times new roman',13,'bold'),bg=self.bg_color,fg='white').grid(row=3,column=3,padx=5,pady=5)
        drink_tex_en=Entry(f6,width=20,textvariable=self.cold_tex,bd=5,relief=SUNKEN,font=('aria 15',12,'bold')).grid(row=3,column=4,padx=5,pady=5)

    # =========== Final Button ====================
        total=Button(f6,text='Total',bg='Green',fg='white',command=self.total,font=('times new roman',13,'bold'),width=10).place(x=900,y=15)
        gen_bill=Button(f6,text='Genrate Bill',bg='Green',command=self.bill_data,fg='white',font=('times new roman',13,'bold'),width=10).place(x=1050,y=15)
        clear=Button(f6,text='Clear',bg='Green',command=self.clear,fg='white',font=('times new roman',13,'bold'),width=10).place(x=900,y=65)
        exit=Button(f6,text='Exit',bg='Green',command=self.exit,fg='white',font=('times new roman',13,'bold'),width=10).place(x=1050,y=65)
        self.bill_common()
    # ===================== footer =========================
        f7=Frame(self.root,width=1380,height=45,bg=self.bg_color)
        f7.place(x=0,y=670)
        ft=Label(f7,text= " © 2023 - Build by using tkinter",bg=self.bg_color,fg='white',font=('times new roman',13,'bold'))
        ft.place(x=560,y=2)




    def total(self):
        self.t_cos_price=float(
            self.soap.get()*20 +
            self.cream.get()*100+
            self.wash.get()*120+
            self.spray.get()*150+
            self.gel.get()*70+
            self.loshan.get()*70
        
        )
        self.cos_price.set('Rs. '+str(self.t_cos_price))

        self.t_gro_price=float(
            self.rice.get()*35 +
            self.oil.get()*180+
            self.daal.get()*70+
            self.wheat.get()*30+
            self.sugar.get()*40+
            self.tea.get()*400
        
        )
        self.gro_price.set('Rs. '+str(self.t_gro_price))

        self.t_cold_price=float(
            self.sprite.get()*25 +
            self.redbull.get()*90+
            self.limca.get()*40+
            self.cock.get()*50+
            self.pepsi.get()*45+
            self.fruity.get()*35
        
        )
        self.cold_price.set('Rs. '+str(self.t_cold_price))

        self.cos_tex.set('Rs. '+str(round(self.t_cos_price*0.005,2)))
        self.gro_tex.set('Rs. '+str(round(self.t_gro_price*0.005,2)))
        self.cold_tex.set('Rs. '+str(round(self.t_cold_price*0.005,2)))
    
    def bill_common(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,'\t Bill Details'.center(52))
        self.textarea.insert(END,f'\nBill No: {self.c_bill.get()}')
        self.textarea.insert(END,f'\nCustomer Name: {self.c_name.get()}')
        self.textarea.insert(END,f'\nPhone Number: {self.c_no.get()}')
        self.textarea.insert(END,'\n'+'-'*51)
        self.textarea.insert(END,'\nProduct\t\tQTY\t\tPrice')
        self.textarea.insert(END,'\n'+'-'*51)
    def bill_data(self):
        if self.c_name.get()=='' or self.c_no.get()=='':
            messagebox.showerror('Error','Customer Details Empty')
        elif self.cos_price.get()=='Rs. 0.0' and self.gro_price.get()=='Rs. 0.0'and self.cold_price.get()=='Rs. 0.0' :
            messagebox.showerror('Error','Total is zero')
        else:
            self.bill_common()
        # Bill Cosmatic ==============================================
            if self.soap.get()!=0:
                self.textarea.insert(END,f'\nSoap\t\t{self.soap.get()}\t\t{self.soap.get()*20}')
            if self.cream.get()!=0:
                self.textarea.insert(END,f'\nCream\t\t{self.cream.get()}\t\t{self.cream.get()*100}')
            if self.wash.get()!=0:
                self.textarea.insert(END,f'\nWash\t\t{self.wash.get()}\t\t{self.wash.get()*120}')
            if self.spray.get()!=0:
                self.textarea.insert(END,f'\nSpray\t\t{self.spray.get()}\t\t{self.spray.get()*150}')
            if self.gel.get()!=0:
                self.textarea.insert(END,f'\nGel\t\t{self.gel.get()}\t\t{self.gel.get()*70}')
            if self.loshan.get()!=0:
                self.textarea.insert(END,f'\nLoshan\t\t{self.loshan.get()}\t\t{self.loshan.get()*70}')

        # Bill Grocery ==============================================
            if self.rice.get()!=0:
                self.textarea.insert(END,f'\nRice\t\t{self.rice.get()}\t\t{self.rice.get()*35}')
            if self.oil.get()!=0:
                self.textarea.insert(END,f'\nOil\t\t{self.oil.get()}\t\t{self.oil.get()*180}')
            if self.daal.get()!=0:
                self.textarea.insert(END,f'\ndaal\t\t{self.daal.get()}\t\t{self.daal.get()*70}')
            if self.wheat.get()!=0:
                self.textarea.insert(END,f'\nWheat\t\t{self.wheat.get()}\t\t{self.wheat.get()*30}')
            if self.sugar.get()!=0:
                self.textarea.insert(END,f'\nSugar\t\t{self.sugar.get()}\t\t{self.sugar.get()*40}')
            if self.tea.get()!=0:
                self.textarea.insert(END,f'\nTea\t\t{self.tea.get()}\t\t{self.tea.get()*400}')

        # Bill Drinks ==============================================
            if self.sprite.get()!=0:
                self.textarea.insert(END,f'\nSprite\t\t{self.sprite.get()}\t\t{self.sprite.get()*25}')
            if self.redbull.get()!=0:
                self.textarea.insert(END,f'\nRedbull\t\t{self.redbull.get()}\t\t{self.redbull.get()*90}')
            if self.limca.get()!=0:
                self.textarea.insert(END,f'\nLimca\t\t{self.limca.get()}\t\t{self.limca.get()*40}')
            if self.cock.get()!=0:
                self.textarea.insert(END,f'\nCock\t\t{self.cock.get()}\t\t{self.cock.get()*50}')
            if self.pepsi.get()!=0:
                self.textarea.insert(END,f'\nPepsi\t\t{self.pepsi.get()}\t\t{self.pepsi.get()*45}')
            if self.fruity.get()!=0:
                self.textarea.insert(END,f'\nFruity\t\t{self.fruity.get()}\t\t{self.fruity.get()*35}')
            self.textarea.insert(END,'\n'+'-'*51)
        # Total Amount , QTY
            t_pro=str(self.soap.get()+ self.cream.get()+self.wash.get()+self.spray.get()+self.gel.get()+self.loshan.get()+
                    self.rice.get()+self.oil.get()+self.daal.get()+self.wheat.get()+self.sugar.get()+self.tea.get()+
                    self.sprite.get()+self.redbull.get()+self.limca.get()+self.cock.get()+self.pepsi.get()+self.fruity.get())

            self.textarea.insert(END,f'\n\t\t{t_pro}')
            t_price=str(round(self.t_cos_price + self.t_gro_price + self.t_cold_price +round(self.t_cos_price*0.005,2) +
                    round(self.t_gro_price*0.005,2)+round(self.t_cold_price*0.005,2)))

            self.textarea.insert(END,f'\t\t{t_price}')
            self.save_bill()

    def save_bill(self):
        a=messagebox.askyesno('Save','Do you went save the bill ??')
        if a:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open(f'E:\GUI PG\\billing_software\\bill\{str(self.c_bill.get())}.txt',"w")   
            f1.write(self.bill_data)
            f1.close()
            success=messagebox.showinfo('Done',"    Bill save successfully   ")

    def find_bill(self):
        a=r'E:\GUI PG\billing_software\bill'
        for i in os.listdir(a):
            if i[0:5]==self.c_bill.get():
                self.textarea.delete('1.0',END)
                f2=open(f'{a}\{i}','r')
                self.textarea.insert(END,f2.read())

    def clear(self):
    #    Cosmetics  
        self.soap.set(0)
        self.cream.set(0)
        self.wash.set(0)
        self.spray.set(0)
        self.gel.set(0)
        self.loshan.set(0)
    #    Grocery 
        self.rice.set(0)
        self.oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
    #    Cold Drinks  
        self.sprite.set(0)
        self.redbull.set(0)
        self.limca.set(0)
        self.cock.set(0)
        self.pepsi.set(0)
        self.fruity.set(0)
    # Total Price
        self.cos_price.set('Rs. 0.0')
        self.gro_price.set('Rs. 0.0')
        self.cold_price.set('Rs. 0.0')
    #  Tex
        self.cos_tex.set('Rs. 0.0')
        self.gro_tex.set('Rs. 0.0')
        self.cold_tex.set('Rs. 0.0')
    # Customer
        self.c_name.set("")
        self.c_no.set("")
        self.c_bill.set("")
        x=random.randint(10000,99999)
        self.c_bill.set(str(x))
        self.bill_common()
    
    def exit(self):
        a=messagebox.askokcancel('Exit',"Do you went to exit")
        if a: self.root.destroy()

                

        

root=Tk()
obj=Bill_App(root)



root.mainloop()