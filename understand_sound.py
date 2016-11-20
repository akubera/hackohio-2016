import speech_recognition as sr
import wave
import struct

f = open('new_test_output.txt','rb')
filedata = f.read()
length = len(filedata)

CHANNELS = 1
RATE = 8000

wavef = wave.open('chipsound.wav','w')
wavef.setnchannels(CHANNELS)
wavef.setsampwidth(1)
wavef.setframerate(RATE)
#wavef.setnframes(4000)

r = sr.Recognizer()
r.energy_threshold = 10
data_int = struct.unpack_from('<'+'H'*(length//2), filedata)
for j in data_int:
    j = j//4
    data = struct.pack('<'+'H',j)
    wavef.writeframesraw(data)

wavef.close()

with sr.AudioFile("chipsound.wav") as source:
    audio_data = r.listen(source)
    try:
        transcription = r.recognize_google(audio_data)
        print(transcription)
    except sr.UnknownValueError:
        print("What did you say?")
