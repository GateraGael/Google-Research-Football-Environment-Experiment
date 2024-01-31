import pyautogui
import time

start_time = time.time()

def convert(seconds):
    return time.strftime("%Mm%Ss", time.gmtime(seconds))

def take_amount_screenshots(num_screenshots, step_num, output_path):
    
    time_elapsed = time.time() - start_time
    
    Minutes_Seconds_Now = convert(time_elapsed)
    for i in range(num_screenshots):
        #savesceenshot directly to disk
        pyautogui.screenshot(output_path + Minutes_Seconds_Now + ".png")
        i += 1

