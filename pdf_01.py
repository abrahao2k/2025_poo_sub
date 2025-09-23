from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

nome = input("Digite seu nome: ")

pdf.cell(50, 5, txt = nome, ln=False, align='L')
pdf.cell(90, 5, txt="Estou gostando disso.", ln=True, align='L')

pdf.output("meu_arquivo.pdf")
print("Arquivo criado com sucesso.")

