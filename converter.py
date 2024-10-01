from gtts import gTTS


class Converter:

    def __init__(self):
        pass

    # convert text to speech and save as mp3
    def text_to_speech(self, text, audio_output):

        # handling exceptions like if text is None

        try:
            tts = gTTS(text=text, lang='en')
            tts.save(audio_output)
            print(f"Audio saved as {audio_output}")
        except Exception as e:
            print(f"Error in converting text to speech: {e}")
