import webbrowser
import pyautogui
from time import sleep
from win10toast import ToastNotifier 

n = ToastNotifier()

while True:
    File = open("C:/Users/XXX/AppleShortcuts/action.txt", "r+")
    Action = File.readline(2).strip("\n")
    if Action == "yt":
        webbrowser.open("https://youtube.com/")
        File.truncate(0)
    elif Action == "mc":
        MinecraftVersion = File.read().strip("\n")
        pyautogui.moveTo(x=201, y=1066)
        pyautogui.click()
        sleep(5)
        pyautogui.moveTo(x=299, y=83)
        pyautogui.click()
        if MinecraftVersion == "1.15":
            pyautogui.moveTo(x=1417, y=201)
            pyautogui.click()
        else:
            n.show_toast("AppleShortcuts", f"Version {MinecraftVersion} is unsuppurted!", duration = 10)
        File.truncate(0)
    else:
        pass
    File.close()
