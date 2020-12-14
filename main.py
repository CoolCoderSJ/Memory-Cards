import random
import time
from tkinter import Tk, Button, DISABLED, messagebox


def close_window(self):
    root.destroy()
    
def show_symbol(x, y): 
    global first
    global previousX, previousY
    global pairs
    global moves
    buttons[x, y]['text'] = button_symbols[x, y] 
    buttons[x, y].update_idletasks()
    if first: 
        previousX = x
        previousY = y
        first = False
        moves += 1
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]['text'] != buttons[x, y]['text']: 
            time.sleep(1)
            buttons[previousX, previousY]['text'] = ''
            buttons[x, y]['text'] = ''
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED 
            pairs += 1
            if pairs == len(buttons)/2:
                print("You finished. Your number of moves was: " + str(moves))
                messagebox.showinfo("Memory Cards Info", "You finished. Your number of moves was: " + str(moves), command=root.destroy())
        first = True

def game_end():
  if all(value==DISABLED for value in buttons.values()):
    return True



root = Tk()
root.title('Matchmaker')
buttons = {}
first = True
previousX = 0
previousY = 0
moves = 0
pairs = 0
button_symbols = {}
symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
 u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728'] 
random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=3, height=3) 
        button.grid(column=x, row=y)
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()

if not game_end():
  root.mainloop()
