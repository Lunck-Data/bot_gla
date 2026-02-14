import pyautogui
import time
import keyboard

# Tempo para você dar alt-tab para o jogo
print("O bot começa em 5 segundos...")
time.sleep(3)

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print(currentMouseX, currentMouseY)

