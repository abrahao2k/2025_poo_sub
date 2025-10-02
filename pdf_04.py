from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.write(8,"O Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte (IFRN) foi fundado em 1909, como parte de uma ação político-educacional do presidente Nilo Peçanha, visando oferecer educação primária e profissional aos filhos de trabalhadores. Através do Decreto n.º 7.566, foram criadas 19 Escolas de Aprendizes Artífices, que marcaram o início da trajetória do IFRN na educação profissional no Brasil.")

pdf.set_font("Arial", size=12, style="B")

pdf.text(30, 60, 'Texto fixo aqui')

pdf.output("text_write.pdf")
print("Arquivo criado com sucesso.")

