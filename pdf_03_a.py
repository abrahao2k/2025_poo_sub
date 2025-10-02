from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Define a cor do texto para vermelho (RGB: 255, 0, 0)
pdf.set_text_color(255, 0, 0)
pdf.cell(0, 10, txt="Texto em vermelho", ln=True)

# Define a cor do texto para azul (RGB: 0, 0, 255)
pdf.set_text_color(0, 0, 255)
pdf.cell(0, 10, txt="Texto em azul", ln=True)

pdf.output("cores.pdf")
print("Arquivo criado com sucesso.")