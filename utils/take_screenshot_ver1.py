import pyautogui

def take_amount_screenshots(num_screenshots, step_num, output_path):
    for i in range(num_screenshots):
        #savesceenshot directly to disk
        pyautogui.screenshot(output_path+f"{str(step_num)}"+f"{i}"+".png")
        i += 1

