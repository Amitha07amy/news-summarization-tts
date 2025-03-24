from gtts import gTTS
import os

def text_to_speech(text, lang='hi'):
    tts = gTTS(text=text, lang=lang, slow=False)
    output_path = "output.mp3"
    tts.save(output_path)
    return output_path  # Return the file path
