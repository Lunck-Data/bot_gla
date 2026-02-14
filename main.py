
import AbrirMarket
import Venda
import time
import Bau
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def menor(menor):
    menor = menor.replace(".","")
    try:
        menor = int(menor)
        print(menor)
        return menor
    except:
        pass

time.sleep(10)
for i in range(0,10000):

    try:
        menorPaella, vendedorPaella = AbrirMarket.verificarPrecoPaella()

        menorPrecoPaella = menor(menorPaella)
        print(menor)
        
        if vendedorPaella != "Marketmaker" and menorPrecoPaella > 3448:
            print(f"Valor de {menorPrecoPaella}, temos lucro")
            print("Entrou na venda")
            Venda.vendaPaella(menorPaella)

        menorFrango, vendedorFrango = AbrirMarket.verificarPrecoFrango()

        menorPrecoFrango = menor(menorPaella)

        if vendedorFrango != "Marketmaker" and menorPrecoFrango > 2716:
            print(f"Valor de {menorPrecoFrango}, temos lucro")
            print("Entrou na venda")
            time.sleep(1)
            Venda.vendaFrango(menorFrango)

        Bau.bau()

        contador = 300

        def timer_forninho(tempo):
            print(f"Iniciando cronômetro de {tempo} segundos para ficar pronto")

            for i in range(tempo, 0, -1):
                print(f"Tempo restante: {i} ", end="\r")
                time.sleep(1)

            print("\n Ficou pronto, LETISGO")

        timer_forninho(contador)
    except:
         time.sleep(10)
         continue
