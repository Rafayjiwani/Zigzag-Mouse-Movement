import pyautogui
import time

def zigzag_move_mouse(count):
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    # Define the circle parameters
    zigzag_height = min(screen_width, screen_height) // 2
    zigzag_width = screen_width // 4
    zigzag_speed = 100

    for i in range(count):
        x = center_x + (-1) ** i * zigzag_width // 2
        y = center_x + zigzag_height * (i / zigzag_width)
        pyautogui.moveTo(x, y, duration=0.2, _pause=False) 
        time.sleep(1 / zigzag_speed)
        y = center_y + zigzag_height * (i / zigzag_width) - 20
        pyautogui.moveTo(x, y, duration=0,_pause=False) 

zigzag_move_mouse(4)