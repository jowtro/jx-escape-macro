from classes.action import Action
from pyautogui import sleep
import pyautogui


class Mining(Action):

    def __init__(self, name="Mining", rock=[0, 0]):
        super().__init__(name)
        self.orebox = [0, 0]
        self.rock = rock
        self.metal_box_found = False
        # TODO add function to scan dir looking for files with a prefix
        self.list_burst_xp = [
            "./assets/xp_burst2.png", "./assets/xp_burst.png"]
        self.image_found = False

    def find_and_set_orebox(self):
        pos = super().find_image("./assets/rune_ore_chest.png")
        # has found
        if pos[0] != -1:
            self.orebox[0] = pos[0] + 30
            self.orebox[1] = pos[1] + 15
            self.metal_box_found = True
        else:
            self.metal_box_found = False
            raise Exception("Ore box not found exception !")

    def look_for_bonus_xp(self):
        for img in self.list_burst_xp:
            pos_xp = super().find_image(img)
            if super().has_found_img(pos_xp):
                self.image_found = True
                sleep(1)
                super().go_click(pos_xp[0], pos_xp[1],
                                 2, pyautogui.easeInBounce)
            else:
                self.image_found = False
