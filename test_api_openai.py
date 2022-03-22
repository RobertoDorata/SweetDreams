import os
import openai

openai.File.create(
  file=open("sogni-fiorella.txt"),
  purpose='fine-tune'
)

openai.FineTune.create(training_file="file-VpNVEU8zYbyeUHBdrwDwz81a", model="curie", batch_size=128, learning_rate_multiplier=0.05)

openai.FineTune.retrieve(id="ft-gKCFFZuHHq2oa3NIH7x1rD8R")

content = openai.File.download("file-udVuCFtjAPpDSROVmGjaN0xo")

openai.Completion.create(
    model="curie:ft-hanaku-2022-02-25-10-37-27",
    prompt="sogni_fiorella",
max_tokens=500)

openai.api_key = os.getenv("")
openai.FineTune.list_events(id="ft-gKCFFZuHHq2oa3NIH7x1rD8R")



