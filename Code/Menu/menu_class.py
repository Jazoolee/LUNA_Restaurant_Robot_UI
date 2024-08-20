import customtkinter as ct
# if(__name__ == "__main__"):
#     from checkout_class import CheckoutPage
from checkout_class import CheckoutPage
class FoodSubFrame:

    def __init__(self,iframe,iname,iprice,iroot,iordered_food_list,icategory):
        self.frame = iframe
        self.name = iname
        self.price = int(iprice)
        self.root = iroot
        self.ordered_food_list = iordered_food_list
        self.quantity = 0
        self.category = icategory
    
    def update_ordered_food_list(self):
        count = len(self.ordered_food_list) + 1
        food = [self.name+" "+self.category,self.quantity,self.price]
        self.ordered_food_list[count] = food
    
    def check_for_ordered_food(self):
        for i in self.ordered_food_list:
            if(self.ordered_food_list[i][0] == self.name+" "+self.category):
                self.cancelbutton.configure(state="normal")
                self.orderbutton.configure(state="disable",text="Ordered",fg_color="Green")

    def create_food_sub_frame(self):

        def order():
            if(self.orderbutton.cget("state") == "normal"):
                self.quantity = 0
                
                newFrame = ct.CTkToplevel(self.root)
                newFrame.title("Order Details")
                newFrame.geometry("500x300+262+150")
                # newFrame.resizable(False,False)
                #newFrame.grab_set()

                def increase_quantity():
                    
                    if(self.quantity < 4):
                        self.quantity += 1
                        newlabel2.configure(text=f"{self.quantity}")
                    if(self.quantity == 4):
                        newbutton2.configure(state="disable")
                    elif(self.quantity == 1):
                        newbutton4.configure(state="normal")
                        newbutton1.configure(state="normal")

                def decrease_quantity():
                    
                    if(self.quantity > 0):
                        self.quantity -= 1
                        newlabel2.configure(text=f"{self.quantity}")
                    if(self.quantity == 0):
                        newbutton1.configure(state="disable")
                        newbutton4.configure(state="disable")
                    elif(self.quantity == 3):
                        newbutton2.configure(state="normal")

                def cancel():
                    #newFrame.grab_release()
                    newFrame.destroy()

                def confirm():
                    if(self.quantity != 0):
                        self.update_ordered_food_list()
                        print(self.ordered_food_list)
                        #newFrame.grab_release()
                        newFrame.destroy()
                        self.cancelbutton.configure(state="normal")
                        self.orderbutton.configure(state="disable",text="Ordered",fg_color="Green")
                    
                
                newlabel = ct.CTkLabel(newFrame,text="Enter Quantity",width=500,height=50,font=("Times",20,"bold","italic"))
                newlabel.grid(row=0,column=0,columnspan=5,pady=20)
                newbutton1 = ct.CTkButton(newFrame,text="-",width=50,height=50,command=decrease_quantity)
                newbutton1.grid(row=1,column=1,padx = 0,pady=20)
                newlabel2 = ct.CTkLabel(newFrame,text=f"{self.quantity}",width=80,height=50,font=("Times",20,"bold","italic"))
                newlabel2.grid(row=1,column=2,padx = 10,pady=20)
                newbutton2 = ct.CTkButton(newFrame,text="+",width=50,height=50,command=increase_quantity)
                newbutton2.grid(row=1,column=3,padx = 0,pady=20)
                newbutton3 = ct.CTkButton(newFrame,text="Cancel",width=80,height=50,command=cancel)
                newbutton3.grid(row=2,column=0,columnspan=2,padx=10)
                newbutton4 = ct.CTkButton(newFrame,text="Confirm",width=80,height=50,command=confirm,state="disable")
                newbutton4.grid(row=2,column=3,columnspan=2,padx=10)
        
        def cancel_order():
            if(self.cancelbutton.cget("state") == "normal"):
                discardi = 0
                for i in self.ordered_food_list:
                    if(self.ordered_food_list[i][0] == self.name+" "+self.category):
                        discardi = i
                        break
                self.ordered_food_list.pop(discardi)
                self.orderbutton.configure(text = "Order",state="normal",fg_color="#1874CD")
                self.cancelbutton.configure(state="disable")

        subframe = ct.CTkFrame(self.frame,height=50,width=500,border_width=3,border_color="turquoise3")
        subframe.pack(pady=10)
        #label
        lb1 = ct.CTkLabel(subframe,text=f"{self.name} - Rs.{self.price}",height=70,width=200,font=("Times",18,"bold","italic"))
        lb1.grid(row=0,column=0,rowspan=2,padx=10,pady=10)
        #Order Button
        self.orderbutton = ct.CTkButton(subframe,text = "Order",height=40,width=150,state="normal",command=order)
        self.orderbutton.grid(row=0,column=1,padx=10,pady=5)
        #Cancel Button
        self.cancelbutton = ct.CTkButton(subframe,text = "Cancel",height=40,width=150,state="disable",command=cancel_order)
        self.cancelbutton.grid(row=1,column=1,padx=10,pady=5)

        if(__name__!="__main__"):
            self.check_for_ordered_food()
        

