import customtkinter as ct
if(__name__ == "__main__"):
    from menu_class import MenuPage

class Food:
    def __init__(self,iordered_food_list,iordered_food,iframe,icount,iroot,ipricelbl):
        self.frame = iframe
        self.ordered_food = iordered_food
        self.count = icount
        self.ordered_food_list = iordered_food_list
        self.root = iroot
        self.pricelbl = ipricelbl
        self.total_price = 0
    
    def update_total_price(self):
        self.total_price = 0
        for i in self.ordered_food_list:
            self.total_price += self.ordered_food_list[i][1]*self.ordered_food_list[i][2]
        self.pricelbl.configure(text=f"Rs.{self.total_price}")
    
    def run_edit_quantity(self):
        quantity = self.ordered_food[1]
        
        newFrame = ct.CTkToplevel(self.root)
        newFrame.title("Order Details")
        newFrame.geometry("500x300")
        newFrame.grab_set()

        def increase_quantity():
            nonlocal quantity
            if(quantity < 4):
                quantity += 1
                newlabel2.configure(text=f"{quantity}")
            if(quantity == 4):
                newbutton2.configure(state="disable")
            elif(quantity == 1):
                newbutton1.configure(state="normal")

        def decrease_quantity():
            nonlocal quantity
            if(quantity > 0):
                quantity -= 1
                newlabel2.configure(text=f"{quantity}")
            if(quantity == 0):
                newbutton1.configure(state="disable")
            elif(quantity == 3):
                newbutton2.configure(state="normal")

        def cancel():
            newFrame.grab_release()
            newFrame.destroy()

        def confirm():
            self.ordered_food[1] = quantity
            self.ordered_food_list[self.count+1] = self.ordered_food
            print(self.ordered_food_list)
            self.lbl2.configure(text=f"{quantity}")
            self.lbl3.configure(text=f"Rs.{self.ordered_food[2]*self.ordered_food[1]}")
            self.update_total_price()
            newFrame.grab_release()
            newFrame.destroy()
        
        newlabel = ct.CTkLabel(newFrame,text="Enter Quantity",width=500,height=50,font=("Times",20,"bold","italic"))
        newlabel.grid(row=0,column=0,columnspan=5,pady=20)
        newbutton1 = ct.CTkButton(newFrame,text="-",width=50,height=50,command=decrease_quantity)
        newbutton1.grid(row=1,column=1,padx = 0,pady=20)
        newlabel2 = ct.CTkLabel(newFrame,text=f"{quantity}",width=80,height=50,font=("Times",20,"bold","italic"))
        newlabel2.grid(row=1,column=2,padx = 10,pady=20)
        newbutton2 = ct.CTkButton(newFrame,text="+",width=50,height=50,command=increase_quantity)
        newbutton2.grid(row=1,column=3,padx = 0,pady=20)
        newbutton3 = ct.CTkButton(newFrame,text="Cancel",width=80,height=50,command=cancel)
        newbutton3.grid(row=2,column=0,columnspan=2,padx=10)
        newbutton4 = ct.CTkButton(newFrame,text="Confirm",width=80,height=50,command=confirm)
        newbutton4.grid(row=2,column=3,columnspan=2,padx=10)
    
    def make_frame(self):

        def edit_quantity():
            self.run_edit_quantity()

        def remove():
            self.ordered_food_list.pop(self.count+1)
            self.myframe.destroy()
            self.update_total_price()

        self.myframe = ct.CTkFrame(self.frame,height=200,width=1000,border_width=3,border_color="yellow")
        self.myframe.grid(row=self.count,column=0,columnspan=4,pady=10)

        hiddenlbl = ct.CTkLabel(self.myframe,text="",width=980,height=10)
        hiddenlbl.grid(row=0,column=0,columnspan=4,pady=5,padx=10)
        lbl1 = ct.CTkLabel(self.myframe,text=f"{self.ordered_food[0]}",width=200,height=30,font=("Times",15,"bold","italic"))
        lbl1.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        self.lbl2 = ct.CTkLabel(self.myframe,text=f"{self.ordered_food[1]}",width=50,height=30,font=("Times",15,"bold","italic"))
        self.lbl2.grid(row=1,column=2,padx=10,pady=10)
        self.lbl3 = ct.CTkLabel(self.myframe,text=f"Rs.{self.ordered_food[2]*self.ordered_food[1]}",width=50,height=30,font=("Times",15,"bold","italic"))
        self.lbl3.grid(row=1,column=3,padx=10,pady=10)

        self.button1 = ct.CTkButton(self.myframe,text="Edit Quantity",width=100,height=30,command=edit_quantity)
        self.button1.grid_remove()
        self.button2 = ct.CTkButton(self.myframe,text="Remove",width=100,height=30,command=remove)
        self.button2.grid_remove()

    



