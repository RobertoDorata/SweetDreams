import openai
from gtts import gTTS
import playsound
language = 'it'
openai.api_key = ""
sogno_generato = openai.Completion.create(
    model="curie:ft-hanaku-2022-02-25-10-37-27",
    prompt="sogni_fiorella",
max_tokens=500)
sogno_generato = sogno_generato["choices"][0]['text']
myobj = gTTS(text=sogno_generato, lang=language, slow=False)
#salva l'audio in file mp3
myobj.save("sogno.mp3")
print(sogno_generato)
#aspetta di terminare la riproduzione del file audio
blocking = True
playsound.playsound("sogno.mp3", block=blocking)



