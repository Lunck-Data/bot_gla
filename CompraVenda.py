import pyautogui
import time
import keyboard

#COMPRA
def EfetuarCompra(menorCompra, nomeItem, quantidade):
    time.sleep(3)

    #Abre o mercado
    pyautogui.moveTo(680, 489)
    pyautogui.click()

    #Publicar
    pyautogui.moveTo(614, 231)
    pyautogui.click()

    time.sleep(0.5)

    #Botão Comprar
    pyautogui.moveTo(720, 636)
    pyautogui.click()

    #Botão Pesquisar
    pyautogui.moveTo(447, 287)
    pyautogui.click()

    #Pesquisar item compra
    pyautogui.write(nomeItem)

    time.sleep(1)

    if nomeItem == "Gema":
        #Botão Comprar
        pyautogui.moveTo(436, 345)
        pyautogui.click()
    else:
        #Botão Comprar
        pyautogui.moveTo(370, 345)
        pyautogui.click()

    #Botão Pesquisar
    pyautogui.moveTo(808, 310)
    pyautogui.click()

    pyautogui.write(menorCompra)

    #Adicionar quantidade
    pyautogui.moveTo(752, 337)
    for i in range(1, quantidade):
        pyautogui.click()

    #Criar Pedido
    pyautogui.moveTo(805, 580)
    pyautogui.click()

        #Criar
    pyautogui.moveTo(676, 502)
    pyautogui.click()

       #Criei o ordem de compra
    pyautogui.moveTo(702, 426)
    pyautogui.click()

    #Fechar aba
    pyautogui.moveTo(1012, 194)
    pyautogui.click()

#VENDA
def EfetuarVenda(menorVenda, nomeItem, quantidade):
    #Abre o mercado
    pyautogui.moveTo(680, 489)
    pyautogui.click()

    #Publicar
    pyautogui.moveTo(614, 231)
    pyautogui.click()

    time.sleep(0.5)

    #Botao vender
    pyautogui.moveTo(841, 634)
    pyautogui.click()

    if nomeItem == "Gema":
        #Gema
        pyautogui.moveTo(734, 586)
        pyautogui.click()

        #Zerar quantidade
        pyautogui.moveTo(616, 333)
        pyautogui.click()

        pyautogui.moveTo(883, 334)
        for i in range(1, quantidade):
            pyautogui.click()

        #Colocar preco
        pyautogui.moveTo(697, 308)
        pyautogui.click()

        pyautogui.write(menorVenda)

        #Vender
        pyautogui.moveTo(624, 586)
        pyautogui.click()

        #Confirmação
        pyautogui.moveTo(695, 502)
        pyautogui.click()

        #Fechar aba
        pyautogui.moveTo(1012, 194)
        pyautogui.click()

    else:

        #Selecionar
        pyautogui.moveTo(489, 293)
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
            localizacao = pyautogui.locateOnScreen(f"{foto}", confidence=0.65, region=(976, 70, 373, 671))
            pyautogui.moveTo(localizacao)
            pyautogui.click()
        except pyautogui.ImageNotFoundException:
            try:
                localizacao = pyautogui.locateOnScreen(f"{foto1}", confidence=0.65, region=((976, 70, 373, 671)))
                pyautogui.moveTo(localizacao)
                pyautogui.click()
            except pyautogui.ImageNotFoundException:
                print("A imagem não está na tela no momento.")
                localizacao = None

                    #Fechar aba
                pyautogui.click()
                pyautogui.moveTo(1012, 194)
                pyautogui.click()

                return

        #Zerar quantidade
        pyautogui.moveTo(615, 332)
        pyautogui.click()

        pyautogui.moveTo(884, 335)
        for i in range(0,4):
            pyautogui.click()

        #Colocar preco
        pyautogui.moveTo(698, 308)
        pyautogui.click()

        pyautogui.write(menorVenda)

        #Vender
        pyautogui.moveTo(627, 591)
        pyautogui.click()

        #Confirmação
        pyautogui.moveTo(689, 498)
        pyautogui.click()

        #Fechar aba
        pyautogui.moveTo(1015, 197)
        pyautogui.click()


