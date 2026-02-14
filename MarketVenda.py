import pyautogui
import time
import keyboard
import Checagem

def ChecarVenda(nomeItem):
    #Abre o mercado
    pyautogui.moveTo(966, 623)
    pyautogui.click()

    time.sleep(0.5)

    #Pesquisar item venda
    pyautogui.write(nomeItem)

    pyautogui.moveTo(1240, 376)
    pyautogui.click()

    time.sleep(1)
    preco_detectado = Checagem.ler_preco_mercado(1181, 424, 92, 24)
    print(f"Menor preço de venda do {nomeItem}: {preco_detectado}")

    vendedor = Checagem.ler_nick_jogador(957, 417, 133, 31)
    print(vendedor)

    #Fechar aba
    pyautogui.moveTo(1289, 300)
    pyautogui.click()

    time.sleep(1)
    return preco_detectado, vendedor