from classes.macro import Macro
import pyautogui
from pyautogui import alert, sleep
from datetime import datetime, timedelta
from python_imagesearch.imagesearch import imagesearch

class Action(Macro):

    def __init__(self,name="mining"):
        super().__init__()
        self.name = name

    @staticmethod
    def go_click(pos_x, pos_y, time, style):
        """move the mouse to the pos and click

        Args:t
            pos_x ([int]): x pos
            pos_y ([int]): y pos
            time ([int]): eg:. 2 seconds
            style ([pyautogui.function]): eg:.pyautogui.easeInBack
        """
        pyautogui.moveTo(pos_x, pos_y, 2, style)
        pyautogui.click()


    @staticmethod
    def find_image(image_path):
        """Find an image on screen

        Args:
            image_path ([str]): [file path]

        Returns:
            list[int]: [x,y]
        """
        return imagesearch(image_path)


    @staticmethod
    def has_found_img(pos):
        if pos[0] != -1:
            return True
        else:
            return False
