from fpdf import FPDF
pdf = FPDF()
pdf.add_page()

## CABEÇALHO #################################################
pdf.image("pepsi.png", x=10, y=10, w=15)
pdf.set_font("Arial", size=10, style="B")
texto="PEPSICO\nRua das Indústrias, SN\nwww.pepsi.com.br"
pdf.set_xy(30,10)
pdf.multi_cell(0,5,txt=texto)

pdf.set_xy(0,30)
pdf.cell(0,10,"ORÇAMENTO", align="C")

## CLIENTE ##################################################
pdf.set_xy(10,45)

nome = input("Nome do Cliente: ")
contato = input("Contato do Cliente: ")

pdf.cell(0,7, "Cliente: " + nome, ln=True)
pdf.cell(0,7, "Contato: " + contato)

## PRODUTOS #################################################
produtos = [ ["Nome","Valor","Qtd","Total"] ]
total_orca = 0
for x in range(5):
    prod = input("Nome do produto: ")
    valor = float(input("Valor do produto: "))
    qtd   = int(input("Qtd produto: "))
    total = valor * qtd
    produtos.append([prod,valor,qtd,total])
    
    total_orca += total #calcula o total do orçamento

pdf.set_xy(10,70)

for linha in produtos:
    pdf.cell(60,10,linha[0],align="L", border=1)
    pdf.cell(40,10,str(linha[1]),align="R", border=1)
    pdf.cell(40,10,str(linha[2]),align="C", border=1)
    pdf.cell(40,10,str(linha[3]),align="R", border=1)
    pdf.ln(10)

pdf.set_xy(10,140)
pdf.cell(0,7,"Total do Orçamento = R$ " + str(total_orca))


pdf.output("orcamento.pdf")

import os
os.startfile("orcamento.pdf")