import pyaudio
import wave

audio = pyaudio.PyAudio()

moth = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

try: 
    while True:
        data = moth.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

moth.stop_stream()
moth.close()
audio.terminate()

sound_file = wave.open("moth-hearing.wav","wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))