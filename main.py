from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk

import time, os, keyboard, toml


## functions 

# simple time function for if you want to log time with event, (ignoring logging)
def logWith(*args):
    return str(( ", ".join(list(args)) ) + "  @ " + time.ctime())

# instead of returning text it will print it
def logWithOut(*args):
    print(( ", ".join(list(args)) ) + "  @ " + time.ctime())


## code that runs

print(logWith("Running"))

keyboard.add_hotkey('ctrl+shift+a', logWithOut, args=("Test", "food"))


director = "C:/windowThing/"

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Main Window")
        self.master.geometry("400x300")

        # create a drop-down menu
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        # create a "File" dropdown menu
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Save settings location", command=self.save_file)


         # create a "Settings" dropdown menu
        settings_menu = tk.Menu(menu)
        menu.add_cascade(label="Settings", menu=settings_menu)

        # add a "Advanced settings" submenu to the settings menu
        advanced_menu = tk.Menu(settings_menu)
        settings_menu.add_cascade(label="Advanced settings", menu=advanced_menu)

        # add a "Is Amazing" checkbox to the advanced settings menu
        self.is_amazing_var = tk.BooleanVar()
        self.is_amazing_var.set(False)
        advanced_menu.add_checkbutton(label="Is Amazing", variable=self.is_amazing_var)

        # add a radio button group to the advanced settings menu
        self.radio_var = tk.StringVar()
        self.radio_var.set("foo")
        advanced_menu.add_radiobutton(label="Print 'foo'", variable=self.radio_var, value="foo")
        advanced_menu.add_radiobutton(label="Set text size to 24px", variable=self.radio_var, value="size")
        advanced_menu.add_radiobutton(label="Do nothing", variable=self.radio_var, value="nothing")

        # add an "All settings" item to the settings menu
        settings_menu.add_command(label="All settings window", command=self.save_settings)


        self.makeFileData_button = tk.Button(self.master, text="Make app data", command=self.makeAppDataStuff)
        self.makeFileData_button.pack()


    def makeAppDataStuff(self):
        try:
            os.mkdir(director)
        except:
            print("Can't make dir")
        
        try:
            with open(director+"settings.toml") as f:
                f.write()
        except:
            print("Can't write to settings")
        
    def open_popup(self, popup_name):
        # create the pop-up window
        popup = tk.Toplevel(self.master)
        popup.title(popup_name)

        # add some content to the popup window
        popup_label = tk.Label(popup, text=f"This is {popup_name}!")
        popup_label.pack()

    def open_all_settings(self):
        # create the "All settings" window
        settings_window = tk.Toplevel(self.master)
        settings_window.title("All Settings")
        settings_window.geometry("400x300")

        # create a tab control
        tab_control = ttk.Notebook(settings_window)
        tab_control.pack(expand=1, fill="both")

        # create the "Settings" tab
        settings_tab = ttk.Frame(tab_control)
        tab_control.add(settings_tab, text="Settings")

        # add the current values of all settings
        self.is_amazing_label = tk.Label(settings_tab, text=f"Is Amazing: {self.is_amazing_var.get()}")
        self.is_amazing_label.pack()

        
        # create the "Change values" tab
        change_values_tab = ttk.Frame(tab_control)
        tab_control.add(change_values_tab, text="Change Values")


        self.is_amazing_checkbutton = tk.Checkbutton(change_values_tab, text="Is Amazing", variable=self.is_amazing_var)
        self.is_amazing_checkbutton.pack()

        self.radio_label = tk.Label(settings_tab, text=f"Radio2: {self.radio_var.get()}")
        self.radio_label.pack()

        foo_radio = tk.Radiobutton(change_values_tab, text="Print 'foo'", variable=self.radio_var, value="foo")
        foo_radio.pack()

        size_radio = tk.Radiobutton(change_values_tab, text="Set text size to 24px", variable=self.radio_var, value="size")
        size_radio.pack()

        nothing_radio = tk.Radiobutton(change_values_tab, text="Do nothing", variable=self.radio_var, value="nothing")
        nothing_radio.pack()

        self.did_save = tk.Label(change_values_tab, text="")
        self.did_save.pack()

        # add a "Save" button to the "Change Values" tab
        save_button = tk.Button(change_values_tab, text="Save", command=self.save_settings)
        save_button.pack()
    
    def save_settings(self):
        # apply the new settings
        is_amazing = self.is_amazing_var.get()
        radio = self.radio_var.get()

        # save the settings to a TOML file
        settings_dict = {
            "Is Amazing": is_amazing,
            "Radio": radio
        }
        with open(director+"settings.toml", "w") as f:
            toml.dump(settings_dict, f)
        
        # update the "All Settings" tab to reflect the new values
        self.is_amazing_label.config(text=f"Is Amazing: {self.is_amazing_var.get()}")
        self.radio_label.config(text=f"Radio: {self.radio_var.get()}")
        self.did_save.config(text="Saved.", fg="green")

    def save_file(self):
        # open a file dialog box for saving a file
        file_path = filedialog.asksaveasfilename(initialdir=director, initialfile="settings.toml")

        # do something with the file path
        print("Saving file to:", file_path)

    # create a button that opens a file dialog box for saving a file
    


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(master=root)
    app.mainloop()
