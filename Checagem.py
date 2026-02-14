import pyautogui
import pytesseract
import cv2
import numpy as np

# Informe ao Python onde o Tesseract está instalado
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# def ler_preco_mercado(x, y, largura, altura):
#     # 1. Tira um print da região do preço
#     screenshot = pyautogui.screenshot(region=(x, y, largura, altura))
    
#     # 2. Converte para um formato que o OpenCV entende
#     imagem_rgb = np.array(screenshot)
#     imagem = cv2.cvtColor(imagem_rgb, cv2.COLOR_RGB2BGR)
    
#     # 3. Tratamento de imagem (Cinza e Contraste) para facilitar o OCR
#     imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
#     _, imagem_binaria = cv2.threshold(imagem_cinza, 150, 255, cv2.THRESH_BINARY_INV)
    
#     # 4. Tenta ler o texto
#     texto = pytesseract.image_to_string(imagem_binaria, config='--psm 6 digits')
    
#     return texto.strip()

def ler_preco_mercado(x, y, largura, altura):
    screenshot = pyautogui.screenshot(region=(x, y, largura, altura))
    imagem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # 1. Escala de cinza e Redimensionamento (3x a 4x)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_maior = cv2.resize(imagem_cinza, None, fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)
    
    # 2. Aumentar o contraste (Torna o que é cinza claro em branco e o que é cinza escuro em preto)
    _, imagem_binaria = cv2.threshold(imagem_maior, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 3. Operação Morfológica (Opcional: remove ruídos pontuais)
    kernel = np.ones((2, 2), np.uint8)
    imagem_final = cv2.morphologyEx(imagem_binaria, cv2.MORPH_CLOSE, kernel)

    # 4. OCR com PSM 6 ou 13
    # PSM 6: Assume um bloco único de texto
    # PSM 13: Trata a imagem como uma única linha de texto ignorando hacks de layout
    config_ocr = '--psm 6 -c tessedit_char_whitelist=0123456789.,'
    texto = pytesseract.image_to_string(imagem_final, config=config_ocr)
    
    return texto.strip()


def ler_nick_jogador(x, y, largura, altura):
    # 1. Tira o print da região
    screenshot = pyautogui.screenshot(region=(x, y, largura, altura))
    
    # 2. Converte para OpenCV
    imagem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # 3. Tratamento para Texto (Nicks costumam ter cores variadas)
    # Converter para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Aumentar o tamanho da imagem (ajuda MUITO na leitura de letras pequenas)
    imagem_maior = cv2.resize(imagem_cinza, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    # 4. OCR focado em Strings (PSM 7 é ideal para "uma linha de texto")
    # Removido o 'digits' para permitir letras
    config_ocr = '--psm 7' 
    texto = pytesseract.image_to_string(imagem_maior, config=config_ocr)
    
    return texto.strip()

