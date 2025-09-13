from gtts import gTTS
import subprocess
import platform

#Step1a: Setup Text to Speech–TTS–model with gTTS
def text_to_speech_with_gtts(input_text, output_filepath):
    language = 'en'
    audio_obj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audio_obj.save(output_filepath)    

#Step2: Use Model for Text output to Voice
def text_to_speech_with_gtts_with_VoiceOutput(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-File', 'play_audio.ps1'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

if __name__ == "__main__":
    input_text = "Hello. How are you?"
    output_filepath = "data\\doctor_voice\\test1.wav"
    #text_to_speech_with_gtts(input_text, output_filepath)
    text_to_speech_with_gtts_with_VoiceOutput(input_text, output_filepath)