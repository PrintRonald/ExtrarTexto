import pytesseract
from PIL import Image

# Especifica la ruta de la imagen
ruta_imagen = r'C:\Users\madar\Documents\GitHub\ExtrarTexto\Imagen1.jpeg'

# Carga la imagen usando PIL (Python Imaging Library)
imagen = Image.open(ruta_imagen)

# Utiliza pytesseract para extraer el texto de la imagen
texto_extraido = pytesseract.image_to_string(imagen)

# Imprime el texto extraído
print(texto_extraido)
print(type(texto_extraido))