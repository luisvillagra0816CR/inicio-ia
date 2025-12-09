
from openai import OpenAI

api_key = "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"

cliente = OpenAI(api_key=api_key)

respuesta = cliente.chat.completions.create(
    model = "gpt-4o",
    messages=[
        {
            "role": "user",
            "content": """
                Genera un CSV con los marcadores de los partidos del mundial Korea Japon 2002.
                Sin título y sin texto adicional. Sin etiquetas de Markdown.
                En la primera columna el país Casa, en la segunda el país vista, la cantidad de goles
                del equipo casa y en la última columna la cantidad de goles del equipo visita.
                Coloca los partidos en orden.
            """
        }
    ],
    temperature=0.5
)



with open("korea_japon.2022_gpt_.txt", mode="w", encoding="utf-8") as archivo:
    archivo.write(respuesta.choices[0].message)

print("Ciao!")
