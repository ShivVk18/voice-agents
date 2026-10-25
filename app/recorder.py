import sounddevice as sd
from scipy.io.wavfile import write




def record_audio(file_name:str="recording.wav",duration:int=5,sample_rate: int = 16000):
    print("🎤 Recording... Speak now!")
    
    audio = audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16",
    device=0
)
    sd.wait()
    
    write(filename=file_name,rate=sample_rate,data=audio)
    
    print("✅ Recording saved!")
    
    return file_name