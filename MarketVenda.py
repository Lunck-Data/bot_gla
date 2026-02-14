import pyautogui
import time
import keyboard
import Checagem

def ChecarVenda(nomeItem):
    #Abre o mercado
    pyautogui.moveTo(680, 489)
    pyautogui.click()

    time.sleep(1)

    #Pesquisar item venda
    pyautogui.write(nomeItem)

    pyautogui.moveTo(966, 273)
    pyautogui.click()

    time.sleep(2)
    preco_detectado = Checagem.ler_preco_mercado(907, 310, 92, 35)
    print(f"Menor preço de venda do {nomeItem}: {preco_detectado}")

    vendedor = Checagem.ler_nick_jogador(684, 310, 136, 33)
    print(vendedor)

    #Fechar aba
    pyautogui.moveTo(1012, 194)
    pyautogui.click()

    time.sleep(1)
    return preco_detectado, vendedor