from google import genai
from dotenv import load_dotenv
import os, io
from gtts import gTTS

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_note(images):
    prompt = "Generate a note summery for these given images and ensure to make it markdown response within 100 words"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text


def generate_audio(notes):
    speech = gTTS(text=notes, lang="en", slow=False)

    audio_buffer = io.BytesIO()

    speech.write_to_fp(audio_buffer)
    # gTTS.save(audio_buffer)

    return audio_buffer
  