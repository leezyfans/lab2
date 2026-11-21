import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # make sure logs.txt / notes.txt are found

from openai import OpenAI

# Part D: RAG - give the model notes first
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

logs = open("logs.txt").read()
notes = open("notes.txt").read()
prompt = f"Using these notes:\n{notes}\n\nSummarise the REAL problems in these logs:\n{logs}"

reply = client.chat.completions.create(
    model="qwen3.5:4b",
    messages=[{"role": "user", "content": prompt}],
)
print(reply.choices[0].message.content)
