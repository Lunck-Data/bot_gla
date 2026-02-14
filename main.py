import MarketCompra
import MarketVenda
import CompraVenda
import time
import Bau
import schedule
import Deslogar
import reset
import CheckTelas

# Agendamento simples e direto
schedule.every().day.at("10:20").do(Deslogar.quit)

contador = 241

def timer_forninho(tempo):
        print(f"Iniciando cronômetro de {tempo} segundos para voltar ao trabalho")

        for i in range(tempo, 0, -1):
            print(f"Tempo restante: {i} ", end="\r")
            time.sleep(1)

        print("\n AO TRABALHO, LETISGO")

def menosUm(menorCompra):
    menorCompra = menorCompra.replace(".", "")
    try:
        menorCompra = int(menorCompra) + 1
        menorCompra = str(menorCompra)
        return menorCompra
    except ValueError:
        return

def igual(menorVenda):
    menorVenda = menorVenda.replace(".", "")
    try:
        menorVenda = int(menorVenda) - 1
        menorVenda = str(menorVenda)
        return menorVenda
    except ValueError:
        return

quantidade = 1
lucroMinimo = 500

time.sleep(3)

nomeItem = ["Gema", "Cristal Radiante"]

while 1 == 1:
    schedule.run_pending()
    CheckTelas.checagemDeTelas()
    for nome in nomeItem:
        try:
            menorCompra, vendedorCompra = MarketCompra.ChecarCompra(nome)
            menorVenda, vendedorVenda = MarketVenda.ChecarVenda(nome)
            menorCompra = menosUm(menorCompra)
            menorVenda = igual(menorVenda)
            print(f"Margem de lucro {nome}: {float(menorVenda)*0.97 - float(menorCompra)*0.97}")
            if (float(menorVenda)*0.97 - float(menorCompra)*0.97) > lucroMinimo:
                if not vendedorCompra == "Marketmaker":
                    CompraVenda.EfetuarCompra(menorCompra, nome, quantidade)
                    time.sleep(1)
                if not vendedorVenda == "Marketmaker":
                    CompraVenda.EfetuarVenda(menorVenda, nome, quantidade)
                    time.sleep(1)
            else:
                print(f"Não vale a pena, lucro de {float(menorVenda)*0.97 - float(menorCompra)*0.97}")
        except TypeError:
            pass
    contador += 1
    print(f"Estamos na volta {contador}/240")

    if contador >= 240:
        reset.resetMarket()
        contador = 0
    Bau.bau()
    timer_forninho(30)