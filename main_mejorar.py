
from google import genai

api_key = "AIzaSyCr3ossVKhar7DatX_rtAyYHXtnOcxhbgE"

cliente = genai.Client(api_key=api_key)

entrada_usuario = input("Ingrese un texto para ser mejorado")

respuesta = cliente.models.generate_content(
    model = "gemini-2.5-flash",
    contents= f"Mejora el siguiente texto y corrije las faltas de ortografía. Revisa bien el contexto completo, votamos es de botar y no de votar. Solo dame el texto resultante: {entrada_usuario}"    

)

print(respuesta.text)