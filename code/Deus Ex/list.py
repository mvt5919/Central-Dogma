def program_paths():
	programs=({"pale moon":"C:\\Program Files\\Pale Moon\\palemoon.exe",
 "spotify":"C:\\Users\\miket\\AppData\\Roaming\\Spotify\\Spotify.exe", 
 "virtual box":"C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe", 
 "vpn":"C:\\Program Files (x86)\\VPNetwork LLC\\TorGuard\\TorGuardDesktopQt.exe", 
 "true crypt":"C:\\Program Files\\TrueCrypt\\TrueCrypt.exe", 
 "steam":"C:\\Program Files (x86)\\Steam\\Steam.exe", "opera":"C:\\Program Files\\Opera\\launcher.exe"})

# Logic behind open command
def program_launch():
	full_command = command
	search_term = full_command[4:]

	print("Opening Program")

	if command == "open" + search_term:
		program_paths()
		for key, value in programs.items():
			if key == search_term:
				print(value)
				subprocess.Popen(['{}'.format(value)])

	else:
		print("Launch Failure!")





# for x in programs:
# 	if x == search_term:
# 		print(x)
# 	else:
# 		print("Not it")


