# CONFIGURAR TAMANHO E ORIENTAÇÃO DA PÁGINA
from fpdf import FPDF

pdf = FPDF(orientation='P', unit="mm", format="a4")
pdf.add_page()

# modificar uma página
pdf.add_page(orientation='L')

pdf.add_page()

pdf.output("deitada.pdf")

# abrir o documento no visualizador padrão do windows
import os
os.startfile("deitada.pdf")
