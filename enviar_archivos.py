from google import genai
import os

api_key = "AIzaSyCr3ossVKhar7DatX_rtAyYHXtnOcxhbgE"

cliente = genai.Client(api_key=api_key)

archivo_csv = cliente.files.upload(
    file="korea_japon.2022.txt"
)

respuesta = cliente.models.generate_content(
    model = "gemini-2.5-flash",
    contents=[
        archivo_csv,
        "Calcula el promedio de Gol de Costa Rica a partir de los datos brindados"
    ]
)

print("La repuesta de la conexión con la IA es", respuesta.text)
print()