class CheckoutPage:

    def __init__(self,iroot,iordered_food_list):
        self.root = iroot
        self.ordered_food_list = iordered_food_list
        self.total_price = 0
    
    def run(self):
        ordered_list = []
        def edit():
            for x in ordered_list:
                x.button1.grid(row=2,column=2,pady=10)
                x.button2.grid(row=2,column=3,pady=10)

        def back_to_menu():
            for widject in self.root.winfo_children():
                widject.destroy()
            m = MenuPage(self.root,self.ordered_food_list)
            m.run()

        def checkout():
            print(self.ordered_food_list)

        self.root.title("Check Out")
        self.root.geometry(f"1024x600+290+132")

        main_label = ct.CTkLabel(self.root,width=980,height=40,text="Your Orders",font=("Times",35,"bold","italic"))
        main_label.grid(row=0,column=0,columnspan=4,pady=40)

        sub_label1 = ct.CTkLabel(self.root,text="Food Item",width=200,height=30,font=("Times",15,"bold","italic"))
        sub_label1.grid(row=1,column=0,columnspan=2)
        sub_label2 = ct.CTkLabel(self.root,text="Quantity",width=50,height=30,font=("Times",15,"bold","italic"))
        sub_label2.grid(row=1,column=2)
        sub_label3 = ct.CTkLabel(self.root,text="Price",width=50,height=30,font=("Times",15,"bold","italic"))
        sub_label3.grid(row=1,column=3)

        myFrame = ct.CTkScrollableFrame(self.root,orientation="vertical",width=1000,height=300,
                                        border_width=3,
                                        border_color="yellow",
                                        label_font=("Times",25,"bold","italic"))
        myFrame.grid(row=2,column=0,columnspan=4)

        totallbl = ct.CTkLabel(self.root,height=30,width=100,text="Total",font=("Times",23,"bold","italic"))
        totallbl.grid(row=3,column=0,columnspan=2,pady=10)
        totalpricelbl = ct.CTkLabel(self.root,height=30,width=100,text=f"Rs.{self.total_price}",font=("Times",23,"bold","italic"))
        totalpricelbl.grid(row=3,column=3)


        for i in self.ordered_food_list:
            food = Food(self.ordered_food_list,self.ordered_food_list[i],myFrame,i-1,self.root,totalpricelbl)
            food.make_frame()
            ordered_list.append(food)
            self.total_price += self.ordered_food_list[i][2]*self.ordered_food_list[i][1]

        totalpricelbl.configure(text=f"Rs.{self.total_price}")
        

        frame3 = ct.CTkFrame(self.root,height=100,width=1000)
        frame3.grid(row=4,column=0,columnspan=4,pady=10)

        main_button1 = ct.CTkButton(frame3,text="Back to Menu",width=100,height=30,command=back_to_menu)
        main_button1.grid(row=3,column=0,padx=110,pady=10)
        main_button2 = ct.CTkButton(frame3,text="Edit",width=100,height=30,command=edit)
        main_button2.grid(row=3,column=1,padx=110,pady=10)
        main_button3 = ct.CTkButton(frame3,text="CheckOut",width=100,height=30,command=checkout)
        main_button3.grid(row=3,column=2,padx=110,pady=10)

        self.root.mainloop()

if(__name__== "__main__"):
    ordered_food_list = {1:["Chicken Fried Rice",2,300],2:["Chicken Kottu",2,300],3:["Chicken Noodles",2,300]}
    root = ct.CTk()
    c = CheckoutPage(root,ordered_food_list)
    c.run()