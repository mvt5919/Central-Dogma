import speech_recognition as sr
import webbrowser
import subprocess

####Central Commands####

#audio recording
def audio_command():
	r = sr.Recognizer()
	mic = sr.Microphone()
	print("Listening")

	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	

		try:
			command = r.recognize_google(audio)
			print("Transcript: " + command)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))

		return command

#Google Search
def google_search():
	full_command = command
	search_term = full_command[6:]
	print("Searching")
	if command == "search" + search_term:
		url = "https://www.google.com.tr/search?q={}".format(search_term)    
		webbrowser.open(url)

	else:
		print("Search Failure!")

# Logic behind open command
def program_launch():
	full_command = command
	search_term = full_command[5:]

	print(search_term)
	if command == "open " + search_term:
		programs=({"pale moon":"C:\\Program Files\\Pale Moon\\palemoon.exe",
 		"spotify":"C:\\Users\\miket\\AppData\\Roaming\\Spotify\\Spotify.exe", 
 		"virtualbox":"C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe", 
 		"vpn":"C:\\Program Files (x86)\\VPNetwork LLC\\TorGuard\\TorGuardDesktopQt.exe", 
 		"truecrypt":"C:\\Program Files\\TrueCrypt\\TrueCrypt.exe", 
 		"steam":"C:\\Program Files (x86)\\Steam\\Steam.exe", "opera":"C:\\Program Files\\Opera\\launcher.exe"})
		for key, value in programs.items():
			if key == search_term:
				print("Opening Program")
				subprocess.Popen(['{}'.format(value)])
				break
			else:
				print("Searching...")
				

	else:
		print("Launch Failure!")





print("Deus Ex Startup!")

# Designates audio input as a lowercase string and assigns to variable command
# This will be important when integrating console commands ** command must stay global

temp = audio_command()
command = temp.lower()
print(command)
program_launch()


# open

# search

# exit

#Text/audio interpretation in plain text

#Reaction to text/audio cues

#Reaction dependent features

 