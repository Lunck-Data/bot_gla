import pyautogui
import time
import keyboard

#COMPRA
def EfetuarCompra(menorCompra, nomeItem, quantidade):
    time.sleep(3)

    #Abre o mercado
    pyautogui.moveTo(966, 623)
    pyautogui.click()

    #Publicar
    pyautogui.moveTo(881, 336)
    pyautogui.click()

    time.sleep(0.5)

    #Botão Comprar
    pyautogui.moveTo(997, 743)
    pyautogui.click()

    #Botão Pesquisar
    pyautogui.moveTo(709, 395)
    pyautogui.click()

    #Pesquisar item compra
    pyautogui.write(nomeItem)

    time.sleep(1)

    if nomeItem == "Gema":
        #Botão Comprar
        pyautogui.moveTo(710, 447)
        pyautogui.click()
    else:
        #Botão Comprar
        pyautogui.moveTo(650, 453)
        pyautogui.click()

    #Botão Pesquisar
    pyautogui.moveTo(1072, 419)
    pyautogui.click()

    pyautogui.write(menorCompra)

    #Adicionar quantidade
    pyautogui.moveTo(1258, 442)
    for i in range(1, quantidade):
        pyautogui.click()

    #Criar Pedido
    pyautogui.moveTo(1082, 686)
    pyautogui.click()

        #Criar
    pyautogui.moveTo(958, 607)
    pyautogui.click()

       #Criei o ordem de compra
    pyautogui.moveTo(974, 536)
    pyautogui.click()

    #Fechar aba
    pyautogui.moveTo(1289, 300)
    pyautogui.click()

#VENDA
def EfetuarVenda(menorVenda, nomeItem, quantidade):
    #Abre o mercado
    pyautogui.moveTo(966, 623)
    pyautogui.click()

    #Publicar
    pyautogui.moveTo(881, 336)
    pyautogui.click()

    #Botao vender
    pyautogui.moveTo(1121, 742)
    pyautogui.click()

    if nomeItem == "Gema":
        #Gema
        pyautogui.moveTo(1013, 690)
        pyautogui.click()

        #Zerar quantidade
        pyautogui.moveTo(889,441)
        pyautogui.click()

        pyautogui.moveTo(1162, 439)
        for i in range(1, quantidade):
            pyautogui.click()

        #Colocar preco
        pyautogui.moveTo(938,418)
        pyautogui.click()

        pyautogui.write(menorVenda)

        #Vender
        pyautogui.moveTo(904,693)
        pyautogui.click()

        #Confirmação
        pyautogui.moveTo(961,612)
        pyautogui.click()

        #Fechar aba
        pyautogui.moveTo(1289, 300)
        pyautogui.click()

    else:

        #Selecionar
        pyautogui.moveTo(767, 397)
        pyautogui.click()

        foto = nomeItem + ".png"
        foto = foto.replace(" ", "")

        foto1 = nomeItem + "1.png"
        foto1 = foto1.replace(" ", "")

        time.sleep(2)
        # try:
        #     localizacao = pyautogui.locateOnScreen(f"{foto}", confidence=0.6, region=(1720, 363, 199, 664))
        #     pyautogui.moveTo(localizacao)
        #     pyautogui.click()
        # except pyautogui.ImageNotFoundException:
        #     print("A imagem não está na tela no momento.")
        #     localizacao = None

        #         #Fechar aba
        #     pyautogui.click()
        #     pyautogui.moveTo(1289, 300)
        #     pyautogui.click()

        #     return

        try:
            localizacao = pyautogui.locateOnScreen(f"{foto}", confidence=0.65, region=(1715, 216, 203, 806))
            pyautogui.moveTo(localizacao)
            pyautogui.click()
        except pyautogui.ImageNotFoundException:
            try:
                localizacao = pyautogui.locateOnScreen(f"{foto1}", confidence=0.65, region=(1715, 216, 203, 806))
                pyautogui.moveTo(localizacao)
                pyautogui.click()
            except pyautogui.ImageNotFoundException:
                print("A imagem não está na tela no momento.")
                localizacao = None

                    #Fechar aba
                pyautogui.click()
                pyautogui.moveTo(1289, 300)
                pyautogui.click()

                return

        #Zerar quantidade
        pyautogui.moveTo(889,441)
        pyautogui.click()

        pyautogui.moveTo(1162, 439)
        for i in range(1, quantidade):
            pyautogui.click()

        #Colocar preco
        pyautogui.moveTo(938,418)
        pyautogui.click()

        pyautogui.write(menorVenda)

        #Vender
        pyautogui.moveTo(904,693)
        pyautogui.click()

        #Confirmação
        pyautogui.moveTo(961,612)
        pyautogui.click()

        #Fechar aba
        pyautogui.moveTo(1289, 300)
        pyautogui.click()


