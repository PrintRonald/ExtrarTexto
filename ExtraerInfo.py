import pdfplumber

# Abre el archivo PDF
with pdfplumber.open('C:/Users/madar/Documents/GitHub/ExtrarTexto/Imagen1.pdf') as pdf:
    # Itera sobre cada página del PDF
    for page in pdf.pages:
        # Extrae el texto de cada página
        text = page.extract_text()
        print(text)  # Imprime el texto de la página (puedes hacer otro procesamiento aquí)