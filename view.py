#!/usr/bin/env python3
from tkinter import (BooleanVar, Button, Checkbutton, Entry, Frame, Label,
                     Scrollbar, Tk, Toplevel, messagebox)
from tkinter.constants import (ACTIVE, BOTH, CENTER, DISABLED, LEFT, NORMAL,
                               RIGHT, TOP, W, BOTTOM)

from controller import (add_new, delete_item, show_within, sort_show_vehicle,
                        update_checks, column_title, checkboxes)

from view_input import HeaderFrame
from view_autocomplete import Combobox_Autocomplete
from view_multi_listbox import Multicolumn_Listbox


def SecWindow():
    if to_edit['state'] == 'normal':
        to_edit.config(state=DISABLED)

    edit_window = Toplevel()

    ##########################################################################################
    # ToDo:
    # Implement autocomplet on vehicle
    # instead of second window, make a pane or notbook for editing
    edit_window.add_vehlabel = Label(edit_window, text='Vehicle no.')
    edit_window.add_vehlabel.pack()

    sorted_list = sort_show_vehicle()

    edit_window.add_vehicle = Combobox_Autocomplete(edit_window, sorted_list)
    edit_window.add_vehicle.pack(padx=15)

    edit_window.add_explabel = Label(
        edit_window, text='expiry date in (dd.mm.yyyy)')
    edit_window.add_explabel.pack()

    edit_window.add_expiry = Entry(edit_window)
    edit_window.add_expiry.pack(padx=15)

    def show_info(msg):
        messagebox.showinfo("This is magical!", msg)

    def del_edit():
        delete = delete_item(edit_window.add_vehicle.get())
        if delete != None:
            show_info(delete)
        edit_window.destroy()
        to_edit.config(state=NORMAL)

    def quit_edit():
        add_vehicle = add_new(edit_window.add_vehicle.get(),
                              edit_window.add_expiry.get())
        if add_vehicle != None:
            show_info(add_vehicle)
        edit_window.destroy()
        to_edit.config(state=NORMAL)

    edit_window.delete_button = Button(
        edit_window, command=del_edit, text="delete")
    edit_window.delete_button.pack(side=LEFT)

    edit_window.add_button = Button(
        edit_window, command=quit_edit, text="Add / Edit")
    edit_window.add_button.pack()

    edit_window.protocol("WM_DELETE_WINDOW", quit_edit)


root = Tk()
root.title("RoadTax Renewal Tracker")
root.configure(background='lavender')

# vehicle = ""
# expiry = ""
# informed = BooleanVar()
# inspected = BooleanVar()
# renewed = BooleanVar()

inputf = HeaderFrame(root, checkboxes(), title_text="Roadtax Renewal Tracker", 
                    input_text="day(s)")

# def on_select(data):
#     # to impliment multiple selection
#     global vehicle
#     global expiry

#     vehicle = data[0]
#     expiry = data[1]
#     informed.set(data[2])
#     inspected.set(data[3])
#     renewed.set(data[4])

#     return vehicle, informed, inspected, renewed


def show_info(msg):
    messagebox.showinfo("This is magical!", msg)

# for i in checkboxes:
#     inputf.checkboxes[i].pack()



tableframe = Frame(root)
tableframe.pack(padx=30, pady=30, fill=BOTH, side=BOTTOM)

mc = Multicolumn_Listbox(tableframe, column_title(), stripped_rows=("white", "lavender"),
                        cell_anchor="center", height=20)

scrollbar = Scrollbar(tableframe)
scrollbar.config(command=mc.interior.yview)

scrollbar.pack(fill=BOTH, side=RIGHT)

mc.interior.config(yscrollcommand=scrollbar.set)
mc.interior.pack()


# mc.table_data = show_within(entry.get())

# chkbox1 = Checkbutton(inputframe, text="Informed",
#                       variable=informed, bg='lavender')
# chkbox2 = Checkbutton(inputframe, text="Inspected",
#                       variable=inspected, bg='lavender')
# chkbox3 = Checkbutton(inputframe, text="Renewed",
#                       variable=renewed, bg='lavender')


# def callback(event):

#     try:
#         # update = update_checks(
#         #     vehicle, expiry, informed.get(), inspected.get(), renewed.get())
#         # entry.get()
#         # mc.table_data = show_within(entry.get())
#         if update != None:
#             show_info(update)
#         return entry.get()
#     except ValueError:
#         show_info("Invalid input, Number only la!!!")
#         send.config(state=NORMAL)
#         pass


# send = Button(inputframe, padx=10, text="Update!")
# inputframe.bind("<Return>", callback)
# send.bind("<Button-1>", callback)

to_edit = Button(root, text='Edit', command=SecWindow, width=15)
to_edit.config(state=ACTIVE)
to_edit.pack(side=TOP, anchor=W, padx=40)


# send.pack(side=LEFT)
# chkbox3.pack(side=RIGHT, anchor=W, pady=1, padx=1)
# chkbox2.pack(side=RIGHT, anchor=W, pady=1, padx=1)
# chkbox1.pack(side=RIGHT, anchor=W, pady=1, padx=1)


root.mainloop()
