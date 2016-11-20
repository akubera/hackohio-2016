import speech_recognition as sr
import wave
import struct

f = open('test_output.txt','rb')
filedata = f.read()
print(filedata)
length = len(filedata)

CHANNELS = 1
RATE = 8000

wavef = wave.open('chipsound.wav','w')
wavef.setnchannels(CHANNELS)
wavef.setsampwidth(1)
wavef.setframerate(RATE)
wavef.setnframes(length//2)

r = sr.Recognizer()
r.energy_threshold = 100
data = struct.unpack_from('<'+'H'*(length//2), filedata)

print(data)
for i in data:
    wavef.writeframes(bytes(i))

print('debug')
wavef.close()

with sr.AudioFile("chipsound.wav") as source:
    audio_data = r.listen(source)
    try:
        transcription = r.recognize_google(audio_data)
        print(transcription)
    except sr.UnknownValueError:
        print("What did you say?")

