
import os
from dotenv import load_dotenv
import requests

load_dotenv()
endpoint = "https://southeastasia.tts.speech.microsoft.com/cognitiveservices/v1"
SPEECH_API_KEY = os.environ.get('SPEECH_API_KEY')

def text_to_speech(text, file_name='response_audio.wav'):
    print(SPEECH_API_KEY)
    headers = {
        "Ocp-Apim-Subscription-Key": SPEECH_API_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3"
    }
    payload = f"""<speak version='1.0' xml:lang='en-US'>
    <voice xml:lang='ko-KR' xml:gender='Female' name='ko-KR-SeoHyeonNeural'>
    {text}
    </voice>
    </speak>"""
    response = requests.post(endpoint, headers=headers, data=payload)
    if response.status_code == 200:
        with open(file_name, 'wb') as audio_file:
            audio_file.write(response.content)
        return file_name
    else:
        print(response.status_code)
        return None
    
if __name__ == "__main__":
    text_to_speech("오늘의 아나운서. 원종은 입니다. 와타시와 칸코쿠진 데스스")