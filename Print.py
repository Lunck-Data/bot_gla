import pyautogui
import time

print("1. Coloque o mouse no CANTO SUPERIOR ESQUERDO da área do preço e aguarde...")
time.sleep(4)
x1, y1 = pyautogui.position()
print(f"Ponto 1 registrado: {x1, y1}")

print("\n2. Agora coloque no CANTO INFERIOR DIREITO da área do preço...")
time.sleep(4)
x2, y2 = pyautogui.position()
print(f"Ponto 2 registrado: {x2, y2}")

largura = x2 - x1
altura = y2 - y1

print("-" * 30)
print(f"Sua Região (Region) é: (x={x1}, y={y1}, largura={largura}, altura={altura})")
print(f"Código pronto: region=({x1}, {y1}, {largura}, {altura})")