class FoodFrame:

    def __init__(self,iframe,iname,iordered_food_list,irow,icolumn,iroot):
        self.frame = iframe
        self.name = iname
        self.ordered_food_list = iordered_food_list
        self.row = irow
        self.column = icolumn
        self.root = iroot
    
    def create_foood_frame(self):

        my_fr = ct.CTkFrame(self.frame,height=200,width=600,border_width=3,border_color="turquoise2")
        my_fr.grid(row=self.row,column=self.column)
        my_lb = ct.CTkLabel(my_fr,text=f"{self.name}",height=50,width=400,fg_color="DeepSkyBlue3",font=("Times",20,"bold","italic"))
        my_lb.pack(pady=10,padx=45)

        if(self.name == "Fried Rice" or self.name == "Kottu" or self.name == "Noodles" or self.name == "Biriyani"):

            subframe1 = FoodSubFrame(my_fr,"Chicken","300",self.root,self.ordered_food_list,self.name)
            subframe1.create_food_sub_frame()
        
            if(self.name == "Fried Rice" or self.name == "Kottu" or self.name == "Noodles"):

                subframe2 = FoodSubFrame(my_fr,"Egg","300",self.root,self.ordered_food_list,self.name)
                subframe2.create_food_sub_frame()
                subframe3 = FoodSubFrame(my_fr,"SeaFood","300",self.root,self.ordered_food_list,self.name)
                subframe3.create_food_sub_frame()
                subframe4 = FoodSubFrame(my_fr,"Mix","300",self.root,self.ordered_food_list,self.name)
                subframe4.create_food_sub_frame()
                subframe5 = FoodSubFrame(my_fr,"Veggie","300",self.root,self.ordered_food_list,self.name)
                subframe5.create_food_sub_frame()
        
                if(self.name == "Kottu"):

                    subframe6 = FoodSubFrame(my_fr,"Cheese Chicken","300",self.root,self.ordered_food_list,self.name)
                    subframe6.create_food_sub_frame()
        else:
            subframe1 = FoodSubFrame(my_fr,"Water","0",self.root,self.ordered_food_list,"")
            subframe1.create_food_sub_frame()
            subframe1 = FoodSubFrame(my_fr,"Lemon Juice","200",self.root,self.ordered_food_list,"")
            subframe1.create_food_sub_frame()
            subframe1 = FoodSubFrame(my_fr,"Mango Juice","200",self.root,self.ordered_food_list,"")
            subframe1.create_food_sub_frame()
            subframe1 = FoodSubFrame(my_fr,"Ice Coffee","250",self.root,self.ordered_food_list,"")
            subframe1.create_food_sub_frame()



class MenuPage:

    def __init__(self,iroot,ifood_list):
        self.root = iroot
        self.ordered_food_list = ifood_list
        
    
    def run(self):

        
        #self.root.overrideredirect(True)

        def goto_nextpage():

            for widject in self.root.winfo_children():
                widject.destroy()
            
            #self.root.attributes("-fullscreen",True)
            c = CheckoutPage(self.root,self.ordered_food_list)
            c.run()
            

        self.root.title("ROBO")
        self.root.geometry(f"1024x600+0+0")
        self.root.attributes("-fullscreen",True)
        myFrame = ct.CTkScrollableFrame(self.root,orientation="vertical",width=1024,height=600,
                                        label_text="MENU",
                                        border_width=3,
                                        border_color="turquoise1",
                                        label_font=("Times",25,"bold","italic"))
        myFrame.pack()

        riceframe = FoodFrame(myFrame,"Fried Rice",self.ordered_food_list,0,0,self.root)
        riceframe.create_foood_frame()
        noodlesframe = FoodFrame(myFrame,"Noodles",self.ordered_food_list,0,1,self.root)
        noodlesframe.create_foood_frame()
        kottuframe = FoodFrame(myFrame,"Kottu",self.ordered_food_list,1,0,self.root)
        kottuframe.create_foood_frame()

        my_fr = ct.CTkFrame(myFrame,height=200,width=600)
        my_fr.grid(row=1,column=1,padx=10,pady=40)

        biriyaniframe = FoodFrame(my_fr,"Biriyani",self.ordered_food_list,0,0,self.root)
        biriyaniframe.create_foood_frame()
        hiddenlbl = ct.CTkLabel(my_fr,text="")
        hiddenlbl.grid(row=1,column=0,pady=10)
        drinksframe = FoodFrame(my_fr,"Drinks",self.ordered_food_list,2,0,self.root)
        drinksframe.create_foood_frame()

        ContinueButton = ct.CTkButton(myFrame,text = "Continue",height=50,width=200,font=("Times",25,"bold","italic"),command=goto_nextpage)
        ContinueButton.grid(row=2,column=0,columnspan=2,padx=10)

        self.root.mainloop()

if(__name__== "__main__"):
    root = ct.CTk()
    m = MenuPage(root,{})
    m.run()