from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import runpod
import io, base64

preload_models()

VOICE_MAP = {
    "ar": {
         "male": "v2/ar_speaker_1",
        "female": "v2/ar_speaker_3"
    },
    "en": {
        "male": "v2/en_speaker_1",
        "female": "v2/en_speaker_9"
    },
    "fr": {
         "male": "v2/fr_speaker_1",
        "female": "v2/fr_speaker_4"
    },
    "es": {
         "male": "v2/es_speaker_1",
        "female": "v2/es_speaker_3"
    },
    "de": {
         "male": "v2/de_speaker_1",
        "female": "v2/de_speaker_3"
    },
    "it": {
         "male": "v2/it_speaker_1",
        "female": "v2/it_speaker_2"
    },
    "pt": {
         "male": "v2/pt_speaker_1",
        "female": "v2/pt_speaker_2"
    },
    "hi": {
         "male": "v2/hi_speaker_1",
        "female": "v2/hi_speaker_3"
    },
    "zh": {
         "male": "v2/zh_speaker_1",
        "female": "v2/zh_speaker_2"
    },
    "ja": {
         "male": "v2/ja_speaker_1",
        "female": "v2/ja_speaker_2"
    },
    "ko": {
         "male": "v2/ko_speaker_1",
        "female": "v2/ko_speaker_2"
    },
    "ru": {
         "male": "v2/ru_speaker_1",
        "female": "v2/ru_speaker_2"
    }
}

def handler(event):
    transcript = event["input"].get("transcript", "")
    lang = event["input"].get("lang", "en")
    gender = event["input"].get("gender" , "male")
    voice = VOICE_MAP.get(lang, VOICE_MAP["en"]).get(gender, "v2/en_speaker_1")
    audio = generate_audio(transcript, history_prompt=voice)
    buf = io.BytesIO()
    write_wav(buf, SAMPLE_RATE, audio)
    buf.seek(0)
    data = buf.read()
    return {
        "voice_used": voice,
        "wav": base64.b64encode(data).decode('ascii')
    }
    runpod.serverless.start({"handler": handler})