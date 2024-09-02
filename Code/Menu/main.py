import customtkinter as ct
from menu_class import MenuPage

root = ct.CTk()
#root.geometry(f"1024x600+0+0")
#root.attributes('-fullscreen',True)
m = MenuPage(root,{})
m.run()