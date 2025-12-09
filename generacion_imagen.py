from google import genai

api_key = "AIzaSyCr3ossVKhar7DatX_rtAyYHXtnOcxhbgE"

cliente = genai.Client(api_key=api_key)


respuesta = cliente.models.generate_content(
    model="gemini-2.5-flash-image",
    contents="Genera una imagen de un perro en bicileta"
)

for part in respuesta.parts:
    if part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")