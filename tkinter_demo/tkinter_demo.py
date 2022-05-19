
import tkinter as tk
from random import *


#.open() will open the file if it exist else create it
with open("jokes.txt","w+") as f:


    joke = f.read()
    
    # check if the element returned from the file is empty
    #if so write some default jokes to the file
    if len(joke) == 0:
        f.write("this is not funny \nseriously try it \nI don't know but it working \n")


def joke_generator():
    """generate random jokes from the file jokes.txt"""

    with open("jokes.txt", "r+") as f:
        jokes = f.readlines()
        lbl_display_joke.config( text = choice(jokes))


def save_joke():
    """save new joke to the file jokes"""

    with open("jokes.txt", "r+") as f:

        #get the txt entered in the txt box
        new_joke = txt_joke.get(1.0, tk.END)
        #check if the text box contain any text
        if len(new_joke)>2:
            #write the text to the file
            f.write(new_joke)

            #clear the text box
            txt_joke.delete('1.0', tk.END)
        else:
            #otherwise display an error msg
            print("Invalid or No text to save")




#create the main window
window = tk.Tk()

#setup some basic geometry for out window
window.rowconfigure([0, 1, 2, 3], minsize=50, weight=10)
window.columnconfigure(0, minsize=50, weight=1)


#create and add the button to the main window to generate new jokes when pressed
btn_generate = tk.Button(master=window, text="Generate a Random Joke", command=joke_generator)
btn_generate.grid(row=0, column=0)

#create and add a label to the main window to display the jokes
lbl_display_joke = tk.Label(master=window, text="No joke as been generated yet", bg="white")
lbl_display_joke.grid(row=1, column=0)

#create and add a label to the main window on top of the text field
lbl_add_joke = tk.Label(master=window, text="Enter new Joke")
lbl_add_joke.grid(row=2, column=0)

#create and add a text bot to the main window that will serve as entry field for new jokes
txt_joke = tk.Text(master=window) 
txt_joke.grid(row=3, column=0)

#create and add the button to the main window for saving input
btn_save = tk.Button(master=window, text="Save", command=save_joke)
btn_save.grid(row=4, column=0)

#run the main loop
window.mainloop()



"""
We can convert any tkinter application to an exe compatible file format using the PyInstaller package in Python.
To work with pyinstaller, first install the package in the environment by using the following command,
pip install pyinstaller
Once installed, we can follow the steps to convert a Python Script File (contains a Tkinter application file) to an Executable file.
Install pyinstaller using pip install pyinstaller in Windows operating system. Now, type pyinstaller --onefile -w filename and press Enter.
Now, check the location of the file (script file) and you will find a dist folder which contains the executable file in it.
When we run the file, it will display the window of the tkinter application. 
From: https://www.tutorialspoint.com/converting-tkinter-program-to-exe-file"""
