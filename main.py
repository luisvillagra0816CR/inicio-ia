
from google import genai

api_key = "AIzaSyCr3ossVKhar7DatX_rtAyYHXtnOcxhbgE"

cliente = genai.Client(api_key=api_key)

respuesta = cliente.models.generate_content(
    model = "gemini-2.5-flash",
    #contents="Escribe un poema acerca de las flores, pero dame solo el poema, sin título y sin texto adicional" # prompt
    contents="""
    Genera un CSV con los marcadores de los partidos del mundial Korea Japon 2002.
    Sin título y sin texto adicional. Sin etiquetas de Markdown.
    En la primera columna el país Casa, en la segunda el país vista, la cantidad de goles
    del equipo casa y en la última columna la cantidad de goles del equipo visita.
    Coloca los partidos en orden.
    """

)

with open("korea_japon.2022.txt", mode="w", encoding="utf-8") as archivo:
    archivo.write(respuesta.text)