# TABELAS
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

dados=[
    ["Nome", "Idade", "Cidade"],
    ["Ana","25","Mossoró"],
    ["Bruno","32","Natal"],
    ["Carla","19","Apodi"]
    ]

for linha in dados:
    pdf.cell(50,10,linha[0],border=1)
    pdf.cell(30,10,linha[1],border=1)
    pdf.cell(50,10,linha[2],border=1)
    pdf.ln(10) #pular pra linha seguinte

pdf.output("tabela.pdf")

import os
os.startfile("tabela.pdf")