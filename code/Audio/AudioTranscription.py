import speech_recognition as sr


r = sr.Recognizer()

SOUND_FILE = sr.AudioFile('harvard.wav')
	
with SOUND_FILE as source:
	r.adjust_for_ambient_noise(source)
	audio = r.record(source)


try:
    print("Transcript: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))