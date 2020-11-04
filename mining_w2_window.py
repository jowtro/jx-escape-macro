from time import time
import pyautogui
from pyautogui import alert, sleep
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import Label, Button, StringVar
from classes.interval import Interval
from classes.mining import Mining
root = tk.Tk(className='escape from boredom - v01')
root.geometry("200x200")

button = tk.Button(root, text="I am a button")

mining = Mining("Mining", rock=[1803, 469])
mining.set_MAX_ITERATIONS(9)
INTERVAL_TIME = 120


def has_found_img(pos):
    if pos[0] != -1:
        return True
    else:
        return False


def set_next_cycle():
    time_to_act = datetime.now() + timedelta(0, INTERVAL_TIME)
    mining.set_time_to_act(time_to_act)

def show_next_cycle():
    dt_diff =  mining.get_time_to_act() - datetime.now()
    app_status.set(f'Next cycle in: {dt_diff.seconds}s')


@Interval(interval=INTERVAL_TIME)
def main_loop():
    if mining.metal_box_found:
        Mining.go_click(
            mining.orebox[0], mining.orebox[1], 2, pyautogui.easeInBack)
        # TODO BURST XP
        mining.look_for_bonus_xp()
        sleep(2)
        Mining.go_click(mining.rock[0], mining.rock[1],
                        2, pyautogui.easeInBounce)
        mining.add_iterations(1)
    else:
        msg.set(f"Can't proceed without a orebox !")
        mining.set_iterations(9)
    set_next_cycle()


def mine():
    set_next_cycle()
    while mining.get_iterations() < mining.get_MAX_ITERATIONS():
        main_loop()
        msg.set(f'Status: Running...\n Nº iterations {mining.get_iterations()}')
        show_next_cycle()
        root.update()
        sleep(1)
    app_status.set(f'Script ended.')

if __name__ == "__main__":
    mining.find_and_set_orebox()
    start_button = Button(root, text="Start Mining", command=mine)
    start_button.pack()
    msg = StringVar()
    msg.set(f'Script started.')

    app_status = StringVar()
    app_status.set(f'All nominal.')
    app_status.set(f'Interval time set to: {INTERVAL_TIME}s')

    txt_ore_box = StringVar()
    txt_ore_box.set(f"Has found ore box ? {mining.metal_box_found}")

    label = Label(root, textvariable=msg)
    label.pack()

    lbl_ore_box = Label(root, textvariable=txt_ore_box)
    lbl_ore_box.pack()

    lbl_app_status = Label(root, textvariable=app_status)
    lbl_app_status.pack()
    root.mainloop()
    alert(text='Finished...', title='Mining', button='OK')
