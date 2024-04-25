from extract4pdf import pdf_text
import re

# Llamar a la función pdf_text para obtener el texto del PDF
texto = pdf_text

# Usar expresión regular para encontrar la palabra después de "No. Remisión:"
no_remision = re.search(r'(?<=No\. Remisión:)\s*(\S+)', texto)
#fecha_reposicion = re.search(r'(?<=No\. Reposición:)\s*(\S+)', texto)


print("No. Remisión:", no_remision.group(1))
#print("Fecha de Reposición:", fecha_expedicion.group(1))




