#! python3
import queue
import pyautogui
import sys
import tkinter as tk
from tkinter import Label, StringVar, Listbox, Scrollbar
from pyautogui import sleep
from pynput import keyboard
from queue import Queue

root = tk.Tk(className='JXTECH')
root.geometry("400x200")
position_str = ""
listbox_entries = []
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_widget = Listbox(root, yscrollcommand=scrollbar.set)
queue = Queue()


def on_release(key):
    global position_str, listbox_entries
    x, y = pyautogui.position()
    position_str = f'[{str(x).rjust(4)},{str(y).rjust(4)}]'


def main():
    global position_str, listbox_widget, listbox_entries
    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_release=on_release)
    listener.start()
    try:
        while True:
            if position_str != "":
                listbox_widget.insert(tk.END, position_str)
            position_str = ""
            root.update()
    except KeyboardInterrupt:
        print('\n')


if __name__ == "__main__":
    msg = StringVar()
    msg.set(f'Press any key to record x,y pos')
    label = Label(root, textvariable=msg)
    label.pack()
    listbox_widget.pack(fill=tk.BOTH)
    scrollbar.config(command=listbox_widget.yview)
    # Collect events until released
    main()
    root.mainloop()
