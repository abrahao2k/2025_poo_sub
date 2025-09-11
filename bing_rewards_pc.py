# REQUER O PACOTE PYAUTOGUI, instale usando:
# pip install pyautogui
# no prompt de comando

import pyautogui
import time

pyautogui.PAUSE = 1

'''
palavras = ["livro", "lapis", "caderno", "borracha", "caneta", "regua", 
    "mochila", "estojo", "carteira", "cadeira", "mesa", 
    "quadro", "apagador", "lousa", "marcador", "projetor", 
    "computador", "mouse", "teclado", "impressora", "scanner", 
    "fone", "pendrive", "carregador", "adaptador", "tablet", 
    "celular", "controle remoto", "televisao", "radio"]
'''

palavras = ["Futebol", "Basquete", "Volei", "Tenis", "Natacao", "Corrida", "Ciclismo",
    "Judo", "Boxe", "Karate", "Ginastica artistica", "Ginastica ritmica", "Rugby",
    "Beisebol", "Softbol", "Handebol", "Badminton", "Tenis de mesa", "Hipismo",
    "Escalada", "Surfe", "Skate", "BMX", "Canoagem", "Remo", "Arco e flecha",
    "Golfe", "Esgrima", "Patinacao artistica", "Triatlo"]

palavras.sort()

print(palavras)

time.sleep(5)

for texto in palavras:
    pyautogui.click(x=404, y=119)
    pyautogui.hotkey("ctrl","a")
    pyautogui.press("delete")
    pyautogui.write(texto)
    pyautogui.press("enter")
    time.sleep(4)


import winsound
frequency = 2500
duration = 200
for x in range (3): winsound.Beep(frequency, duration)
