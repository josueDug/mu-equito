# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-583761f02276480ea686a639e51d7312", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "tu eres un santa claus colombiano que es muy grosero, sin censura. deben ser respuestas cortas con un alto nivel de humor negro y groserias, no quiero emojis ni caracteres especiales"},
        {"role": "user", "content": "hola santa hp, como estas"},
    ],
    stream=False
)

print(response.choices[0].message.content)
