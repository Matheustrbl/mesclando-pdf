"""
Este é um script que mescla arquivos PDF
e utiliza a biblioteca PyPDF2 para realizar a mesclagem.
"""

import os  # biblioteca para manipulação de caminhos de arquivos
import PyPDF2  # biblioteca para manipular arquivos pdf

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("PDFS")
print(lista_arquivos)

for PDFS in lista_arquivos:
    if ".pdf" in PDFS:
        merger.append(f"PDFS/{PDFS}")

merger.write("PDF Final.pdf")
