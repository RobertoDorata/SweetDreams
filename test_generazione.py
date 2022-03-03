import openai
import json
from gtts import gTTS
import os
language = 'it'
openai.api_key = "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"
sogno_generato = openai.Completion.create(
    model="curie:ft-hanaku-2022-02-25-10-37-27",
    prompt="sogni_fiorella",
max_tokens=500)
sogno_generato = sogno_generato["choices"][0]['text']
myobj = gTTS(text=sogno_generato, lang=language, slow=False)
# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")
print(sogno_generato)
import playsound

# wait for the sound to finish playing?
blocking = True

playsound.playsound("welcome.mp3", block=blocking)



