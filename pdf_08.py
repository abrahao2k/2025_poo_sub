# CONFIGURAR MARGENS DA PÁGINA
from fpdf import FPDF

pdf = FPDF()

pdf.set_margins(25,25,25)

pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.write(5, "Meu texto.")

pdf.output("margens.pdf")

import os
os.startfile("margens.pdf")