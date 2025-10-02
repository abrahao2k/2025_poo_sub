# NUMERAÇÃO DE PÁGINA
from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15) # 15mm de baixo para cima
        self.set_font("Arial", size=10)
        self.cell(0,10,f"Página {self.page_no()}", align="R")

pdf = PDF()

pdf.add_page()
pdf.add_page()
pdf.add_page()

pdf.output("numeracao.pdf")

import os
os.startfile("numeracao.pdf")