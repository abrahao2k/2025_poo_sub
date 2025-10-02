from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12, style="B")

pdf.set_text_color(255,0,0) # mudar a cor do texto
pdf.cell(90, 5, txt="Meu texto colorido.", ln=True, align='L')

pdf.set_font("Arial", size=12, style="I")

pdf.set_text_color(0,255,0) # mudar a cor do texto
pdf.cell(90, 5, txt="Meu texto colorido.", ln=True, align='L')

pdf.set_font("Arial", size=12, style="U")

pdf.set_text_color(0,0,255) # mudar a cor do texto
pdf.cell(90, 5, txt="Meu texto colorido.", ln=True, align='L')

pdf.output("cores.pdf")
print("Arquivo criado com sucesso.")

