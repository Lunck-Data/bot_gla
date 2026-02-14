import pyautogui
import time
import keyboard
import Checagem

def verificarPrecoPaella():
    #Abre o mercado
    pyautogui.moveTo(674, 491)
    pyautogui.click()

    time.sleep(1.5)

    #Pesquisar preço Paella
    pyautogui.write("Paella de camar")

    time.sleep(1.5)

    pyautogui.moveTo(966, 278)
    pyautogui.click()

    time.sleep(0.5)
    preco_detectado = Checagem.ler_preco_mercado(912, 316, 80, 28)
    print(f"Menor preço Paella: {preco_detectado}")

    vendedor = Checagem.ler_nick_jogador(696, 316, 120, 26)
    print(vendedor)

    #Fechar aba
    pyautogui.moveTo(1010, 192)
    pyautogui.click()

    return preco_detectado, vendedor


def verificarPrecoFrango():
    #Abre o mercado
    pyautogui.moveTo(674, 491)
    pyautogui.click()

    time.sleep(1.5)

    #Pesquisar preço Frango
    pyautogui.write("Frango Teriyaki")

    time.sleep(1.5)

    pyautogui.moveTo(966, 278)
    pyautogui.click()

    time.sleep(0.5)
    preco_detectado = Checagem.ler_preco_mercado(912, 316, 80, 28)
    print(f"Menor preço Frango: {preco_detectado}")

    vendedor = Checagem.ler_nick_jogador(696, 316, 120, 26)
    print(vendedor)

    #Fechar aba
    pyautogui.moveTo(1010, 192)
    pyautogui.click()

    return preco_detectado, vendedor
