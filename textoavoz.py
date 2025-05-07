import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

load_dotenv()

client = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = client.text_to_speech.convert(
    text="Jajajaja Santa hijueputa, Qué descaro, gonorrea Pero bueno, aquí ando, más borracho que costeño en diciembre, repartiendo regalos del dollarcity a los que se portaron bien y a los malcriados del justo y bueno, porque pa qué ser tan hijueputa.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)
