#custom title bar for tkinter

from tkinter import Tk, Frame, Button, Canvas

root = Tk()

# def move_window(event):
#     root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
#
# root.overrideredirect(True) # turns off title bar, geometry
root.overrideredirect(0) # turns off title bar, geometry

root.geometry('400x20') # set new geometry

# # make a frame for the title bar
# title_bar = Frame(root, bg='white', relief='raised', bd=2)
#
# # put a close button on the title bar
# close_button = Button(title_bar, text='Close this Window', command=root.destroy)
#
# # a canvas for the main area of the window
# window = Canvas(root, bg='black')
#
# # pack the widgets
# title_bar.pack(expand=1, fill="x")
# close_button.pack(side="right")
# window.pack(expand=1, fill="both")
#
# # bind title bar motion to the move window function
# title_bar.bind('<B1-Motion>', move_window)

root.mainloop()