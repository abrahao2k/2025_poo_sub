from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_xy(40,30)

longo = "Estou com fome. Que horas é a merenda? Tem coxinha? Eu quero uma!"
pdf.multi_cell(50, 5, txt = longo, align='J')

pdf.set_xy(100,30)
pdf.multi_cell(50, 5, txt = longo, align='J')

pdf.output("varias_linhas.pdf")
print("Arquivo criado com sucesso.")