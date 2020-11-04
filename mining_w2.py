import pyautogui
from pyautogui import alert, sleep

metal_box = {"x": 2030,"y": 571}
rock  ={"x": 1803,"y": 469}
MAX_ITERATIONS = 9
iterations = 0

def main():
    """
                            Macro for mining
    """
    #screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
    #print(screenWidth,screenHeight)

    pyautogui.moveTo(metal_box['x'], metal_box['y'], 2, pyautogui.easeInBack)
    pyautogui.click()

    sleep(2)

    pyautogui.moveTo(rock['x'], rock['y'], 2, pyautogui.easeInBounce)
    pyautogui.click()
    #alert(text='teste', title='', button='OK')
if __name__ == "__main__":
    while iterations < MAX_ITERATIONS :
        main()
        sleep(120)
        iterations += 1
        print(f'Number of {iterations}')
    alert(text='Finished...', title='Mining', button='OK')
    