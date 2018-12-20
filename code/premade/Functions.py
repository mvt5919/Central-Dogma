#ideas, useful sorting, calculation of numbers, sorting of values, audio frameworks, useful classes, 
#Try/Except handling, Api autocalls with try except handling(how to return all values from api?)

#API Calls

def callPYOWM():
	# Calls PYOWM Module, API calls are limited to 10 minute intervals before ban
	import pyowm
	
	owm = pyowm.OWM('2e98671aef6d8c2afd8fa291d2192f2e')
	observation = owm.weather_at_place('Lafayette,us')
	w = observation.get_weather()
	
	print(w.get_wind())
	print(w.get_humidity())
	print(w.get_temperature('fahrenheit'))

def callspeechrec():

	#Calls speech_recognition module, accepts audio input and queries to google to analyze, limited to 
	# 50 queries per day
	import speech_recognition as sr
	
	r = sr.Recognizer()
	mic = sr.Microphone()

	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	print(r.recognize_google(audio))