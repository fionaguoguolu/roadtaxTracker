from tkinter import (BooleanVar, Button, Checkbutton, Entry, Frame, Label,
                     Scrollbar, Tk, Toplevel, messagebox)
from tkinter.constants import (ACTIVE, BOTH, BOTTOM, CENTER, DISABLED, LEFT,
                               NORMAL, RIGHT, TOP, E, N, S, W)


class HeaderFrame(Frame):
    def __init__(self, master, checkboxeslabel, title_text=None, input_text=None,
                 title_font=None, body_font=None, background=None):
        Frame.__init__(self, master=None)

        if title_text is not None:
            self._title_text = title_text
        else:
            self._title_text = "Untitled"

        if input_text is not None:
            self._input_text = input_text
        else:
            self._input_text = "Untitled"

        if title_font is not None:
            self._title_font = title_font
        else:
            self._title_font = ("Courier", 24)

        if body_font is not None:
            self._body_font = body_font
        else:
            self._body_font = ("Courier", 12)

        if background is not None:
            self._background = background
        else:
            self._background = 'lavender'

        self._button_width = 15

        Frame.config(self, background=self._background)
        Frame.grid(self)

        self._checkboxeslabel = checkboxeslabel
        self._number_of_checkboxes = len(checkboxeslabel)

        # for i in range(0, self._number_of_checkboxes):
        #     self._checkboxeslabel[i] = BooleanVar()
        #     Checkbutton(master, text=checkboxeslabel[i],
        #                 variable=self._checkboxeslabel[i], bg=self._background)

        self.title = Label(master, font=self._title_font, text=self._title_text,
                           bg=self._background)
        self.input_label = Label(master, font=self._body_font, text=self._input_text,
                                 bg=self._background)
        self.entry = Entry(master)
        self.entry.focus_set()
        self.entry.insert(0, '30')

        self._vehicle = ""
        self._expiry = ""
        self._informed = BooleanVar()
        self._inspected = BooleanVar()
        self._renewed = BooleanVar()

        self.chkbox1 = Checkbutton(master, text="Informed",
                                   variable=self._informed, bg=self._background)
        self.chkbox2 = Checkbutton(master, text="Inspected",
                                   variable=self._inspected, bg=self._background)
        self.chkbox3 = Checkbutton(master, text="Renewed",
                                   variable=self._renewed, bg=self._background)

        def on_select(self, data):
            # to impliment multiple selection
            self._vehicle = data[0]
            self._expiry = data[1]
            self._informed.set(data[2])
            self._inspected.set(data[3])
            self._renewed.set(data[4])

            return self._vehicle, self._informed, self._inspected, self._renewed

        self.update_btn = Button(master, text="Update", command=on_select)
        self.save_btn = Button(master, text="Save")
        self.update_btn.config(width=self._button_width)
        self.save_btn.config(width=self._button_width)

        self.title.grid(padx=40, pady=40, row=0, column=1,
                        columnspan=8, sticky=W+E+N+S)
        self.entry.grid(row=1, column=1, padx=5)
        self.input_label.grid(row=1, column=2, sticky=W, padx=5)
        self.chkbox1.grid(row=1, column=3, stick=W+E, padx=5)
        self.chkbox2.grid(row=1, column=4, stick=W+E, padx=5)
        self.chkbox3.grid(row=1, column=5, stick=W+E, padx=5)
        self.update_btn.grid(row=1, column=6, padx=5)
        self.save_btn.grid(row=1, column=7, padx=5)
