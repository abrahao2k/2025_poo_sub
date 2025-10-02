# IMAGEM NO PDF

from fpdf import FPDF
pdf = FPDF()
pdf.add_page()

pdf.image("pepsi.png", x=10, y=10, w=30, h=30, link="https://www.pepsi.com")

pdf.set_xy(50,20) # move o cursor para o texto não sobrepor a imagem

pdf.set_text_color(0,0,255) # cor azul
pdf.set_font("Arial", size=12, style="U") # estilo sublinhado
pdf.write(5, 'Acesse o site da PEPSI', link="https://www.pepsi.com")

pdf.output("imagem.pdf")
print("Arquivo criado com sucesso.")

import os
os.startfile("imagem.pdf")