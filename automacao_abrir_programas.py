import pyautogui as pa
import win32com.client as win32
pa.PAUSE = 1

programas = ["Intellij", "Chrome", "Telegram", "Brave", "WhatsApp", "WhatsApp Beta", 
            "Spotify", "Notion"]

for programa in programas:
    print("Abrindo o", programa, "...")
    pa.press("win")
    pa.write(programa)
    pa.press("ENTER")