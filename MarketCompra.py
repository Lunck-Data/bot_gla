import pyautogui
import time
import keyboard
import Checagem

def ChecarCompra(nomeItem):
    #Abre o mercado
    pyautogui.moveTo(966, 623)
    pyautogui.click()

    #Pedido de compra
    pyautogui.moveTo(1025, 344)
    pyautogui.click()

    time.sleep(0.5)

    #Clicar no nome
    pyautogui.moveTo(1093, 377)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()

    #Pesquisar item compra
    pyautogui.write(nomeItem)

    pyautogui.moveTo(1240, 376)
    pyautogui.click()

    time.sleep(1)
    preco_detectado = Checagem.ler_preco_mercado(1181, 424, 92, 24)
    print(f"Menor preço de compra do {nomeItem}: {preco_detectado}")

    vendedor = Checagem.ler_nick_jogador(957, 417, 133, 31)
    print(vendedor)

    #Fechar aba
    pyautogui.moveTo(1289, 300)
    pyautogui.click()

    time.sleep(1)
    return preco_detectado, vendedor