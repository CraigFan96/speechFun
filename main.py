import speech_recognition as sr
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize

r = sr.Recognizer()

mic = sr.Microphone()
"""
with mic as source:
	r.adjust_for_ambient_noise(source, duration = 0.5)
	print('listening')
	audio = r.listen(source)


file = open("text.txt", "w")
file.write(r.recognize_google(audio))

print(r.recognize_google(audio))
"""
print()
print()

readFile = open("avengers.txt", "r")
text = readFile.read()

print("Summary:")
print(summarize(text, ratio = 0.3))


"""
text = sr.AudioFile('speech.wav')
with text as source:
	r.adjust_for_ambient_noise(source, duration = 0.5)
	audio = r.record(source)
	print(r.recognize_google(audio))
"""