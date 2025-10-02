# LINK EM UM TEXTO

from fpdf import FPDF
pdf = FPDF()
pdf.add_page()

pdf.set_text_color(0,0,255) # cor azul
pdf.set_font("Arial", size=12, style="U") # estilo sublinhado

#write ou cell
pdf.write(5, 'Acesse o site do IFRN', link="https://www.ifrn.edu.br")

pdf.output("link.pdf")
print("Arquivo criado com sucesso.")

