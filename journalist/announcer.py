import requests
import os


def request_tts(text, id):
    SPEECH_REGION=os.environ.get("AZURE_COGS_REGION")
    SPEECH_KEY=os.environ.get("AZURE_COGS_KEY")
    endpoint = f"https://{SPEECH_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": SPEECH_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3"
    }
    
    payload = f"""
    <speak version='1.0' xml:lang='ko-KR'>
        <voice xml:lang='ko-KR' xml:gender='Male' name='en-GB-OllieMultilingualNeural'>
            {text}
        </voice>
    </speak>
    """
    
    response = requests.post(endpoint, headers=headers, data=payload)
    if response.status_code == 200:
        with open(f"journalist/tts_audio.mp3", "wb") as audio_file:
            audio_file.write(response.content)
            return f"journalist/tts_audio.mp3"
    else:
        return ""
    
    
if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv()
    text = "안녕하세요. 반갑습니다."
    request_tts(text)