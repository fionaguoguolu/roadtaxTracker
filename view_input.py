from tkinter import (BooleanVar, Button, Checkbutton, Entry, Frame, Label,
                     Scrollbar, Tk, Toplevel, messagebox)

from tkinter.constants import (ACTIVE, BOTH, CENTER, DISABLED, LEFT, NORMAL,
                               RIGHT, TOP, W)


class HeaderFrame(Frame):
    def __init__(self, master, checkboxeslabel, title_text=None, input_text=None, 
                font=None, data=None, command=None, background=None):

        if title_text is not None:
            self._title_text = title_text
        else:
            self._title_text = "Untitled"
            
        if input_text is not None:
                self._input_text = input_text
        else:
            self._input_text = "Untitled"  

        if font is not None:
            self._font = font
        else:
            self._font = ("Courier", 24)

        if background is not None:
            self._background = background
        else:
            self._background = 'lavender'

        self._checkboxeslabel = checkboxeslabel
        self._number_of_checkboxes = len(checkboxeslabel)

        
        for i in range(0, self._number_of_checkboxes):
            self._checkboxeslabel[i] =  BooleanVar()
            Checkbutton(master, text=checkboxeslabel[i], 
                variable=self._checkboxeslabel[i], bg=self._background)

        self.title = Label(master, font=self._font, text=self._title_text, bg=self._background)
        self.input_label = Label(master, text=self._input_text, bg=self._background)
        self.entry = Entry(master)

        self.title.pack(side=LEFT, padx=40)
        self.input_label.pack(fill=BOTH, side=LEFT)

        # self.entry.insert()
        self.entry.focus_set()

        if data is not None:
            self._data = data

        if command is not None:
            self._command = command
            self.bind()

        # def on_select(data):
        # # to impliment multiple selection
        #     global vehicle
        #     global expiry

        #     vehicle = data[0]
        #     expiry = data[1]
        #     for i in range(0, self._number_of_checkboxes):
        #         self.checkboxes[i].set(data[i+2])
        #         return checkboxes

        #     return vehicle, 



    