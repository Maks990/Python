from tkinter import *

tk = Tk()
tk.title("SSSR")
tk.geometry('400x400')
Banner = Label(tk, text = "КамЕнь~Ножницы~Бумага", font=("Times new Roman", 25))
Banner.grid(row=1)
sc = [0,0]
score = Label(tk, text = f"score: {sc[0]}:{sc[1]}", font=("Times new Roman", 16))
score.grid(row=2)

"""
ebveibvfeg
score: 1:1
Егор негр  
    
wf  wef wfe    
    
"""
tk.mainloop()