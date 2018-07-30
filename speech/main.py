import speech_recognition as sr
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize

r = sr.Recognizer()

speech = True

if speech:

	mic = sr.Microphone()

	with mic as source:
		r.adjust_for_ambient_noise(source, duration = 300)
		print('listening')
		audio = r.listen(source)


	file = open("text.txt", "w")
	file.write(r.recognize_google(audio))
	file.close()

	print(r.recognize_google(audio))

	print()

	readFile = open("text.txt", "r")
	text = readFile.read()

	print("Summary:")
	print(summarize(text, ratio = 0.2))

else:

	print()
	print()

	readFile = open("avengers.txt", "r")
	text = readFile.read()

	print("Summary:")
	print(summarize(text, ratio = 0.2))